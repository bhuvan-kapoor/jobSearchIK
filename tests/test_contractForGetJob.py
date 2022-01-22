import data.fixture
import utility.returnJson as jsonHelper
import json
from helper import getJobForUserHelper as getJobForUserHelper
from jsonschema import validate

getJobForUserHelper = getJobForUserHelper.getJobForUserHelper()


def test_getJobContract():
    studentDetail = data.fixture.multipleStudentDetailsFile
    multipleStudentDetailJson = jsonHelper.returnJson.returnJsonResponse(studentDetail)
    for ele in multipleStudentDetailJson:
        getJobResponse = getJobForUserHelper.fetchCustomRequest(ele)
        contentResponse = json.loads(getJobResponse.content)
        assert getJobResponse.status_code == 200
        try:
            validate(instance=contentResponse, schema=jsonHelper.returnJson.returnJsonResponse(data.fixture.jobContract))
        except AssertionError as e:
            print("No result returned %s" %e)
