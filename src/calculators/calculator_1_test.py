from typing import Dict
from pytest import raises
from .calculator_1 import Calculator1

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body
    
def test_calculate():
    mock_request = MockRequest(body = {'number': 1})
    claculator_1 = Calculator1()

    response = claculator_1.calculate(mock_request)

    assert "data" in response
    assert "Calculator" in response["data"]
    assert "Result" in response["data"]

    assert response["data"]["Calculator"] == 1
    assert response["data"]["Result"] == 14.25

def test_calculate_with_invalid_body():
    mock_request = MockRequest(body = {'invalid_key': 1})
    claculator_1 = Calculator1()

    with raises(Exception) as excinfo:
        claculator_1.calculate(mock_request)

        assert str(excinfo.value) == "Body mal formado"