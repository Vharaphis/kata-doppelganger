from typing import Dict, List

import pytest
from unittest.mock import Mock

from discount_applier import DiscountApplier
from user import User


@pytest.fixture
def users() -> List[User]:
    users: List[User] = []
    NUMBER_OF_USERS = 5

    for i in range(NUMBER_OF_USERS):
        users.append(User(f"User{i}", f"user{i}@email.com"))
    return users


@pytest.fixture
def notifier():
    return Mock()


def test_apply_v1(users, notifier):
    # TODO: write a test that fails due to the bug in
    # DiscountApplier.apply_v1
    DISCOUNT_RATE = 0.3

    discount_applier = DiscountApplier(notifier)
    discount_applier.apply_v1(DISCOUNT_RATE, users)

    assert notifier.notify.call_count == len(users)  # Fails because 4 users notified instead of 5


def test_apply_v2(users, notifier):
    # TODO: write a test that fails due to the bug in
    # DiscountApplier.apply_v2
    DISCOUNT_RATE = 0.3
    sent_messages: Dict[str, str] = {}

    def notify(user: User, msg: str):
        sent_messages[user.email] = msg

    notifier.notify.side_effect = notify

    discount_applier = DiscountApplier(notifier)
    discount_applier.apply_v2(DISCOUNT_RATE, users)

    assert len(sent_messages) == len(users)  # Fails because 1 user notified instead of 5

