## Requirements
- python 3
- pip 3
- virtualenv

## Installations steps

- Clone this repository
- `cd CURRENT_PATH/aivo-challenge`
- run `pip3 install -r requirements.txt`

## Run

- `python3 app.py`

## cURLs

- GET /indicators `curl --location --request GET 'http://localhost:5000/indicators'`
Returns a list of posible indicator values

- GET /inequalities `curl --location --request GET 'http://localhost:5000/inequalities'`
Returns a list of posible inequality values

- GET /inequality `curl --location --request GET 'http://localhost:5000/countries?indicator=SW_LIFS&value=1&inequality=Total'`
By providing `indicator`, `value`, `inequality` (optional) a list of countries with their inequality values is returned. Posible `indicator` and `inequality` values are the ones returned by the GET `/indicators` and GET `/inequalities` endpoints respectively.
