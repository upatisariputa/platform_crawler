import xlrd

id_datas = {}

def get_id_from_xl():
    book = xlrd.open_workbook('afreeca.xlsx')
    sheet = book.sheet_by_name('afreeca')

    for r in range(0, sheet.nrows):
        af_num = round(sheet.cell(r, 0).value)
        af_name = sheet.cell(r, 1).value
        id_datas[af_num] = af_name

get_id_from_xl()
