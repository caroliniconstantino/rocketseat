from typing import Dict
from src.drivers.numpy_handler import NumpyHandler
from .calculator_3 import Calculator3
from pytest import raises

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calcute():
    mock_request = MockRequest({'numbers': [1, 2, 3]})
    calculator_3 = Calculator3(NumpyHandler())

    with raises(Exception) as exc_info:
        calculator_3.calculate(mock_request)

    assert str(exc_info.value) == 'Invalid body: variance is less than multiplication'