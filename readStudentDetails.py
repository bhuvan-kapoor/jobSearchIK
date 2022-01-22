import json
import requests

studentDetailsFile = open("studentDetails.json")
jobSearchFile = open("jobSearch.json")

studentDetailsJson = json.load(studentDetailsFile)
jobSearchJson = json.load(jobSearchFile)


# print(studentDetailsJson)
# print(jobSearchJson)

def searchJob(studentDetails, jobSearch):
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
    print(resultList)


searchJob(studentDetailsJson, jobSearchJson)
