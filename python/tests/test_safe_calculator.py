from safe_calculator import SafeCalculator


def test_divide_should_not_raise_any_error_when_authorized():
    # TODO: write a test that fails due to the bug in
    # SafeCalculator.add
    authorizer: Authorizer = Authorizer()
    calc: SafeCalculator = SafeCalculator(authorizer)
    calc.add(1, 1)  # Should raise an exception because Authorize returns False


class Authorizer:
    def __init__(self):
        pass

    def authorize(self):
        return True
