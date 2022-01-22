from helper import *
import helper.userHelper as userHelper

userObject = userHelper.userHelper()


def test_studentId():
    assert userObject.returnStudentId is not None


def test_experience():
    assert userObject.returnExperience() is not None


def test_location():
    assert userObject.returnLocation() is not None


def test_type():
    assert userObject.returnType() is not None


def test_skill():
    assert userObject.returnSkill() is not None


def test_name():
    assert userObject.returnCompanyName() is not None
