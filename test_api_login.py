from requests import Session


def test_can_login(logged_in_session):
    resp = logged_in_session.get(
        url="http://127.0.0.1:5000/search"
    )
    assert 'Search By ISBN-10' in resp.text

def test_can_skip_login_using_browser(
    logged_in_session, browser):
    # Load cookies into browser session
    lsession = logged_in_session.cookies.get('LSESSION')
    token = logged_in_session.cookies.get('token')

    # Navigate to landing page (WARNING: You cannot add cookies until 
    # the path has been set this way! Don't skip this step!)
    browser.get(url="http://127.0.0.1:5000")

    # Add the necessary cookies to the browser instance
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

    # Attempt to navigate directly to the search page
    browser.get(url="http://127.0.0.1:5000/search")

    # Prove that we are logged in successfully
    assert 'Search By ISBN-10' in browser.page_source

    import pdb; pdb.set_trace()