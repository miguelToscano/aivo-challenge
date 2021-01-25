import flask
import pandas as pd

from services import indicators as indicators_service
from validators import indicators as indicators_validator
app = flask.Flask('aivo-challenge')

@app.route('/indicators', methods = ['GET'])
def get_columns():
    
    return flask.make_response(
        flask.jsonify({ 'indicators' : indicators_service.get_indicators()}),
        200,
    )

@app.route('/inequality', methods = ['GET'])
def get_inequality():

    try:

        indicator = flask.request.args.get('indicator')
        value = flask.request.args.get('value')
        inequality = flask.request.args.get('inequality')

        indicators_validator.validate_get_inequality(indicator, value, inequality)

        data = indicators_service.get_inequality(indicator, value, inequality)

        return flask.make_response(
            flask.jsonify({ 'filtered_by': data['filtered_by'], 'results' : data['countries_inequalities']}),
            200,
        )

    except Exception as error:

        return flask.make_response(
            flask.jsonify({ 'message': error.args[0] }),
            error.args[1],
        )

app.run()