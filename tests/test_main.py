import requests
from unittest.mock import Mock, patch

from main import fetch_public_ip


def test_fetch_public_ip_success():
    mock_resp = Mock()
    mock_resp.raise_for_status = Mock()
    mock_resp.json.return_value = {"ip": "1.2.3.4"}
    with patch("main.requests.get", return_value=mock_resp):
        assert fetch_public_ip() == "1.2.3.4"


def test_fetch_public_ip_failure():
    with patch("main.requests.get", side_effect=requests.exceptions.RequestException):
        assert fetch_public_ip() is None

