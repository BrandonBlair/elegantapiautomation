from requests import Session

def test_can_login_using_api_request():
    session = Session()

    # Mimic navigating to the landing page
    landing_page_resp = session.get(url="http://127.0.0.1:5000/")

    # Login with a POST
    login_info = {
        "email": "brandon@techstepacademy.com",
        "password": "1234"
    }

    login_resp = session.post(url="http://127.0.0.1:5000/v1/login", data=login_info)
    
    print(login_resp.text)