from requests import Session
import time

from pytest import mark

def test_can_login(logged_in_session):
    resp = logged_in_session.get(
        url="http://127.0.0.1:5000/search"
    )
    assert 'Search By ISBN-10' in resp.text

@mark.without_browser
def test_can_login_without_browser(logged_in_session, browser):
    # Retrieve LSESSION and token from session cookies
    lsession = logged_in_session.cookies.get('LSESSION')
    token = logged_in_session.cookies.get('token')

    # WARNING: You must navigate to the landing page FIRST
    # or injecting cookies will fail
    browser.get('http://127.0.0.1:5000')

    # Inject cookies into browser
    browser.add_cookie(
        {
            'name': 'LSESSION',
            'value': lsession
        }
    )

    browser.add_cookie(
        {
            'name': 'token',
            'value': token
        }
    )

    browser.get('http://127.0.0.1:5000/search')
    
    assert 'Search By ISBN-10' in browser.page_source

@mark.with_browser
def test_can_login_using_browser(browser):
    browser.get('http://127.0.0.1:5000')
    email_ipt = browser.find_element_by_css_selector('input#email')
    pw_ipt = browser.find_element_by_css_selector('input#password')
    submit_btn = browser.find_element_by_css_selector('button[value="Submit"]')

    email_ipt.send_keys('brandon@techstep.com')
    time.sleep(2)

    pw_ipt.send_keys('1234')
    time.sleep(2)
    submit_btn.click()
    time.sleep(2)
    assert 'Search By ISBN-10' in browser.page_source