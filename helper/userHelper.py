import pytest

import data.fixture
import utility.returnJson as jsonHelper


class userHelper():
    studentDetailsFile = data.fixture.studentDetailsFile
    studentDetails = jsonHelper.returnJson.returnJsonResponse(studentDetailsFile)

    studentId = studentDetails['studentId']
    experienceFilter = studentDetails['filter']['experience']
    typeFilter = studentDetails['filter']['type']
    skillFilter = studentDetails['filter']['skill']
    companyNameFilter = studentDetails['filter']['companyName']
    locationFilter = studentDetails['filter']['location']

    def returnStudentId(self):
        return self.studentId

    def returnType(self):
        return self.typeFilter

    def returnCompanyName(self):
        return self.companyNameFilter

    def returnLocation(self):
        return self.locationFilter

    def returnExperience(self):
        return self.experienceFilter

    def returnSkill(self):
        return self.skillFilter
