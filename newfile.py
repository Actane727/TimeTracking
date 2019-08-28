#!/bin/python3

from openpyxl import*

filepath = "/home/pi/Desktop/TrainingTime.xlsx"

wb = Workbook()
wb.save(filepath)

exit(0)
