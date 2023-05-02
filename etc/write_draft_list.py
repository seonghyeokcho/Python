import os
from datetime import datetime
import openpyxl

# 아래의 "" 안에 기안서목록 & 워드 파일이 있는 경로를 복붙하세요.
path = ""

files = [f for f in os.listdir(path) if f.endswith('.docx')]

for f in files:  # 불러온 모든 기안서 파일 이름을 출력
    print(f)

dates = []
names = []
for f in files:
    date_str, name = f.split("_")
    date = datetime.strptime(date_str, "%Y%m%d")
    dates.append(date.strftime("%Y-%m-%d"))  # 날짜 양식 변경
    names.append(name[:-5])  # 파일확장자 제거

# 불러온 엑셀 파일에 데이터 덮어씌우기
wb = openpyxl.load_workbook(path + "draft_list.xlsx", data_only=True)
sheet = wb.active

for row, (date, name) in enumerate(zip(dates, names), start=4):
    sheet[f'C{row}'] = date
    sheet[f'D{row}'] = name

wb.save(path + "draft_list.xlsx")