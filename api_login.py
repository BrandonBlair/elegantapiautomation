from requests import Session

session = Session()

# Perform the first GET to retrieve a cookie (LSESSION)
get_resp = session.get(url="http://127.0.0.1:5000/login")

# Login using a POST
login_info = {
    "email": "brandon@techstep.com",
    "password": "1234"
}

post_resp = session.post(url="http://127.0.0.1:5000/login", data=login_info)

import pdb; pdb.set_trace()