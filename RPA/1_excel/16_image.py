from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

img = Image("/Users/csh/jupytercreation/Python_Practice/RPA/basic/1_excel/img/stinkbug.png")

# C3 위치에 stinkbug.png 파일의 이미지가 생성됨
ws.add_image(img, 'C3')
## ImportError : You must install Pillow to fetch image ...
## 위와 같은 오류 발생 시 pip install Pillow 를 설치해주면 됨

wb.save("/Users/csh/jupytercreation/Python_Practice/RPA/basic/1_excel/data/sample_image.xlsx")