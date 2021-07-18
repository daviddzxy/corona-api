# corona-api
This project is a reimplementation of the [data.korona.gov.sk API](https://data.korona.gov.sk/). The original API does not support querying of reports by entity id to which the report belongs to and it also does not allow querying reports by published on date field. This API reimplementation allows such queries, making it suitable as a backend service for web based clients. The original API is used as a datasource for this reimplementation. The schema and examples of this api can be found [here](https://corona-api-sk.herokuapp.com/api/schema/swagger/).

To run this API locally follow these instructions.
```
1. Git clone https://github.com/daviddzxy/corona-api
2. cd corona-api
3. Set up your PostgreSQL database and change the database settings in file corona_api/corona_api/settings/common.py
4. pip install -r requirements.txt
5. python corona_api/manage.py migrate
6. python corona_api/manage.py runserver # server now runs locally
7. python data_fetch/fetch.py # fetch data from the original API, this script fetches new data every day at 01:00 AM by default, to change the fetching time change the FETCH_SETTINGS in corona_api/corona_api/settings/common.py
```
