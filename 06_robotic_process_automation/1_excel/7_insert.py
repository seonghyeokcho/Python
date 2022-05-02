from openpyxl import load_workbook
wb = load_workbook("/Users/csh/jupytercreation/Python_Practice/RPA/basic/1_excel/sample.xlsx")
ws = wb.active

# ws.insert_rows(8)  # 8번째 줄에 빈 row 가 생성됨
# ws.insert_rows(8, 5)  # 8번째 줄 위치에 5개의 row 가 생성됨

ws.insert_cols(2, 3)  # B열에 빈 column 이 생성됨

# wb.save("/Users/csh/jupytercreation/Python_Practice/RPA/basic/1_excel/sample_insert_rows.xlsx")
wb.save("/Users/csh/jupytercreation/Python_Practice/RPA/basic/1_excel/sample_insert_cols.xlsx")