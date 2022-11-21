import requests
from constants import HEADERS, REQUEST_PARAMS
from datetime import date, timedelta

#функція яка вертає шаблон параметрів для запитів
def GetTemplateParametrs():
    templateParams = {
        "aVuzID": REQUEST_PARAMS["aVuzID"],
        "aFacultyID": None,
        "aEducationForm": None,
        "aCourse": None,
        "aGiveStudyTimes": "false",
        "aStudyTypeID": "null",
        "aStudyGroupID": None,
        "aStartDate": date.today().strftime('%d.%m.%Y'),
        "aEndDate": None,
    }
    return templateParams

#функція яка витягує факультети з js функції на сайті
def GetFaculties(params):
    url = f"https://vnz.osvita.net/BetaSchedule.asmx/GetEmployeeFaculties?aVuzID={params['aVuzID']}"
    jsonRequest = requests.get(url=url, headers=HEADERS).json()
    return jsonRequest['d']
  
#функція яка витягує групи з js функції на сайті
def GetGroups(params):
    url = f"https://vnz.osvita.net/BetaSchedule.asmx/GetStudyGroups?aVuzID={params['aVuzID']}&aFacultyID=%22{params['aFacultyID']}%22&aEducationForm=%22{params['aEducationForm']}%22&aCourse=%22{params['aCourse']}%22&aGiveStudyTimes={params['aGiveStudyTimes']}"
    jsonRequest = requests.get(url=url, headers=HEADERS).json()
    return jsonRequest['d']['studyGroups']

#функція яка витягує розклад з js функції на сайті
def GetSchedule(params):
    url = f"https://vnz.osvita.net/BetaSchedule.asmx/GetScheduleDataX?aVuzID=%22{params['aVuzID']}%22&aStudyGroupID=%22{params['aStudyGroupID']}%22&aStartDate=%22{params['aStartDate']}%22&aEndDate=%22{params['aEndDate']}%22&aStudyTypeID={params['aStudyTypeID']}"
    jsonRequest = requests.get(url=url, headers=HEADERS).json()
    return jsonRequest['d']

#функція яка повертає курси
def GetCourses():
    courses = [
       "1", "2", "3", "4"
    ]
    return courses

#функція яка повертає форми навчання
def GetEducationForms():
    forms = [
        {"Key": "1", "Value": "Денна"},
        {"Key": "3", "Value": "Заочна"}
    ]
    return forms

#функція яка повертає дати вибору
def GetDate():
    dates = [
        {"Key": [{"aStartDate": f"{date.today().strftime('%d.%m.%Y')}", "aEndDate": f"{date.today().strftime('%d.%m.%Y')}"}], "Value": "Сьогодні"},
        {"Key": [{"aStartDate": f"{(date.today() + timedelta(days=1)).strftime('%d.%m.%Y')}", "aEndDate": f"{(date.today() + timedelta(days=1)).strftime('%d.%m.%Y')}"}], "Value": "Завтра"},
        {"Key": [{"aStartDate": f"{date.today().strftime('%d.%m.%Y')}", "aEndDate": f"{(date.today() + timedelta(days=7)).strftime('%d.%m.%Y')}"}], "Value": "7 днів вперед"},
        {"Key": [{"aStartDate": f"{(date.today() + timedelta(days=-1)).strftime('%d.%m.%Y')}", "aEndDate": f"{(date.today() + timedelta(days=-1)).strftime('%d.%m.%Y')}"}], "Value": "Вчора"},
        {"Key": [{"aStartDate": f"{(date.today() + timedelta(days=-7)).strftime('%d.%m.%Y')}", "aEndDate": f"{date.today().strftime('%d.%m.%Y')}"}], "Value": "7 днів назада"},
    ]
    return dates

#функція яка повертає ключ по значенню в заданому словнику
def GetKeyByValue(dict, value, valueParam=None, keyParam=None):
    if valueParam != None and keyParam != None:
        for item in dict:
            if item[valueParam] == value:
                return item[keyParam]
    return None
