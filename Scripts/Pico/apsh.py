# APSH

from machine import *
import time
import os

# Date
def date():
    print("Under Development")
    print("I need to get an RTC Module first")

def pwd():
    workdir = os.getcwd()
    print(workdir)

def uname():
    details = os.uname()
    print(details)

def ls():
    content = os.listdir()
    print(content)

def led():
    led = Pin(25, Pin.OUT)

    print("LED information")
    print("Pin and mode: ", led)
    print("LED Value: ", led.value())

# Processing
def process(user_input):
    try:
        if user_input == "help":
            print("""PSD apsh, version 1.0
exit
date
pwd
uname
ls
led
""")
        elif user_input == "exit":
            exit()
        elif user_input == "ls":
            ls()
        elif user_input == "uname":
            uname()
        elif user_input == "led":
            led()
        elif user_input == "pwd":
            pwd()
        elif user_input == "date":
            date()
        elif user_input == "":
            return
        else:
            print("Command invalid or not implemented yet.")

    except Exception as e:
        print(f"An error occurred: {e}")

while True:
    user_input = input(">> ").strip()
    process(user_input)

