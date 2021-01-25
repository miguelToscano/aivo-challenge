import pytest
import pandas as pd
from pytest_mock import mocker

from validators import indicators as indicatorsValidator

def test_is_valid_value_returns_true(mocker):

    response = indicatorsValidator.is_valid_value(1)

    assert response == True

def test_is_valid_value_returns_false(mocker):

    response = indicatorsValidator.is_valid_value('value')

    assert response == False

def test_validate_get_inequality_raises_exception_with_invalid_indicator(mocker):

    with pytest.raises(Exception) as error:
        indicatorsValidator.validate_get_inequality('njdskf', 1, 'Total')

def test_validate_get_inequality_raises_exception_with_invalid_value(mocker):

    with pytest.raises(Exception) as error:
        indicatorsValidator.validate_get_inequality('SW_LIFS', 'invalid_value', 'Total')

def test_validate_get_inequality_raises_exception_with_invalid_inqeuality(mocker):

    with pytest.raises(Exception) as error:
        indicatorsValidator.validate_get_inequality('SW_LIFS', 1, 'Totally wrong')

