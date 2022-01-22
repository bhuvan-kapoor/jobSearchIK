import json
from typing import overload

import data.fixture
import utility.genericRequestBuilder as genericRequestBuilder
import utility.returnJson as jsonHelper


class getJobForUserHelper():
    genericRequestBuilder = genericRequestBuilder.genericRequestBuilder()
    endpoint = "/returnJob"
    headers = {}

    def fetchRequest(self):
        studentDetail = data.fixture.studentDetailsFile
        studentDetailJson = jsonHelper.returnJson.returnJsonResponse(studentDetail)
        response = self.genericRequestBuilder.createGetRequest(self.endpoint, self.headers, json.dumps(studentDetailJson))
        print(response.status_code)
        print(json.loads(response.content))
        return response

    def fetchCustomRequest(self, param):
        response = self.genericRequestBuilder.createGetRequest(self.endpoint, self.headers, json.dumps(param))
        print(response.status_code)
        print(json.loads(response.content))
        return response
