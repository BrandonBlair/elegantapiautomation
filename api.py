import time

import requests

start = time.time()
response = requests.get('http://google.com')
print(response.text[:200])
elapsed = time.time() - start
print(f"API validation took {elapsed} seconds")