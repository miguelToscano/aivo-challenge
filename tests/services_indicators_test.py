import pytest
import pandas as pd
from pytest_mock import mocker

from services import indicators as indicators_service

def test_get_indicators_returns_indicators_successfuly(mocker):

    data = {'col1': [1, 2, 4, 4], 'col2': [1, 2, 4, 4]}

    mockDataframe = pd.DataFrame(data)

    mocker.patch('pandas.read_csv', return_value = mockDataframe)

    response = indicators_service.get_indicators()

    assert len(response) == 3

def test_get_countries_returns_no_countries_succesfully(mocker):

    data = {'INDICATOR': ['A', 'A', 'C'],
            'Inequality': ['Total', 'Total', 'Total'],
            'Indicator': ['A', 'B', 'C'],
            'Value': [1, 2, 3], 
            'Country': ['Argentina', 'Brasil', 'Chile'],
            'Unit': ['Percentage','Percentage','Percentage']
            }

    mockDataframe = pd.DataFrame(data)

    mocker.patch('pandas.read_csv', return_value = mockDataframe)

    response = indicators_service.get_inequality('A', 2, 'Men')

    assert len(response['countries_inequalities']) == 0

def test_get_countries_returns_one_country_succesfully(mocker):

    data = {'INDICATOR': ['A', 'A', 'C'],
            'Inequality': ['Total', 'Total', 'Total'],
            'Indicator': ['A', 'B', 'C'],
            'Value': [1, 2, 3], 
            'Country': ['Argentina', 'Brasil', 'Chile'],
            'Unit': ['Percentage','Percentage','Percentage']
            }
    mockDataframe = pd.DataFrame(data)

    mocker.patch('pandas.read_csv', return_value = mockDataframe)

    response = indicators_service.get_inequality('A', 1, 'Total')

    assert len(response['countries_inequalities']) == 1

def test_get_countries_returns_two_countries_succesfully(mocker):

    data = {'INDICATOR': ['A', 'A', 'C'],
            'Inequality': ['Total', 'Total', 'Total'],
            'Indicator': ['A', 'B', 'C'],
            'Value': [1, 2, 3], 
            'Country': ['Argentina', 'Brasil', 'Chile'],
            'Unit': ['Percentage','Percentage','Percentage']
            }

    mockDataframe = pd.DataFrame(data)

    mocker.patch('pandas.read_csv', return_value = mockDataframe)

    response = indicators_service.get_inequality('A', 0, 'Total')

    assert len(response['countries_inequalities']) == 2