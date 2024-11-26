from dataclasses import dataclass

import pytest

from mail_sender import SendMailRequest, MailSender, SendMailResponse
from user import User


@dataclass
class SendFullMailResponse:
    code: int
    message: str
    request: SendMailRequest


class HttpClient:
    def __init__(self):
        self._request = None

    def post(self, url: str, request: SendMailRequest) -> SendFullMailResponse:
        return SendFullMailResponse(503, request.recipient, request)


@pytest.fixture
def http_client() -> HttpClient:
    return HttpClient()


@pytest.fixture
def user() -> User:
    return User("User", "user@email.fr")


def test_send_v1(http_client: HttpClient, user: User):
    # TODO: write a test that fails due to the bug in MailSender.send_v1
    mail_sender: MailSender = MailSender(http_client)

    res = mail_sender.send_v1(user, "Message")

    assert res.request.recipient == user.email
    assert res.request.subject == "New notification"


def test_send_v2(http_client: HttpClient, user: User):
    # TODO: write a test that fails due to the bug in MailSender.send_v2
    mail_sender: MailSender = MailSender(http_client)

    res = mail_sender.send_v2(user, "Message")
