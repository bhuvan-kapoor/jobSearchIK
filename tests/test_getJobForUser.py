import data.fixture
import utility.returnJson as jsonHelper
import json
from helper import getJobForUserHelper as getJobForUserHelper

getJobForUserHelper = getJobForUserHelper.getJobForUserHelper()


def test_fetchResponse():
    getJobResponse = getJobForUserHelper.fetchRequest()
    assert getJobResponse.status_code == 200

def test_customFetchResponse():
    studentParam = {
        "studentId": "1234",
        "filter": {
            "experience": "311-5",
            "type": "permanent",
            "skill": "java,mysql",
            "companyName": "ABC",
            "location": "any"
        }
    }
    getJobResponse = getJobForUserHelper.fetchCustomRequest(studentParam)
    assert getJobResponse.status_code == 200

def test_customFetchResponseFromFixture():
    studentDetail = data.fixture.multipleStudentDetailsFile
    multipleStudentDetailJson = jsonHelper.returnJson.returnJsonResponse(studentDetail)
    for ele in multipleStudentDetailJson:
        getJobResponse = getJobForUserHelper.fetchCustomRequest(ele)
        contentResponse = json.loads(getJobResponse.content)
        assert getJobResponse.status_code == 200
        try:
            assert len(contentResponse['jobsList']) >= 1
        except AssertionError as e:
            print("No result returned %s" %e)
