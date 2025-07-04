import yfinance as yf
from datetime import datetime
import os
import pandas as pd

def download_data():
    """
    1. 下載yfinance的4檔股票資料,股票有:2330.TW,2303.TW,2454.TW,2317.TW
    2. 在目前目錄下建立一個data的資料夾,如果已經有這個資料夾,就不建立
    3. 下載的4檔股票必需儲存為4個csv檔,檔名為2330.csv,2303.csv,2454.csv,2317.csv
    4. 如果已經有這些檔案,就不下載
    5. 由於每次執行時都有新的日期，檔案須每日更新，下載到最新日期檔案
    """
    # 股票代碼列表
    stocks = ['2330.TW', '2303.TW', '2454.TW', '2317.TW']
    # 資料夾名稱
    data_folder = 'data15_3'

    # 檢查並建立資料夾
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)

    # 迴圈下載每支股票的資料
    for stock_code in stocks:
        # 產生檔案名稱
        file_name = os.path.join(data_folder, f"{stock_code.split('.')[0]}.csv")

        # 檢查檔案是否存在，如果不存在則下載
        if not os.path.exists(file_name):
            print(f"Downloading {stock_code}...")
            data = yf.download(stock_code, start='2024-01-01', end=datetime.now().strftime('%Y-%m-%d'), auto_adjust=True)
            data.to_csv(file_name)
            print(f"Downloaded {stock_code} to {file_name}")
        else:
            print(f"檔案 {file_name} 已存在，檢查更新...")
            
            # 讀取現有資料的最後日期
            existing_df = pd.read_csv(file_name, index_col='Date', parse_dates=True)
            last_date = existing_df.index[-1]
            
            # 設定更新的開始日期為現有資料的隔天
            start_date = last_date + pd.Timedelta(days=1)
            end_date = datetime.now()

            # 如果開始更新的日期已經是今天或未來，代表資料已是最新
            if start_date.date() >= end_date.date():
                print(f"{stock_code} 資料已是最新。")
                continue

            # 下載從 start_date 到今天的新資料
            print(f"正在下載 {stock_code} 從 {start_date.strftime('%Y-%m-%d')} 的新資料...")
            new_data = yf.download(stock_code, start=start_date, end=end_date, auto_adjust=True)

            if not new_data.empty:
                # 如果有新資料，附加到舊檔案後面 (mode='a' for append, header=False)
                new_data.to_csv(file_name, mode='a', header=False)
                print(f"已更新 {stock_code} 至 {file_name}")
            else:
                # 如果沒有新資料 (例如假日或尚未開盤)
                print(f"{stock_code} 沒有可更新的資料。")

def main():
    download_data()

if __name__ == '__main__':
    main()