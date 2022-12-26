# https://pypi.org/project/python-random-strings/
# https://coding-kindergarten.tistory.com/84

# pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz

from python_random_strings import random_strings
import time 

for i in range (10):
    a = random_strings.random_lowercase(6)
    print(a)

    time.sleep(1.5)

# -F, --onefile dist 폴더 안에 잡다한 폴더는 모두 지움 
# -n NAME, --name NAME 파일 이름
# -w, --windowed, --noconsole GUI 경우만 해당

# -i <FILE.ico or FILE.exe,ID or FILE.icns or “NONE”>, --icon <FILE.ico or FILE.exe,ID or FILE.icns or “NONE”> 아이콘 
# --add-data <SRC;DEST or SRC:DEST> 셀레늄 크롬 드라이버 생각하면 됨 