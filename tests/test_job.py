import pytest

import data.fixture
import helper.jobHelper as jobhelper
import utility.returnJson as jsonHelper

jobObject = jobhelper.jobHelper()


def test_notNull():
    jobObject.returnJobDetails() is not None

def test_return():
    studentDetailsFile = data.fixture.studentDetailsFile
    studentDetails = jsonHelper.returnJson.returnJsonResponse(studentDetailsFile)
    matchDetails = jobObject.returnMatchDetails(studentDetails)
    assert matchDetails is not None

def test_job():
    studentDetailsFile = data.fixture.studentDetailsFile
    studentDetails = jsonHelper.returnJson.returnJsonResponse(studentDetailsFile)
    matchDetails = jobObject.returnMatchDetails(studentDetails)
    assert matchDetails is not None