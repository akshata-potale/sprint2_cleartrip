from Library.config import Config
import xlrd
path = Config.Data_Path

def read_locators():
    workbook = xlrd.open_workbook(path)
    worksheet = workbook.sheet_by_name("hotelpage")
    rows = worksheet.nrows
    print(rows)
    d={}
    for i in range(rows):
        row=worksheet.row_values(i)
        # print(row)
        d[row[0]]=(row[1],row[2])
    return d
print(read_locators())