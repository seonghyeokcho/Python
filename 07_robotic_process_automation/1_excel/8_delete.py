from openpyxl import load_workbook
wb = load_workbook("/Users/csh/jupytercreation/Python_Practice/RPA/basic/1_excel/sample.xlsx")
ws = wb.active

# ws.delete_rows(8)  # 8번째 줄에 있는 7번 학생 데이터 삭제
# ws.delete_rows(8, 3)  # 8번째 줄부터 총 3줄 삭제(7,8,9번 학생 데이터 삭제)
# wb.save("/Users/csh/jupytercreation/Python_Practice/RPA/basic/1_excel/sample_delete_rows.xlsx")

# ws.delete_cols(2)  # 2번째 열(영어 열) 삭제
ws.delete_cols(2, 2)  # 2번째 열로부터 총 2개 열 삭제(영어, 수학 열 삭제)

wb.save("/Users/csh/jupytercreation/Python_Practice/RPA/basic/1_excel/sample_delete_cols.xlsx")