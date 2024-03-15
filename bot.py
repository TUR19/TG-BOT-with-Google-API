from __future__ import print_function

import keyword
import os.path
import pickle
from google.protobuf import service
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import telebot
import mimetypes
import os
import pprint
import io
from datetime import datetime
from telebot.types import User, Chat

Askar_AGA = 2817
Tuka = 8888
Tuka2 = 50754
Dako = 5219
Sako = 938
Ali = 6798
Zake = 821
Aidana = 17327
mayBeBOT = 51479

ProjectManajer = Tuka
BrigadaTelegramID = [0, 0, 0, 0]

GroupForData = -7686

ExVar = 0
GeoLINK = ""
ValueMessageID = 0
ValueWord = ""

SAMPLE_RANGE_NAME = 'Test List!A2:E246'

class GoogleSheet:
    SPREADSHEET_ID = '1J2jWnVOdWXKPSJfjxK5UNNuAfwIzLkb40I_bUlE1c3A'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    service = None

    def __init__(self):
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                print('flow')
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)

    def updateRangeValues(self, range, values):
        data = [{
            'range': range,
            'values': values
        }]
        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': data
        }
        result = self.service.spreadsheets().values().batchUpdate(spreadsheetId=self.SPREADSHEET_ID,
                                                                  body=body).execute()
        print('{0} cells updated.'.format(result.get('totalUpdatedCells')))

    def getInfo(self, range):
        resVal = self.service.spreadsheets().values().get(spreadsheetId=self.SPREADSHEET_ID, range=range).execute()
        print(resVal.get('values'))
        arrResVal = resVal.get('values')
        print(type(arrResVal))

        exStrVal = ""
        for i in arrResVal:
            exStrVal += str(i)
        print(exStrVal)

        needIntVal = 0
        needIntVal = (needIntVal + int(exStrVal[2])) * 10
        needIntVal = (needIntVal + int(exStrVal[3])) * 10
        needIntVal = (needIntVal + int(exStrVal[4])) * 10
        needIntVal = (needIntVal + int(exStrVal[5])) * 10
        needIntVal = (needIntVal + int(exStrVal[6])) * 10
        needIntVal = (needIntVal + int(exStrVal[7])) * 10
        needIntVal = (needIntVal + int(exStrVal[8])) * 10
        needIntVal = (needIntVal + int(exStrVal[9])) * 10
        needIntVal = (needIntVal + int(exStrVal[10]))


        print(needIntVal)
        return needIntVal

    def getWord(self, range):
        exampleWord = self.service.spreadsheets().values().get(spreadsheetId=self.SPREADSHEET_ID, range=range).execute()
        listExWord = str(exampleWord.get('values'))

        # needWord = exampleWord.get('values')
        # for i in needWord:
        #     word += str(i)
        word = ""
        for i in listExWord:
            j = ord(i)
            if j != 91 and j != 93 and j != 34 and j != 47 and j != 39:
                word += i

        return word

    def getNumber(self, range):
        exampleNumber = self.service.spreadsheets().values().get(spreadsheetId=self.SPREADSHEET_ID, range=range).execute()
        listExNumber = str(exampleNumber.get('values'))
        number = 0

        for i in listExNumber:
            j = ord(i)
            if j > 47 and j < 58:
                number *= 10
                number += int(i)

        return number

    def getGeoData(self, range):
        exampleGeoData = self.service.spreadsheets().values().get(spreadsheetId=self.SPREADSHEET_ID, range=range).execute()
        listExGeoData = str(exampleGeoData.get('values'))
        strGeoData = [" ", " "]
        geoData = [1.1, 1.1]

        k = 0
        for i in listExGeoData:
            j = ord(i)
            if (j > 47 and j < 58) or j == 46:
                strGeoData[k] += i
            elif j == 44:
                k = 1

        geoData[0] = float(strGeoData[0])
        geoData[1] = float(strGeoData[1])

        # print(listExGeoData)
        # print(ord(','))
        # print(geoData)

        return geoData


def main():
    gs = GoogleSheet()
    #test_range = 'Бригада!G2:H4'
    #test_values = [
    #    ["Xmmm", 2],
    #    [34, "Hello"],
    #    ["WWS", 667]
    #]
    #gs.updateRangeValues(test_range, test_values)

    #ExampleVar = gs.getInfo('Бригада!K2')
    #global ExVar
    #ExVar = ExampleVar

    #global GeoLINK
    #GeoLINK = gs.getWord('Проект!C2')

    global BrigadaTelegramID
    BrigadaTelegramID[0] = gs.getNumber("Бригада!D2")
    BrigadaTelegramID[1] = gs.getNumber("Бригада!D3")
    BrigadaTelegramID[2] = gs.getNumber("Бригада!D4")
    BrigadaTelegramID[3] = gs.getNumber("Бригада!D5")

    # gs.getGeoData("Бригада!E2")

    # print(gs.getWord("Бригада!B1"))
    # print(ord('['))
    # print(ord(']'))
    # print(ord('"'))
    # print(ord('/'))
    # print(chr(39))

    print("Finish main")


if __name__ == '__main__':
    main()

bot = telebot.TeleBot('5147964:AAGcEGX023WznCFdPYaNfQMOTWa5')


clGoogle = GoogleSheet()
dataButton1 = "Бригада 1 кнопка нажата"
dataButton2 = "Бригада 2 кнопка нажата"
dataButton3 = "Бригада 3 кнопка нажата"
dataButton4 = "Бригада 4 кнопка нажата"

projectButton = ["Проект кнопка нажата",
                 "Проект кнопка нажата",
                 "Проект 2 кнопка нажата",
                 "Проект 3 кнопка нажата",
                 "Проект 4 кнопка нажата",
                 "Проект 5 кнопка нажата",
                 "Проект 6 кнопка нажата",
                 "Проект 7 кнопка нажата",
                 "Проект 8 кнопка нажата",
                 "Проект 9 кнопка нажата",
                 "Проект 10 кнопка нажата"]

rangeList = 'Проект!C4'

klava = telebot.types.ReplyKeyboardMarkup()

callback_button = telebot.types.KeyboardButton(text="Xmmm")
# callback_button = telebot.types.KeyboardButtonPollType(type="Xmmm")
klava.add(callback_button)

klavaStart = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

btn = telebot.types.KeyboardButton(text="Начать работу", request_location=True)
klavaStart.add(btn)

klavaFinish = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

btn = telebot.types.KeyboardButton(text="Завершить работу")
klavaFinish.add(btn)

brigada = telebot.types.InlineKeyboardMarkup()

callback_button = telebot.types.InlineKeyboardButton(text="Бригада 1", callback_data=dataButton1)
brigada.add(callback_button)
callback_button = telebot.types.InlineKeyboardButton(text="Бригада 2", callback_data=dataButton2)
brigada.add(callback_button)
callback_button = telebot.types.InlineKeyboardButton(text="Бригада 3", callback_data=dataButton3)
brigada.add(callback_button)
callback_button = telebot.types.InlineKeyboardButton(text="Бригада 4", callback_data=dataButton4)
brigada.add(callback_button)

project = telebot.types.InlineKeyboardMarkup()

callback_button = telebot.types.InlineKeyboardButton(text="Проект", callback_data=projectButton[1])
project.add(callback_button)
callback_button = telebot.types.InlineKeyboardButton(text="Геолокация", callback_data=projectButton[2])
project.add(callback_button)
callback_button = telebot.types.InlineKeyboardButton(text="Фотография", callback_data=projectButton[3])
project.add(callback_button)
callback_button = telebot.types.InlineKeyboardButton(text="Кнопка проверки", callback_data=projectButton[4])
project.add(callback_button)

answer_n1 = telebot.types.InlineKeyboardMarkup()
callback_button = telebot.types.InlineKeyboardButton(text="да", callback_data="yes_n1")
answer_n1.add(callback_button)
callback_button = telebot.types.InlineKeyboardButton(text="нет", callback_data="no_n1")
answer_n1.add(callback_button)

answer_n2 = telebot.types.InlineKeyboardMarkup()
callback_button = telebot.types.InlineKeyboardButton(text="да", callback_data="yes_n2")
answer_n2.add(callback_button)
callback_button = telebot.types.InlineKeyboardButton(text="нет", callback_data="no_n2")
answer_n2.add(callback_button)

answer_n3 = telebot.types.InlineKeyboardMarkup()

callback_button = telebot.types.InlineKeyboardButton(text="да", callback_data="yes_n3")
answer_n3.add(callback_button)
callback_button = telebot.types.InlineKeyboardButton(text="нет", callback_data="no_n3")
answer_n3.add(callback_button)

answer_n4 = telebot.types.InlineKeyboardMarkup()

callback_button = telebot.types.InlineKeyboardButton(text="да", callback_data="yes_n4")
answer_n4.add(callback_button)
callback_button = telebot.types.InlineKeyboardButton(text="нет", callback_data="no_n4")
answer_n4.add(callback_button)


@bot.message_handler(commands=['start']) #здесь начинается все. То есть старт процессов.
def start_message(message):
    print(message.from_user.id)
    #print(message.chat.id)
    #print(User.username)

    if message.from_user.id == ProjectManajer:
        #print(bot.get_me()) ----------------------------------------------------------------------------
        bot.send_message(message.from_user.id, "Hello Admin!", reply_markup=project)
    else:
        bot.send_message(message.from_user.id, "Hello!")

        first_name = message.from_user.first_name
        usernameinTG = message.from_user.username
        userID = str(message.from_user.id)

        bot.send_message(GroupForData, "Имя пользовотеля : " + first_name)
        bot.send_message(GroupForData, "В телеграмме для пойска : @" + usernameinTG)
        bot.send_message(GroupForData, "ID : " + userID)


@bot.message_handler(commands=['myid', 'getmyid'])
def get_my_id(message):
    bot.send_message(message.from_user.id, message.from_user.id)
    xmmm = bot.get_me()
    # print(xmmm)


@bot.message_handler(commands=['xmmm'])
def xmmm(message):
    bot.send_message(message.from_user.id, "Xmmm!")


@bot.message_handler(content_types=['text'])
def send_text(message, update):
    if message.text == "Да":
        bot.send_message(ProjectManajer, "Gotov!")

    global ValueMessageID
    ValueMessageID = message.message_id


@bot.message_handler(content_types=['location'])
def send_location(message):
    if message.location.longitude != 0:

        xstr = str(message.location.longitude)
        ystr = str(message.location.latitude)
        convertToString = ystr + " , " + xstr
        mapX = [[convertToString]]

        #messageFromUserID = message.from_user.id

        range = "Бригада!E2"

        if message.from_user.id == BrigadaTelegramID[0]:
            range = "Бригада!E2"
        elif message.from_user.id == BrigadaTelegramID[1]:
            range = "Бригада!E3"
        elif message.from_user.id == BrigadaTelegramID[2]:
            range = "Бригада!E4"
        elif message.from_user.id == BrigadaTelegramID[3]:
            range = "Бригада!E5"

        #charArip = 8
        #charSan = 9
        #valueA = ord(range[charArip])

        #k = 1
        #while k <= 4:
        #    if messageFromUserID ==

        #print(chr(valueA))

        clGoogle.updateRangeValues(range, mapX)


@bot.message_handler(content_types=['photo'])
def send_photo(message):
    photoID = message.photo[0].file_id
    # print(valueForPhoto)
    range = "Бригада!K3"

    if message.from_user.id == BrigadaTelegramID[0]:
        range = "Бригада!F2"
    elif message.from_user.id == BrigadaTelegramID[1]:
        range = "Бригада!F3"
    elif message.from_user.id == BrigadaTelegramID[2]:
        range = "Бригада!F4"
    elif message.from_user.id == BrigadaTelegramID[3]:
        range = "Бригада!F5"

    valueForBD = [[photoID]]

    clGoogle.updateRangeValues(range, valueForBD)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global ValueWord, ValueMessageID
    ValueMessageID = 0
    print(call.data)
    valRangeC = ["Бригада!C2", "Бригада!C3", "Бригада!C4", "Бригада!C5"]
    valRangeD = ["Бригада!D2", "Бригада!D3", "Бригада!D4", "Бригада!D5"]
    if call.data == dataButton1:
        # print(clGoogle.getNumber('Бригада!D2'))
        if clGoogle.getNumber(valRangeC[0]) == 1:
            bot.send_message(ProjectManajer, "Бригада 1 заняты. Выберите другую бригаду : ", reply_markup=brigada)
        else:
            bot.send_message(ProjectManajer, "Бригада 1 свободны. Проект отправлен бригаде. Ждите ответа.")

            # valueID1 = clGoogle.getNumber(valRangeD[0])

            # bot.send_message(valueID1, ValueWord)
            # bot.send_message(valueID1, "Вы готовы принять работу?", reply_markup=answer_n1)

            bot.send_message(BrigadaTelegramID[0], ValueWord)
            bot.send_message(BrigadaTelegramID[0], "Вы готовы принять работу?", reply_markup=answer_n1)

    elif call.data == dataButton2:
        if clGoogle.getNumber(valRangeC[1]) == 1:
            bot.send_message(ProjectManajer, "Бригада 2 заняты. Выберите другую бригаду : ", reply_markup=brigada)
        else:
            bot.send_message(ProjectManajer, "Бригада 2 свободны. Проект отправлен бригаде. Ждите ответа.")

            # valueID2 = clGoogle.getNumber(valRangeD[1])

            # bot.send_message(valueID2, ValueWord)
            # bot.send_message(valueID2, "Вы готовы принять работу?", reply_markup=answer_n2)

            bot.send_message(BrigadaTelegramID[1], ValueWord)
            bot.send_message(BrigadaTelegramID[1], "Вы готовы принять работу?", reply_markup=answer_n2)

    elif call.data == dataButton3:
        if clGoogle.getNumber(valRangeC[2]) == 1:
            bot.send_message(ProjectManajer, "Бригада 3 заняты. Выберите другую бригаду : ", reply_markup=brigada)
        else:
            bot.send_message(ProjectManajer, "Бригада 3 свободны. Проект отправлен бригаде. Ждите ответа.")

            # valueID3 = clGoogle.getNumber(valRangeD[2])

            # bot.send_message(valueID3, ValueWord)
            # bot.send_message(valueID3, "Вы готовы принять работу?", reply_markup=answer_n3)

            bot.send_message(BrigadaTelegramID[2], ValueWord)
            bot.send_message(BrigadaTelegramID[2], "Вы готовы принять работу?", reply_markup=answer_n3)

    elif call.data == dataButton4:
        if clGoogle.getNumber(valRangeC[3]) == 1:
            bot.send_message(ProjectManajer, "Бригада 4 заняты. Выберите другую бригаду : ", reply_markup=brigada)
        else:
            bot.send_message(ProjectManajer, "Бригада 4 свободны. Проект отправлен бригаде. Ждите ответа.")

            # valueID4 = clGoogle.getNumber(valRangeD[3])

            # bot.send_message(valueID4, ValueWord)
            # bot.send_message(valueID4, "Вы готовы принять работу?", reply_markup=answer_n4)

            bot.send_message(BrigadaTelegramID[3], ValueWord)
            bot.send_message(BrigadaTelegramID[3], "Вы готовы принять работу?", reply_markup=answer_n4)

    elif call.data == projectButton[1]:
        print(call.message.message_id)
        needWord = "Проект КОК!B2"
        needId = "Бригада!K2"

        ValueWord = clGoogle.getWord(needWord)
        valueNeedWord = "Проект : " + ValueWord + ". Какой строительной бригаде хотите отправить проект?"

        bot.send_message(clGoogle.getNumber(needId), valueNeedWord, reply_markup=brigada)
        #bot.send_message(clGoogle.getInfo('Бригада!K2'), call.message.message_id)

        # bot.send_location(ProjectManajer, 43.240281, 76.832014)

        # rangexmmm = "Бригада!K4:L5"
        # valuesxmmm = [
        #     [1],
        #     [7]
        # ]
        # clGoogle.updateRangeValues(rangexmmm, valuesxmmm)


        #global ValueMessageID

        #while ValueMessageID == 0:
        #    if ValueMessageID != 0:
        #        break

        #bot.forward_message(Tuka, Tuka2, message_id=ValueMessageID)

    elif call.data == projectButton[2]:
        # bot.send_message('Бригада!K2:K2', str('Проект!C3:C3'))
        # bot.send_message(ExVar, clGoogle.getWord('Проект!C2'))
        geoData = clGoogle.getGeoData("Бригада!E2")
        bot.send_location(ProjectManajer, geoData[0], geoData[1])
    elif call.data == projectButton[3]:
        # bot.send_message(Aidana, 'Проект!С4:С4')
        photoID = clGoogle.getWord("Бригада!K3")
        bot.send_photo(ProjectManajer, photoID)
    elif call.data == projectButton[4]:
        # bot.send_message(ExVar, GeoLINK)
        # xRange = 'Проект!C2'
        # xValue = "Xmmm"
        # clGoogle.updateRangeValues(xRange, xValue)
        # bot.forward_message(Ali, Tuka, message_id=359)
        bot.send_message(ProjectManajer, "Проверка", reply_to_message_id=ValueMessageID)
    elif call.data == projectButton[5]:
        bot.send_message('Бригада!K2:K2', str('Проект!C6:C6'))
    elif call.data == projectButton[6]:
        bot.send_message('Бригада!K2:K2', str('Проект!C7:C7'))
    elif call.data == projectButton[7]:
        bot.send_message('Бригада!K2:K2', str('Проект!C8:C8'))
    elif call.data == projectButton[8]:
        bot.send_message('Бригада!K2:K2', str('Проект!C9:C9'))
    elif call.data == projectButton[9]:
        bot.send_message('Бригада!K2:K2', str('Проект!C10:C10'))
    elif call.data == projectButton[10]:
        bot.send_message('Бригада!K2:K2', str('Проект!C11:C11'))

    elif call.data == "yes_n1":
        bot.send_message(ProjectManajer, "Строительная бригада принял работу.")
        bot.send_message(BrigadaTelegramID[0], "Отправляйтесь на местоположение работы. После приезда нажмите кнопку Начать работу.", reply_markup=klavaStart)
    elif call.data == "no_n1":
        bot.send_message(ProjectManajer, "Строительная бригада не принял работу.")
        bot.send_message(BrigadaTelegramID[0], "Оставьте комментарий.")

        while ValueMessageID == 0:
            if ValueMessageID != 0:
                break

        bot.forward_message(ProjectManajer, BrigadaTelegramID[0], message_id=ValueMessageID)

    elif call.data == "yes_n2":
        bot.send_message(ProjectManajer, "Строительная бригада принял работу.")
        bot.send_message(BrigadaTelegramID[1], "Отправляйтесь на местоположение работы. После приезда нажмите кнопку Начать работу.", reply_markup=klavaStart)
    elif call.data == "no_n2":
        bot.send_message(ProjectManajer, "Строительная бригада не принял работу.")
        bot.send_message(BrigadaTelegramID[1], "Оставьте комментарий.")

        while ValueMessageID == 0:
            if ValueMessageID != 0:
                break

        bot.forward_message(ProjectManajer, BrigadaTelegramID[1], message_id=ValueMessageID)

    elif call.data == "yes_n3":
        bot.send_message(ProjectManajer, "Строительная бригада принял работу.")
        bot.send_message(BrigadaTelegramID[2], "Отправляйтесь на местоположение работы. После приезда нажмите кнопку Начать работу.", reply_markup=klavaStart)
    elif call.data == "no_n3":
        bot.send_message(ProjectManajer, "Строительная бригада не принял работу.")
        bot.send_message(BrigadaTelegramID[2], "Оставьте комментарий.")

        while ValueMessageID == 0:
            if ValueMessageID != 0:
                break

        bot.forward_message(ProjectManajer, BrigadaTelegramID[2], message_id=ValueMessageID)

    elif call.data == "yes_n4":
        bot.send_message(ProjectManajer, "Строительная бригада принял работу.")
        bot.send_message(BrigadaTelegramID[3], "Отправляйтесь на местоположение работы. После приезда нажмите кнопку Начать работу.", reply_markup=klavaStart)
    elif call.data == "no_n4":
        bot.send_message(ProjectManajer, "Строительная бригада не принял работу.")
        bot.send_message(BrigadaTelegramID[3], "Оставьте комментарий.")

        while ValueMessageID == 0:
            if ValueMessageID != 0:
                break

        bot.forward_message(ProjectManajer, BrigadaTelegramID[3], message_id=ValueMessageID)

    elif call.data == "Xmmm":
        bot.get_me()


bot.polling()
# bot.polling(none_stop=True, interval=0)