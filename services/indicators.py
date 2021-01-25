import pandas as pd
import numpy as np
import errors

def get_indicators():

    try:

        df_temp = pd.read_csv('./data/indicators.csv', usecols = ['Indicator', 'INDICATOR', 'Unit'])
        df_temp = df_temp.rename(columns = {'Indicator': 'description', 'INDICATOR': 'indicator', 'Unit': 'unit'})
        indicators = df_temp.drop_duplicates().to_dict(orient = 'records')

        return indicators

    except:

        raise Exception('Could not read data file', errors.INTERNAL_SERVER_ERROR_CODE)


def get_inequality(indicator, value, inequality = None):

    try:

        df_indicators = pd.read_csv('./data/indicators.csv', usecols = ['Country', 'Inequality', 'Value', 'INDICATOR', 'Indicator', 'Unit'])

    except:

        raise Exception('Could not read data file', errors.INTERNAL_SERVER_ERROR_CODE)

    try: 

        df_indicators = df_indicators.rename(columns = {'Indicator': 'description'})
        df_indicators.columns = df_indicators.columns.str.lower()

        data_by_indicator = df_indicators[df_indicators['indicator'] == str(indicator)]

        if inequality != None:

            data_by_indicator = data_by_indicator[data_by_indicator['inequality'] == str(inequality)]

        data_by_indicator = data_by_indicator[data_by_indicator['value'] > float(value)]
        countries_columns = ['country', 'value', 'inequality']
        indicator_columns = ['description', 'indicator', 'unit']

        filtered_by = {
            'criteria': 'greater than ' + str(value),
            'indicator': str(indicator),
            'unit': df_indicators[df_indicators['indicator'] == str(indicator)].iloc[0].unit,
            'description': df_indicators[df_indicators['indicator'] == str(indicator)].iloc[0].description,
        } 
     
        response = {
            'countries_inequalities': data_by_indicator[countries_columns].to_dict(orient = 'records'),
            'filtered_by': filtered_by
        }

        return response

    except:

        raise Exception('Error geting values', errors.INTERNAL_SERVER_ERROR_CODE)
    