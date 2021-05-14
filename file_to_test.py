import openpyxl
from openpyxl import load_workbook
from openpyxl.styles import colors
from openpyxl.styles import Font, Color
fontStyle = Font(name="Calibri", size=12, color=colors.BLACK)
amounts, indexValue, cell = [1, 2, 3, 4, 5], 0, "A2"
book = load_workbook("output.xlsx")
sheet = book.active
while indexValue != 5:
    sheet[cell] = amounts[indexValue]
    sheet[cell].font = fontStyle
    indexValue += 1
    cell = chr(ord(cell[0]) + 1) + str(cell[1])
    print ("Sheet updating complete.")
    book.save("output.xlsx")