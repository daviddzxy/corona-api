import requests
import json
import time
import datetime
from requests import exceptions as rexceptions
from corona_api.settings import DATABASES
from database import Database, ENTITIES, REPORTS

DB_SETTINGS = DATABASES['default']
URL = 'https://data.korona.gov.sk/api/'

if __name__ == '__main__':
    db = Database(DB_SETTINGS['HOST'], DB_SETTINGS['NAME'], DB_SETTINGS['USER'], DB_SETTINGS['PASSWORD'])
    for entity in ENTITIES:
        result = None
        while result is None:
            try:
                result = requests.get(URL + entity.alt_name)
            except (rexceptions.RequestException, rexceptions.ConnectionError, rexceptions.ConnectTimeout):
                time.sleep(60)
        data = json.loads(result.text)
        try:
            db.execute_values(entity.get_insert_statement(), data, entity.get_insert_template(), page_size=len(data))
        except Exception:
            db.rollback()
            exit(1)

    for report in REPORTS:
        last_update_date = db.execute('SELECT updated_at FROM {}'
                                      ' ORDER BY updated_at DESC LIMIT 1;'.format(report.table_name))

        params = {}
        if last_update_date:
            last_update_date = last_update_date[0]['updated_at']
            last_update_date = last_update_date + datetime.timedelta(hours=0, seconds=1)
            last_update_date = last_update_date.strftime('%Y-%m-%d %H:%M:%S')
            params['updated_since'] = last_update_date

        next_offset = True
        result = None
        while next_offset:
            while result is None:
                try:
                    result = requests.get(URL + report.alt_name,
                                          params=params
                                          )
                except (rexceptions.RequestException, rexceptions.ConnectionError, rexceptions.ConnectTimeout) as e:
                    db.rollback()
                    exit(1)

            data = json.loads(result.text)

            if data['page']:
                try:
                    db.execute_values(report.get_insert_statement(), data['page'], report.get_insert_template(),
                                      page_size=len(data['page']))
                except Exception as e:
                    db.rollback()
                    exit(1)

            if data['next_offset']:
                params['offset'] = data['next_offset']
            else:
                next_offset = False

            result = None

    db.close()
