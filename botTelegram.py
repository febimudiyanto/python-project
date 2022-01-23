'''
Author : Febi Mudiyanto
Date : 23/01/2022

'''

import os
import telebot
from dotenv import load_dotenv

# load API_KEY from .env
# put your API_KEY in ".env" file
# API_KEY=<token>
load_dotenv()
API_KEY = os.getenv("API_KEY")

# make a connection to bot
bot = telebot.TeleBot(API_KEY)

# start and help command
@bot.message_handler(commands=['start','help'])
def help(message):
    msg = '''
Server Monitoring Bot
---------
1. Disk Usage → /disk
2. CPU and RAM Usage → /sysinfo
3. Uptime Server → /uptime
4. Server Description → /server

Help → /help

Regards,

Bots
---------
    '''
    bot.send_message(message.chat.id, msg)

# make command function to chat if command receive
@bot.message_handler(commands=['check'])
def check(message):
    bot.send_message(message.chat.id, "The server is alive")


# get system info

import psutil
import subprocess

# disk usage (/disk)
@bot.message_handler(commands=['disk'])
def disk(message):
    diskTotal = int(psutil.disk_usage('/').total/(1024*1024*1024))
    diskUsed = int(psutil.disk_usage('/').used/(1024*1024*1024))
    diskAvail = int(psutil.disk_usage('/').free/(1024*1024*1024))
    diskPercent = psutil.disk_usage('/').percent

    msg = '''
Disk Info
---------
Total = {} GB
Used = {} GB
Avail = {} GB
Usage = {} %\n'''.format(diskTotal,diskUsed,diskAvail,diskPercent)
    bot.send_message(message.chat.id,msg)


# cpu & ram (/sysinfo)
@bot.message_handler(commands=['sysinfo'])
def sysinfo(message):
    cpuUsage = psutil.cpu_percent(interval=1)
    ramTotal = int(psutil.virtual_memory().total/(1024*1024)) #GB
    ramUsage = int(psutil.virtual_memory().used/(1024*1024)) #GB
    ramFree = int(psutil.virtual_memory().free/(1024*1024)) #GB
    ramUsagePercent = psutil.virtual_memory().percent
    msg = '''
CPU & RAM Info
---------
CPU Usage = {} %

RAM
Total = {} MB
Usage = {} MB
Free  = {} MB
Used = {} %\n'''.format(cpuUsage,ramTotal,ramUsage,ramFree,ramUsagePercent)
    bot.send_message(message.chat.id,msg)

# uptime (/uptime)
@bot.message_handler(commands=['uptime'])
def uptime(message):
    upTime = subprocess.check_output(['uptime','-p']).decode('UTF-8')
    msg = upTime
    bot.send_message(message.chat.id,msg)


# server desc (/server)
@bot.message_handler(commands=['server'])
def server(message):
    uname = subprocess.check_output(['uname','-rsoi']).decode('UTF-8')
    host = subprocess.check_output(['hostname']).decode('UTF-8')
    ipAddr = subprocess.check_output(['hostname','-I']).decode('UTF-8')
    msg ='''
Server Desc
---------
OS = {}
Hostname = {} 
IP Addr = {}'''.format(uname,host,ipAddr)
    bot.send_message(message.chat.id,msg)


# listen to telegram commands
bot.polling()
