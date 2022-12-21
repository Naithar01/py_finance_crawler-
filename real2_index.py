import pandas as pd
import matplotlib.pyplot as plt

url = "https://finance.naver.com/marketindex/exchangeDailyQuote.naver?marketindexCd=FX_USDKRW"

tables = pd.read_html(url, encoding='euc-kr') # UTF-8

select_table = tables[0]

trading_price = select_table[['매매기준율']].values
trading_price_date = select_table[['날짜']].values

trading_price_data = []
trading_price_date_data = []
for i in range(10):
    trading_price_data.append(trading_price[i][0])
    trading_price_date_data.append(trading_price_date[i][0])


print("revers 이전", trading_price_data)

trading_price_data.reverse()
trading_price_date_data.reverse()

print("revers 이후",trading_price_data)



plt.rc('font', size=6) # 폰트 사이즈 조절
plt.rc('font', family="Malgun Gothic") # 한글 폰트 깨짐 오류 해결코드


plt.plot(trading_price_date_data, trading_price_data) # plot 을 사용해서 기본 그래프 그리기

plt.title("달러 환율 그래프")
plt.xlabel("날짜")
plt.ylabel("단위: 원")

plt.show()