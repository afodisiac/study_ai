# this is to test and know the zodiac signs....

input("Enter Your Name :) :  ")
print("....................................................")
print("WELCOME TO RAJ.ZODIAC SIGNS.. HOPE YOU ENJOY.")
print("....................................................")

day= int(input("Please Enter Your Birthday day only: "))
month= input("Please Enter Your Month: ")

if month == 'december':
    astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn' 
if month == 'january':
    astro_sign = 'Capricorn' if (day < 20) else 'Aquarias'
if month == 'february':
    astro_sign = 'Aquarias' if (day < 19) else 'Pisces'
if month == 'march':
    astro_sign = 'Pisces' if (day < 21) else 'Aries'
if month == 'april':
    astro_sign = 'Aries' if (day < 20) else 'Taurus'
if month == 'may':
    astro_sign = 'Taurus' if (day < 21) else 'Gemini'
if month == 'june':
    astro_sign = 'Gemini' if (day < 21) else 'Cancer'
if month == 'july':
    astro_sign = 'Cancer' if (day < 23) else 'Leo'
if month == 'august':
    astro_sign = 'Leo'   if (day < 23) else 'Virgo'
if month == 'september':
    astro_sign = 'Virgo' if (day < 23) else 'Libra'
if month == 'october':
    astro_sign = 'Libra' if (day < 23) else 'Scorpio'
if month == 'november':
    astro_sign = 'Scorpio' if (day< 22) else  'Sagittarius'

print("______________________________________________________")
print ("Your Zodiac Sign Is:  ", astro_sign)
print("______________________________________________________")

import sys,time,os
message= "THANK YOU FOR TRYING OUT"
def typewriter(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

typewriter(message)

