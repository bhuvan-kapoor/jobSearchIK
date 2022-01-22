from flask import Flask
from flask import request
import json
import data.fixture
import utility.returnJson as jsonHelper

app = Flask(__name__)

jobSearchFile = data.fixture.jobSearchFile
jobSearchJson = jsonHelper.returnJson.returnJsonResponse(jobSearchFile)


@app.route('/returnJob/', methods=['POST', 'GET'])
def returnJob():
    jobFilter = json.loads(request.data)
    experienceFilter = jobFilter['filter']['experience'] if "experience" in jobFilter['filter'] else None
    typeFilter = jobFilter['filter']['type'] if "type" in jobFilter['filter'] else None
    skillFilter = jobFilter['filter']['skill'] if "skill" in jobFilter['filter'] else None
    companyNameFilter = jobFilter['filter']['companyName'] if "companyName" in jobFilter['filter'] else None
    locationFilter = jobFilter['filter']['location'] if "location" in jobFilter['filter'] else None
    resultList = []
    for ele in jobSearchJson['jobsList']:
        if experienceFilter == ele['experience'] or typeFilter == ele['type'] or companyNameFilter == ele[
            'company'] or locationFilter == ele['location']:
            resultList.append(ele)
    finalResponse = {}
    finalResponse["jobsList"] = resultList
    return finalResponse


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
