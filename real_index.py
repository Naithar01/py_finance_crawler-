import pandas as pd
import matplotlib.pyplot as plt

# 크롤링을 해와야 하는 웹사이트 url 
url = "https://finance.naver.com/marketindex/?tabSel=gold#tab_section"

# read_html 함수는 해당 페이지의 table 태그를 모두 긁어옴 
tables = pd.read_html(url, encoding='euc-kr') # UTF-8

select_table = tables[0]

print(select_table)

# 데이터들, 2차원 배열 
select_table_item_name = select_table[['상품명']].values
select_table_now_price = select_table[['현재가']].values
select_table_date = select_table[['기준일']].values

name_date_data = []
price_data = []

for i in range(3):
    name_date_data.append(select_table_item_name[i][0] + "\n" + select_table_date[i][0])
    price_data.append(select_table_now_price[i][0])


plt.rc('font', family="Malgun Gothic") # 한글 폰트 깨짐 오류 해결코드

x = name_date_data
y = price_data

plt.bar(x, y) 

plt.title("유가 시세 막대 그래프")
plt.xlabel("상품명 - 기준일")
plt.ylabel("단위: 원 / 리터")

plt.show()
