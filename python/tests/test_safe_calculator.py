from unittest.mock import Mock

from safe_calculator import SafeCalculator


def authorizer():
    authorizer_mock = Mock()
    authorizer_mock.authorize.return_value = True
    return authorizer_mock

def test_divide_should_not_raise_any_error_when_authorized(authorizer_mock):
    # TODO: write a test that fails due to the bug in
    # SafeCalculator.add
    calc: SafeCalculator = SafeCalculator(authorizer_mock)
    calc.add(1, 1)  # Should raise an exception because Authorize returns False
