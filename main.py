"""
    health_check.py
        Script to check a URL for a version number.
"""
import requests
import logging
from time import sleep
from datetime import datetime
from os import getenv
from http import HTTPStatus
from json import loads

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

url = None


def check_url(url: str, version: str = "1.0.5") -> None:
    """Check a url for a version string"""
    timestamp = datetime.utcnow().isoformat()
    response = requests.get(url)

    status_code = response.status_code
    content = response.content.decode('utf-8')
    logger.info(f"{timestamp}, URL: {url}, status_code: {status_code}, content: {content}")

    if response.status_code != HTTPStatus.OK:
        logger.error(f"Version did not match {version}")


if __name__ == '__main__':
    if url is None:
        url = input(F"Enter the URL to check: ")

    while True:
        check_url(url=url)
        sleep(5)
