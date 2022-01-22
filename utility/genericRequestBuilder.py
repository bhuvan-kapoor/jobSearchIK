import requests

import data.fixture

class genericRequestBuilder():

    def createGetRequest(self, endpoint, headers, body):
        return requests.get(data.fixture.baseUrl+endpoint, headers=headers, data=body)