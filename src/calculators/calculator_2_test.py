from typing import Dict, List
from .calculator_2 import Calculator2
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler(DriverHandlerInterface):
    def standard_deviation(self, numbers: List[float]) -> float:
        return 3

def test_calculate_integration():
    mock_request = MockRequest({'numbers': [1, 2, 3]})
    driver_handler = MockDriverHandler()
    calculator_2 = Calculator2(driver_handler)
    formated_response = calculator_2.calculate(mock_request)
    print(formated_response)


    assert isinstance(formated_response, dict)
    assert formated_response == {'data': {'Calculator': 2, 'Result': 0.33}}
