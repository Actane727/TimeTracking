#!/bin/python3

from openpyxl import*

filepath = "/home/pi/Desktop/TrainingTime.xlsx"

wb = Workbook(filepath, read_only=False)
wb.save(filepath)

exit(0)
