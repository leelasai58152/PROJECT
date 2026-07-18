from openpyxl import load_workbook





def open_excel(file , sheet):
    workbook = load_workbook(file)
    wc= workbook[sheet]
    data = []
    for row in wc.item_rows(min_row=2, value_only = True):
        data.append(row)
        return data