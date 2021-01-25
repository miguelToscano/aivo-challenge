import pandas as pd
import errors

def is_valid_value(value):

    return (type(value) is int or type(value) is float) and value >= 0

def validate_get_inequality(indicator, value, inequality = None):

    try:
        if is_valid_value(float(value)) == False:

            raise Exception('Invalid value', errors.BAD_REQUEST_CODE)
    except:
        raise Exception('Invalid value', errors.BAD_REQUEST_CODE)

    data = pd.read_csv('./data/indicators.csv', usecols = ['INDICATOR', 'Inequality'])

    if inequality != None and not inequality in data['Inequality'].unique().tolist() :
    
        raise Exception('Invalid inequality', errors.BAD_REQUEST_CODE)

    if not indicator in data['INDICATOR'].unique().tolist():

        raise Exception('Invalid indicator', errors.BAD_REQUEST_CODE)

    return


