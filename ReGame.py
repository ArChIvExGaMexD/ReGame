import keyboard
import serial
import time
import os
import telebot
import sys
token='no'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет')
@bot.message_handler(commands=['sleep'])
def sleep_message(message):
    bot.send_message(message.chat.id,'EXIT')
    sys.exit()
ser = serial.Serial('COM10', 9600)
ser.close()
ser.open()
def openGamesRU():
    print("Игры: Unturned, CS:GO, TITP, GM, ADOFI, osu!lazer или поддержка")
    game = input()
    if game == "Unturned":
        os.system('"D:/Steam/steamaaps/common/Unturned/Unturned_BE.exe"')
        bot.send_message(1872674461,'StartedGame')
    elif game == "CS:GO":
        os.system('"D:/Steam/steamapps/common/Counter-Strike Global Offensive/csgo.exe" -insecure')
        bot.send_message(1872674461,'StartedGame')
    elif game == "TITP":
        os.system('"D:/Steam/steamapps/common/This is Timmy Playtest/WindowsNoEditor/thisistimmy.exe"')
        bot.send_message(1872674461,'StartedGame')
    elif game == "GM":
        os.system('"D:/Games/Garrys Mod/hl2.exe"')
        bot.send_message(1872674461,'StartedGame')
    elif game == "ADOFI":
        os.system('"D:/qlatu/A Dance of Fire and Ice/ADOFAI 2.7/A Dance of Fire and Ice/A Dance of Fire and Ice.exe"')
        bot.send_message(1872674461,'StartedGame')
    elif game == "osu!lazer":
        os.system('"C:/Users/CyberSec/AppData/Local/osulazer/osu!.exe"')
        bot.send_message(1872674461,'StartedGame')
    elif game == "поддержка":
        print("Скоро буду")
        bot.send_message(1872674461,'Help1')
    

def openGamesEN():
    print("Games: Unturned, CS:GO, TITP, GM, ADOFI, osu!lazer or support")
    game = input()
    if game == "Unturned":
        os.system('"D:/Steam/steamapps/common/Unturned/Unturned_BE.exe"')
        bot.send_message(1872674461,'StartedGame')
    elif game == "CS:GO":
        os.system('"D:/Steam/steamapps/common/Counter-Strike Global Offensive/csgo.exe" -insecure')
        bot.send_message(1872674461,'StartedGame')
    elif game == "TITP":
        os.system('"D:/Steam/steamapps/common/This is Timmy Playtest/WindowsNoEditor/thisistimmy.exe"')
        bot.send_message(1872674461,'StartedGame')
    elif game == "GM":
        os.system('"D:/Games/Garrys Mod/hl2.exe"')
        bot.send_message(1872674461,'StartedGame')
    elif game == "ADOFI":
        os.system('"D:/qlatu/A Dance of Fire and Ice/ADOFAI 2.7/A Dance of Fire and Ice/A Dance of Fire and Ice.exe"')
        bot.send_message(1872674461,'StartedGame')
    elif game == "osu!lazer":
        os.system('"C:/Users/CyberSec/AppData/Local/osulazer/osu!.exe"')
        bot.send_message(1872674461,'StartedGame')
    elif game == "help":
        print("help is comming")
        bot.send_message(1872674461,'Help2')

def openGamesPL():
    print("Gry: Unturned, CS:GO, TITP, GM, ADOFI, osu!lazer albo coś nie działa")
    game = input()
    if game == "Unturned":
        os.system('"D:/Steam/steamapps/common/Unturned/Unturned_BE.exe"')
        bot.send_message(1872674461,'StartedGame')
    elif game == "CS:GO":
        os.system('"D:/Steam/steamapps/common/Counter-Strike Global Offensive/csgo.exe" -insecure')
        bot.send_message(1872674461,'StartedGame')
    elif game == "TITP":
        os.system('"D:/Steam/steamapps/common/This is Timmy Playtest/WindowsNoEditor/thisistimmy.exe"')
        bot.send_message(1872674461,'StartedGame')
    elif game == "GM":
        os.system('"D:/Games/Garrys Mod/hl2.exe"')
        bot.send_message(1872674461,'StartedGame')
    elif game == "ADOFI":
        os.system('"D:/qlatu/A Dance of Fire and Ice/ADOFAI 2.7/A Dance of Fire and Ice/A Dance of Fire and Ice.exe"')
        bot.send_message(1872674461,'StartedGame')
    elif game == "osu!lazer":
        os.system('"C:/Users/CyberSec/AppData/Local/osulazer/osu!.exe"')
        bot.send_message(1872674461,'StartedGame')
    elif game == "coś nie działa":
        print("asystent jest już w drodze")
        bot.send_message(1872674461,'Help1')

while True:
    print('Ожидание Ключ-карты / Waiting for Master key / Oczekiwanie na kartę-klucz')
    bot.send_message(1872674461,'Ожидание Ключ-карты / Waiting for Master key')
    response = ser.readline()
    decoded_response = response.decode('utf-8')
    if decoded_response != 0:
        lang = input("Язык / Lang / Język:")
        if lang == "RU":
            openGamesRU()
        elif lang == "EN":
            openGamesEN()
        elif lang == "PL" or "Polski":
            openGamesPL()
