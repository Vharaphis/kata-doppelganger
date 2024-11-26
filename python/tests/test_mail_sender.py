from unittest.mock import Mock

import pytest

from mail_sender import SendMailRequest, MailSender, SendMailResponse
from user import User

@pytest.fixture
def http_client():
    return Mock()


@pytest.fixture
def user() -> User:
    return User("User", "user@email.fr")


def test_send_v1(http_client, user: User):
    # TODO: write a test that fails due to the bug in MailSender.send_v1
    BODY = "Message"

    mail_sender: MailSender = MailSender(http_client)
    mail_sender.send_v1(user, BODY)

    args = http_client.post.call_args.args

    request = args[1]
    assert request.recipient == user.email
    assert request.subject == "New notification"


def test_send_v2(http_client, user: User):
    # TODO: write a test that fails due to the bug in MailSender.send_v2
    BODY = "Message"

    http_client.post.return_value = SendMailResponse(503, BODY)

    mail_sender: MailSender = MailSender(http_client)
    mail_sender.send_v2(user, BODY)

    args = http_client.post.call_args.args

    request = args[1]
    assert type(request) is SendMailRequest
