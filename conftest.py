from pytest import fixture
from requests import Session

from selenium import webdriver


@fixture
def logged_in_session():
    session = Session()

    # Perform the first GET to retrieve a cookie (LSESSION)
    get_resp = session.get(url="http://127.0.0.1:5000/login")

    # Login using a POST
    login_info = {
        "email": "brandon@techstep.com",
        "password": "1234"
    }

    post_resp = session.post(url="http://127.0.0.1:5000/login", data=login_info)

    if 'Search By Author' not in post_resp.text:
        raise Exception("Did not log in successfully")

    return session

@fixture
def browser():
    chrome = webdriver.Chrome()
    yield chrome
    chrome.quit()