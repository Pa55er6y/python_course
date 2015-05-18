#!/usr/bin/python
# -*- coding: utf-8 -*-
#Created on May 17, 2015
#    A program which generates randomly a number of date and time values and displays them in Finnish language.
#@author: Likai

import random, time

MONTHS = {1:'tammikuu', 2:'helmikuu', 3:'maaliskuu', 4:'huhtikuu', 5:'toukokuu', 6:'kesäkuu', 7:'heinäkuu', 8:'elokuu', 9:'syyskuu', 10:'lokakuu', 11:'marraskuu', 12:'joulukuu'}
NUMBERS = ['nolla', 'yksi', 'kaksi', 'kolme', 'neljä', 'viisi', 'kuusi', 'seitsemän', 'kahdeksan', 'yhdeksän']
WEEKDAYS = ['maanantai', 'tiistai', 'keskiviikko', 'torstai', 'perjantai', 'lauantai', 'sunnuntai']
TITLE = ['', 'kymmentä ', 'sata ', 'tuhat ']
TITLES = ['', 'kymmentä ', 'sataa ', 'tuhatta ']
def numberInFinnish(num):
    length = len(str(num))
    if num < 10000:
        literality = ''
        i = 0
        while num > 0:
            digit = num % 10
            num /= 10
            if i == 1:
                if literality == '':
                    literality = 'kymmenen'
                else:
                    literality += '-toista'
            elif digit > 1:
                literality = NUMBERS[digit] + TITLES[i] + literality
            elif digit == 1:
                literality = NUMBERS[digit] + TITLE[i] + literality
            i += 1
        return literality
    else: return 'This number is not supported!'

def readDate(year, month, day, wday):
    print('Tänään on ' + WEEKDAYS[wday] + ', ' + numberInFinnish(day) + ' ' + MONTHS[month] + 'ta, ' + numberInFinnish(year) + ' vuotta.' + ' (' + str(day) + '/' + str(month) + '/' + str(year) + ')')

def readTime(hour, minute):
    time = 'Kello on '
    if minute == 0:
        time += numberInFinnish(hour)
    elif minute in range(1, 30):
        time += numberInFinnish(minute) + ' yli ' + numberInFinnish(hour)
    elif minute == 30:
        time += 'puoli' + numberInFinnish(hour)
    elif minute in range(31, 60):
        time += numberInFinnish(60 - minute) + ' vaille ' + numberInFinnish(hour)
    time += '.'
    if len(str(minute)) == 1:
        time += ' (' + str(hour) + '.' + '0' + str(minute) + ')'
    elif len(str(minute)) == 0:
        time += ' (' + str(hour) + '.00' + ')'
    else: time += ' (' + str(hour) + '.' + str(minute) + ')'
    print(time)
   
if __name__ == '__main__' :
    # Generate date:
    timestamp = random.randint(0, 32510000000)
    DateTime = time.localtime(timestamp)
    
    year = DateTime.tm_year
    month = DateTime.tm_mon
    day = DateTime.tm_mday
    wday = DateTime.tm_wday
    hour = DateTime.tm_hour
    minute = DateTime.tm_min

    readDate(year, month, day, wday)
    readTime(hour, minute)
    
