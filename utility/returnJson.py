import json
import os
import sys

class returnJson():
    def __init__(self) -> None:
        super().__init__()

    def returnJsonResponse(userFilePath) -> object:
        userFile = open(os.path.dirname(os.path.dirname(__file__)) + userFilePath)
        return json.load(userFile)