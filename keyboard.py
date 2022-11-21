from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
import dataRequests as request

#функція яка вертає клавіатуру з назвами факультетів
def faculty_keyboards(params):
    buttons = [KeyboardButton(item["Value"]) for item in request.GetFaculties(params)]
    markup = ReplyKeyboardMarkup()
    side = 0
    for button in buttons:
        if (side == 0):
            markup.add(button)
            side = 1
        elif (side == 1):
            markup.insert(button)
            side = 0
    return markup

#функція яка вертає клавіатуру з назвами форм навчання
def education_form_keyboards():
    buttons = [KeyboardButton(item["Value"]) for item in request.GetEducationForms()]
    markup = ReplyKeyboardMarkup()
    side = 0
    for button in buttons:
        if (side == 0):
            markup.add(button)
            side = 1
        elif (side == 1):
            markup.insert(button)
            side = 0
    return markup

#функція яка вертає клавіатуру з назвами курсів
def cours_keyboards():
    buttons = [KeyboardButton(item) for item in request.GetCourses()]
    markup = ReplyKeyboardMarkup()
    side = 0
    for button in buttons:
        if (side == 0):
            markup.add(button)
            side = 1
        elif (side == 1):
            markup.insert(button)
            side = 0
    return markup

#функція яка вертає клавіатуру з назвами груп
def group_keyboards(params):
    buttons = [KeyboardButton(item["Value"]) for item in request.GetGroups(params)]
    markup = ReplyKeyboardMarkup()
    side = 0
    for button in buttons:
        if (side < 3):
            markup.insert(button)
            side+= 1
        elif (side == 3):
            markup.add(button)
            side = 1
    return markup

#функція яка вертає клавіатуру з назвами дат вибору
def date_keyboards():
    buttons = [KeyboardButton(item["Value"]) for item in request.GetDate()]
    markup = ReplyKeyboardMarkup()
    side = 0
    for button in buttons:
        if (side == 0):
            markup.add(button)
            side = 1
        elif (side == 1):
            markup.insert(button)
            side = 0
    return markup

#функція яка видаляє клавіатуру в користувача
def delete_keyboard():
    return ReplyKeyboardRemove()