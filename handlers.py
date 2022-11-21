import dataRequests as request
import keyboard as markup
from aiogram import types, Dispatcher
from createBot import bot, dp
from datetime import datetime as dt

#параметри для запитів
params = request.GetTemplateParametrs()

#Функція яка починає весь цикл фільтрів
async def start_command(message: types.Message):
    params["aFacultyID"] = None
    params["aEducationForm"] = None
    params["aCourse"] = None
    params["aStudyGroupID"] = None
    params["aEndDate"] = None
    params["aStartDate"] = dt.today().strftime("%d.%m.%Y")
    await bot.send_message(message.chat.id, f'Виберіть факультет', reply_markup=markup.faculty_keyboards(params))

#Функція яка перевіряє введене повідомлення користувачем
async def user_message(message: types.Message):
    if (params["aFacultyID"] == None):
        if (message.text in [value["Value"] for value in request.GetFaculties(params)]):
            params["aFacultyID"] = request.GetKeyByValue(request.GetFaculties(params), message.text, "Value", "Key")
            await bot.send_message(message.chat.id, f"Виберіть форму навчання", reply_markup=markup.education_form_keyboards())
        else:
            await bot.send_message(message.chat.id, f"Такий факультет не існує")

    elif (params["aEducationForm"] == None):
        if (message.text in [value["Value"] for value in request.GetEducationForms()]):
            params["aEducationForm"] = request.GetKeyByValue(request.GetEducationForms(), message.text, "Value", "Key")
            await bot.send_message(message.chat.id, f"Виберіть курс", reply_markup=markup.cours_keyboards())
        else:
            await bot.send_message(message.chat.id, f"Такої форми навчання не існує")

    elif (params["aCourse"] == None):
        if (message.text in request.GetCourses()):
            params["aCourse"] = message.text
            await bot.send_message(message.chat.id, f"Виберіть групу", reply_markup=markup.group_keyboards(params))
        else:
            await bot.send_message(message.chat.id, f"Такий курс не існує")

    elif (params["aStudyGroupID"] == None):
        if (message.text in [value["Value"] for value in request.GetGroups(params)]):
            params["aStudyGroupID"] = request.GetKeyByValue(request.GetGroups(params), message.text, "Value", "Key")
            await bot.send_message(message.chat.id, f"Виберіть дату", reply_markup=markup.date_keyboards())
        else:
            await bot.send_message(message.chat.id, f"Така група не існує")

    elif (params["aEndDate"] == None):
        if (message.text in [value["Value"] for value in request.GetDate()]):
            params["aEndDate"] = request.GetKeyByValue(request.GetDate(), message.text, "Value", "Key")[0]["aEndDate"]
            params["aStartDate"] = request.GetKeyByValue(request.GetDate(), message.text, "Value", "Key")[0]["aStartDate"]
            schedule = request.GetSchedule(params)
            if(len(schedule) == 0):
                params["aEndDate"] = None
                params["aStartDate"] = dt.today().strftime("%d.%m.%Y")
                await bot.send_message(message.chat.id, f"Така дата не існує")
            else:
                scheduleHtml = ""
                scheduleDay = ""
                for subject in schedule:
                    if scheduleDay != subject["week_day"]:
                        scheduleDay = f"{subject['week_day']}"
                        scheduleHtml+= f"<b>{scheduleDay} ({subject['full_date']})</b>\n"
                    else:
                        scheduleHtml+= f"\t<u>{subject['study_time'].strip()}</u>:\n \t<i>{subject['discipline'].strip()}</i>\n \t<i>{subject['study_type'].strip()}</i>\n \t<i>{subject['cabinet'].strip()}</i>\n \t<i>{subject['study_time_begin'].strip()}-{subject['study_time_end'].strip()}</i>\n"
                await bot.send_message(message.chat.id, scheduleHtml, reply_markup=markup.delete_keyboard(), parse_mode="HTML")
        else:
            await bot.send_message(message.chat.id, f"Така дата не існує")

#Функція яка регеструє функції чату в бот
def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start', 'help'])
    dp.register_message_handler(user_message) 