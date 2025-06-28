import yfinance as yf
from datetime import datetime
import pandas as pd
import os

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
    data_folder = 'data'

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
            print(f"{stock_code} already exists. Checking for updates...")
            # 如果檔案存在，則讀取現有資料並更新到最新日期
            existing_data = yf.download(stock_code, start='2024-01-01', end=datetime.now().strftime('%Y-%m-%d'), auto_adjust=True)
            existing_data.to_csv(file_name)
            print(f"Updated {stock_code} to {file_name}")
  

def create_close_price_dataframe():
    """
    讀取 data 資料夾中的股票 CSV 檔，整合成一個包含所有收盤價的 DataFrame。

    Returns:
        pandas.DataFrame: 整合後的 DataFrame，索引為日期，欄位為股票中文名稱。
                          如果找不到任何資料，則返回 None。
    """
    DATA_DIR = 'data'
    STOCK_MAPPING = {
        '2330': '台積電',
        '2303': '聯電',
        '2454': '聯發科',
        '2317': '鴻海'
    }

    if not os.path.isdir(DATA_DIR):
        print(f"錯誤：資料夾 '{DATA_DIR}' 不存在。請先執行 download_data()。")
        return None

    all_dataframes = []
    
    try:
        files_in_data = os.listdir(DATA_DIR)
    except FileNotFoundError:
        print(f"錯誤：資料夾 '{DATA_DIR}' 不存在。")
        return None

    for code, name in STOCK_MAPPING.items():
        # 修正：檔案名稱是 {code}.csv，不是 {code}_ 開頭。
        expected_filename = f"{code}.csv"
        stock_file = next((f for f in files_in_data if f == expected_filename), None)
        
        if stock_file:
            filepath = os.path.join(DATA_DIR, stock_file)
            try:
                # 修正：讀取時將第一欄作為 index，並解析為日期
                df = pd.read_csv(filepath, index_col=0, parse_dates=True)
                # 只保留 Close 欄位，並重新命名
                df = df[['Close']].rename(columns={'Close': name})
                all_dataframes.append(df)
            except Exception as e:
                print(f"處理檔案 {filepath} 時發生錯誤: {e}")
        else:
            print(f"警告：在 '{DATA_DIR}' 中找不到股票代碼 {code} 的資料檔。")

    if not all_dataframes:
        print("沒有成功讀取任何股票資料，無法建立 DataFrame。")
        return None

    # 合併所有 DataFrame
    final_df = pd.concat(all_dataframes, axis=1)
    final_df.sort_index(inplace=True)
    return final_df

def main():
    download_data()
    close_prices_df = create_close_price_dataframe()
    
    if close_prices_df is not None:
        print("\n==========================================")
        print("整合後的四支股票收盤價資料 (最新5筆):")
        print("==========================================")
        print(close_prices_df.tail())

if __name__ == '__main__':
    main()