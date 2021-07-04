import psycopg2
from psycopg2.extras import execute_values, RealDictCursor


class Table():
    def __init__(self, table_name, fields, alt_name=None):
        self.fields = fields
        self.table_name = table_name
        self.alt_name = alt_name

    def get_insert_statement(self):
        return 'INSERT INTO {} ({}) values %s ON CONFLICT DO NOTHING;'.format(self.table_name, ', '.join(self.fields))

    def get_insert_template(self):
        return '({})'.format(', '.join(['%({})s'.format(field) for field in self.fields]))


class Database():
    def __init__(self, host, db_name, user, password):
        self.conn = psycopg2.connect(host=host,
                                     database=db_name,
                                     user=user,
                                     password=password)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)

    def execute_values(self, query, data, query_template, page_size):
        execute_values(self.cur, query, data, query_template, page_size)
        self.conn.commit()

    def execute(self, query):
        self.cur.execute(query)
        return self.cur.fetchall()

    def rollback(self):
        self.conn.rollback()

    def close(self):
        self.cur.close()
        self.conn.close()


ENTITIES = [Table('api_region', ['id', 'title', 'code', 'abbreviation'], 'regions'),
            Table('api_vaccine', ['id', 'title', 'manufacturer'], 'vaccines'),
            Table('api_district', ['id', 'title', 'code', 'region_id'], 'districts'),
            Table('api_city', ['id', 'title', 'code', 'district_id'], 'cities'),
            Table('api_hospital', ['id', 'title', 'code', 'city_id'], 'hospitals')]

REPORTS = [Table('api_vaccinationreport',
                   ['id', 'dose1_count', 'dose2_count', 'updated_at', 'published_on', 'region_id', 'vaccine_id'],
                   'vaccinations'),
           Table('api_agtestsreport',
                   ['id', 'positivity_rate', 'positives_count', 'negatives_count', 'positives_sum', 'negatives_sum',
                    'updated_at', 'published_on', 'district_id'],
                   'ag-tests/by-district'),
           Table('api_bedsreport',
                   ['id', 'capacity_all', 'free_all', 'capacity_covid', 'occupied_jis_covid', 'occupied_oaim_covid',
                    'occupied_o2_covid', 'occupied_other_covid', 'reported_at', 'updated_at', 'published_on',
                    'hospital_id'],
                   'hospital-beds'),
           Table('api_hospitalstaffreport',
                   ['id', 'out_of_work_ratio_doctor', 'out_of_work_ratio_nurse', 'out_of_work_ratio_other',
                    'updated_at', 'published_on', 'hospital_id'],
                   'hospital-staff'),
           Table('api_patientsreport',
                   ['id', 'ventilated_covid', 'non_covid', 'confirmed_covid', 'suspected_covid', 'updated_at',
                    'published_on', 'hospital_id'],
                   'hospital-patients')
           ]
