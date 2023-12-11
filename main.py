import pyautogui as p
from time import sleep

with open("countries.txt") as countries_file:
    countries = countries_file.readlines()
    PROMPT_BAR = p.Point(x=353, y=925)
    sleep(5)
    p.mouseDown(PROMPT_BAR)

for country in countries:
    p.write(country)