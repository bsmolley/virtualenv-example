#!/usr/bin/env python

# virtualenv <NameOfEnv>
# cd <NameOfEnv>

import requests

print requests.__version__

response = requests.get("http://google.ca")
print response.status_code

print response.text
