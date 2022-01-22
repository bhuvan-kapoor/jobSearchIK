import data.fixture
import utility.returnJson as jsonHelper

studentDetailsFile = data.fixture.studentDetailsFile
jobSearchFile = data.fixture.jobSearchFile

studentDetailsJson = jsonHelper.returnJson.returnJsonResponse(studentDetailsFile)
jobSearchJson = jsonHelper.returnJson.returnJsonResponse(jobSearchFile)


def test_searchJob(studentDetails, jobSearch):
    experienceFilter = studentDetails['filter']['experience']
    typeFilter = studentDetails['filter']['type']
    skillFilter = studentDetails['filter']['skill']
    companyNameFilter = studentDetails['filter']['companyName']
    locationFilter = studentDetails['filter']['location']

    resultList = []
    for ele in jobSearch['jobsList']:
        if experienceFilter == ele['experience'] or typeFilter == ele['type'] or companyNameFilter == ele[
            'company'] or locationFilter == ele['location']:
            resultList.append(ele)
            #print(ele)
            assert experienceFilter == ele['experience']
    print(resultList)

test_searchJob(studentDetailsJson, jobSearchJson)
