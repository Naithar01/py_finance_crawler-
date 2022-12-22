import pandas as pd
import seaborn as sns

url = "https://ko.wikipedia.org/wiki/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%9D%B8%EA%B5%AC"

tables = pd.read_html(url)

select_table = tables[4]

# 연도 (년)   추계인구(명)  출생자수(명)  사망자수(명)  자연증가수(명)  조출생률 (1000명당)  조사망률 (1000명당)  자연증가율 (1000명당)  합계출산율
slice_data = select_table[90:]

data_frame_slice_data = pd.DataFrame({
    "연도": slice_data["연도 (년)"].values,
    "출생자수": slice_data["출생자수(명)"].values,
    "사망자수": slice_data["사망자수(명)"].values,
})
# data_frame_slice_data["연도"].values

sns.lineplot(data=data_frame_slice_data, x="출생자수", y="연도", errorbar=None, label="출생자수", marker="o")
sns.lineplot(data=data_frame_slice_data, x="사망자수", y="연도", errorbar=None, label="사망자수", linestyle='--')

https://ko.wikipedia.org/wiki/%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%9D%B8%EA%B5%AC
