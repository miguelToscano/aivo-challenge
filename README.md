## Requirements
- python 3
- pip 3
- virtualenv

## Installations steps

- Clone this repository
- `cd aivo-challenge`
- Create and activate a virtual environment
- Run `pip3 install -r requirements.txt`

## Run

- `python3 app.py`

## cURLs

- **GET /indicators** `curl --location --request GET 'http://localhost:5000/indicators'`
Returns a list of possible indicator values

- **GET /inequalities** `curl --location --request GET 'http://localhost:5000/inequalities'`
Returns a list of possible inequality values

- **GET /inequality** `curl --location --request GET 'http://localhost:5000/countries?indicator=SW_LIFS&value=1&inequality=Total'`
By providing `indicator`, `value`, `inequality` (optional) a list of countries with their inequality values is returned. Possible `indicator` and `inequality` values are the ones returned by the GET `/indicators` and GET `/inequalities` endpoints respectively.
