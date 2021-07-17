import requests
import json
import datetime
import logging
import pathlib
import os
import schedule
import time
from corona_api.corona_api.settings.production import DATABASES, FETCH_SETTINGS
from database import Database, ENTITIES, REPORTS

DB_SETTINGS = DATABASES['default']
URL = 'https://data.korona.gov.sk/api/'


def _fetch():
    logging.basicConfig(filename=os.path.join(pathlib.Path(__file__).parent.resolve(), 'fetch_logs.log'),
                        level=logging.INFO,
                        format='%(asctime)s;%(levelname)s;%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    db = Database(DB_SETTINGS['HOST'], DB_SETTINGS['NAME'], DB_SETTINGS['USER'], DB_SETTINGS['PASSWORD'])

    logging.info('Fetching new data.')
    # fetch entities
    for entity in ENTITIES:
        result = None
        try:
            result = requests.get(URL + entity.alt_name)
        except Exception:
            logging.error('Unable to fetch entity {}'.format(entity.table_name), exc_info=True)
            exit(1)

        data = json.loads(result.text)

        # insert fetched data into database
        try:
            db.execute_values(entity.get_insert_statement(), data, entity.get_insert_template(), page_size=len(data))
        except Exception:
            logging.error('Unable to insert fetched entity {} into database.'.format(entity.table_name), exc_info=True)
            # if we are unable to insert data into database, terminate the script, because the schema of datasource has
            # been probably changed in the meantime
            db.rollback()
            exit(1)

    # fetch reports
    for report in REPORTS:
        # get the last report so we fetch only reports that were added after the latest report
        last_update_date = db.execute('SELECT updated_at FROM {}'
                                      ' ORDER BY updated_at DESC LIMIT 1;'.format(report.table_name))

        params = {}
        if last_update_date:
            # set query parameters if we found any previous reports in the local database
            last_update_date = last_update_date[0]['updated_at']
            last_update_date = last_update_date + datetime.timedelta(hours=0, seconds=1)
            last_update_date = last_update_date.strftime('%Y-%m-%d %H:%M:%S')
            params['updated_since'] = last_update_date

        next_offset = True
        result = None

        # repeat fetch until all reports are fetched
        while next_offset:
            try:
                result = requests.get(URL + report.alt_name,
                                      params=params
                                      )
            except Exception:
                logging.error('Unable to fetch report {}'.format(report.table_name), exc_info=True)
                exit(1)

            data = json.loads(result.text)

            if data['page']:
                try:
                    db.execute_values(report.get_insert_statement(), data['page'], report.get_insert_template(),
                                      page_size=len(data['page']))
                except Exception:
                    logging.error('Unable to insert fetched report {} into database.'.format(report.table_name),
                                  exc_info=True)
                    # if we are unable to insert data into database terminate the script, because the schema of
                    # datasource has been probably changed in the meantime
                    db.rollback()
                    exit(1)

            if data['next_offset']:
                params['offset'] = data['next_offset']
            else:
                next_offset = False

            result = None

    db.close()


if __name__ == '__main__':
    _fetch()
    schedule.every().day.at(FETCH_SETTINGS['TIME']).do(_fetch)
    while True:
        schedule.run_pending()
        time.sleep(5)
