import pandas as pd
import yfinance as yf
import os

def download_data():
    #上下3個雙引號寫function的說明
    """
    1.下載yfinance股價數據資料：2330 台積電、2303 聯電、2454 聯發科、2317 鴻海
    2.在目前目錄下建立一個data的資料夾，如果已經有這個資料夾，就不建立
    3.下載的四檔股票必須儲存為4個csv檔，檔名為2330_{當天日期}.csv、2303_{當天日期}.csv
    、2454_{當天日期}.csv、2317_{當天日期}.csv
    4.檔案如果當天已經有下載，就不要再下載
    5.每次下載成功後，刪除舊日期的檔案，只保留最新的一份
    """    