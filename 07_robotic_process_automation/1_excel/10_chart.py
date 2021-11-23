from openpyxl import load_workbook
from openpyxl.chart import BarChart, Reference, LineChart
wb = load_workbook("/Users/csh/jupytercreation/Python_Practice/RPA/basic/1_excel/sample.xlsx")
ws = wb.active

# B2:C11 까지의 데이터를 차트로 생성
bar_value = Reference(ws, min_row=1, max_row=11, min_col=2, max_col=3)
bar_chart = BarChart()  # 차트 종류 설정 (Bar, Line, Pie, ..)
bar_chart.add_data(bar_value, titles_from_data=True)  # 차트에 사용할 데이터 추가
bar_chart.title = '성적표'
bar_chart.style = 5
bar_chart.y_axis.title = '점수'
bar_chart.x_axis.title = '번호'
ws.add_chart(bar_chart, 'E1')  # 차트 넣을 위치 정의

# B1:C11 까지의 데이터를 차트로 생성(제목 포함)
# line_value = Reference(ws, min_row=1, max_row=11, min_col=2, max_col=3)
# line_chart = LineChart()
# line_chart.add_data(line_value, titles_from_data=True)  # 차트의 계열1,계열2 부분이 영어, 수학으로 바뀜(제목에서 가져옴)
# line_chart.title = '성적표'  # 제목
# line_chart.style = 10  # 미리 정의된 스타일을 적용, 사용자가 개별 지정도 가능
# line_chart.y_axis.title = '점수'  # Y축의 제목
# line_chart.x_axis.title = '번호'  # X축의 제목
# ws.add_chart(line_chart, 'E1')

wb.save("/Users/csh/jupytercreation/Python_Practice/RPA/basic/1_excel/sample_chart.xlsx")