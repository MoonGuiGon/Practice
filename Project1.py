import FinanceDataReader as fdr
import pandas as pd

# 각 지수 Data 불러오기
kospi = fdr.DataReader('KS11')
kosdaq = fdr.DataReader('KQ11')
nasdaq = fdr.DataReader('IXIC')
sp500 = fdr.DataReader('US500')

# 전일 대비 등락율, 52주 최고, 최저치 구하기
for index in [kospi, kosdaq, nasdaq, sp500]:
    index['pct_change'] = index['Close'].pct_change() * 100
    index['52week_high'] = index['Close'].rolling(window=252).max()
    index['52week_low'] = index['Close'].rolling(window=252).min()

# 마지막 날짜 구하기
last_dates = [index.index[-1].strftime('%Y-%m-%d') for index in [kospi, kosdaq, nasdaq, sp500]]

# DataFrame 생성
index_data = {
    '날짜': last_dates,
    '종가': [index['Close'].iloc[-1] for index in [kospi, kosdaq, nasdaq, sp500]],
    '전일대비': [index['pct_change'].iloc[-1] for index in [kospi, kosdaq, nasdaq, sp500]],
    '52주 최고': [index['52week_high'].iloc[-1] for index in [kospi, kosdaq, nasdaq, sp500]],
    '52주 최저': [index['52week_low'].iloc[-1] for index in [kospi, kosdaq, nasdaq, sp500]]
}

# DataFrame 생성 및 출력
df = pd.DataFrame(index_data, index=['코스피', '코스닥', '나스닥', 'S&P500'])
df

#새로 추가