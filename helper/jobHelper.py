import data.fixture
import utility.returnJson as jsonHelper


class jobHelper():
    jobDetailsFile = data.fixture.jobSearchFile
    jobDetails = jsonHelper.returnJson.returnJsonResponse(jobDetailsFile)

    def returnJobDetails(self):
        return self.jobDetails

    def returnMatchDetails(self, userRequest):
        studentId = userRequest['studentId']
        experienceFilter = userRequest['filter']['experience'] if userRequest['filter'][
                                                                      'experience'] is not None else None
        typeFilter = userRequest['filter']['type'] if userRequest['filter']['type'] is not None else None
        skillFilter = userRequest['filter']['skill'] if userRequest['filter']['skill'] is not None else None
        companyNameFilter = userRequest['filter']['companyName'] if userRequest['filter'][
                                                                        'companyName'] is not None else None
        locationFilter = userRequest['filter']['location'] if userRequest['filter']['location'] is not None else None

        resultList = []
        for ele in self.jobDetails['jobsList']:
            if experienceFilter == ele['experience'] or typeFilter == ele['type'] or companyNameFilter == ele[
                'company'] or locationFilter == ele['location']:
                resultList.append(ele)
        return resultList
