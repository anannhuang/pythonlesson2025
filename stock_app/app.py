import pandas as pd
import yfinance as yf
import os
from datetime import datetime
import streamlit as st
import matplotlib.pyplot as plt

# --- Constants ---
# Define constants to avoid repetition and make code easier to maintain.
STOCK_SYMBOLS = ['2330', '2303', '2454', '2317']
STOCK_NAMES = ['台積電', '聯電', '聯發科', '鴻海'] # Use names for clearer column headers
DATA_DIR = 'data'

def download_data():
    """
    1.下載從2024-01-01~當天的yfinance股價數據資料：2330 台積電、2303 聯電、2454 聯發科、2317 鴻海
    2.在目前目錄下建立一個data的資料夾，如果已經有這個資料夾，就不建立
    3.下載的四檔股票必須儲存為4個csv檔，檔名為2330_{當天日期}.csv、2303_{當天日期}.csv
    、2454_{當天日期}.csv、2317_{當天日期}.csv
    4.檔案如果當天已經有下載，就不要再下載
    5.每次下載成功後，刪除舊日期的檔案，只保留最新的一份
    """
    os.makedirs(DATA_DIR, exist_ok=True)
    today = datetime.now().strftime('%Y-%m-%d')
    start_date = '2024-01-01'
    for symbol in STOCK_SYMBOLS:
        filename = f"{symbol}_{today}.csv"
        filepath = os.path.join(DATA_DIR, filename)
        if os.path.exists(filepath):
            print(f"檔案 {filename} 已存在，跳過下載。"); continue
        ticker = f"{symbol}.TW"
        print(f"正在下載 {ticker} 從 {start_date} 到今天的股價數據...")
        stock_data = yf.download(ticker, start=start_date, end=today, progress=False)
        if stock_data.empty:
            print(f"下載 {ticker} 失敗，找不到資料或股票代碼錯誤。")
            continue
        stock_data.to_csv(filepath)
        print(f"檔案 {filename} 下載完成。")
        for file in os.listdir(DATA_DIR):
            if file.startswith(f"{symbol}_") and file != filename:
                os.remove(os.path.join(DATA_DIR, file))
                print(f"舊檔案 {file} 已刪除。")

def get_close_price_df():
    """
    1. 取出各個股票的收盤價，並建立DataFrame as df，顯示每日收盤價(區間為2024-01-01~當日)，建立df['STOCK_NAMES']以及df.loc['DATE']
    2. 用pandas整合成一張表格
    """
    close_dict = {}
    today = datetime.now().strftime('%Y-%m-%d')
    for symbol, name in zip(STOCK_SYMBOLS, STOCK_NAMES):
        filename = f"{symbol}_{today}.csv"
        filepath = os.path.join(DATA_DIR, filename)
        if os.path.exists(filepath):
            df = pd.read_csv(filepath, index_col=0, parse_dates=True)
            # 股票名稱與代號放同一格
            col_name = f"{name}\n ({symbol})"
            close_series = df['Close']
            # 移除無效索引（如'Date'字串、空字串、Ticker等）
            close_series = close_series[~close_series.index.isin(['Date', '', None, 'Ticker', 'ticker'])]
            close_dict[col_name] = close_series
        else:
            print(f"找不到 {filename}")
    if not close_dict:
        print("沒有資料")
        return pd.DataFrame()
    df = pd.DataFrame(close_dict)
    df = df.apply(pd.to_numeric, errors='coerce')
    df = df.round(2)

    print(df)
    return df


def show_streamlit_table():
    """
    使用 Streamlit 顯示收盤價表格與可互動的折線圖（st.line_chart，圖上可直接縮放/平移）
    """
    # 標題與現在時間同列顯示
    today_str = datetime.now().strftime('%Y-%m-%d')
    st.markdown(f"""
    <div style='display: flex; align-items: center; justify-content: space-between;'>
        <span style='font-size: 30px; font-weight: bold; margin-bottom: 0;'>台股每日收盤價</span>
        <span style='color: #888; font-size:18px; margin-left: 20px;'>今天日期：{today_str}</span>
    </div>
    """, unsafe_allow_html=True)
    df = get_close_price_df()
    if df.empty:
        st.warning("沒有資料可顯示")
        return
    df = df.sort_index(ascending=False)
    if not pd.api.types.is_datetime64_any_dtype(df.index):
        df.index = pd.to_datetime(df.index)


    # 日期與股票篩選器並列顯示
    col1, col2 = st.columns([1, 1])
    with col1:
        date_min = df.index.min().date()
        date_max = df.index.max().date()
        date_range = st.date_input(
            "日期區間",
            value=(date_min, date_max),
            min_value=date_min,
            max_value=date_max,
            key='date_range',
            help='選擇要顯示的日期範圍'
        )
    with col2:
        stock_options = list(df.columns)
        selected_stocks = st.multiselect(
            "請選取要顯示的股票",
            options=stock_options,
            default=stock_options,
            key='stock_select',
            help='選擇要顯示的股票'
        )
    # 篩選資料
    if isinstance(date_range, tuple):
        start_date, end_date = date_range
    else:
        start_date = end_date = date_range
    mask = (df.index.date >= start_date) & (df.index.date <= end_date)
    df = df.loc[mask]
    if not selected_stocks:
        st.info("請至少選擇一檔股票")
        return
    df_filtered = df[selected_stocks]

    # 圖表顯示
    st.subheader("股價走勢折線圖")
    import altair as alt
    # Altair 資料轉換
    df_reset = df_filtered.reset_index().rename(columns={df.index.name or 'index': '日期'})
    df_melt = df_reset.melt(id_vars=['日期'], var_name='股票', value_name='收盤價')
    # Altair 互動游標與輔助線
    import altair as alt
    nearest = alt.selection(type='single', nearest=True, on='mouseover', fields=['日期'], empty='none')
    line = alt.Chart(df_melt).mark_line().encode(
        x=alt.X('日期:T', title='日期'),
        y=alt.Y('收盤價:Q', title='收盤價'),
        color=alt.Color('股票:N', title='股票')
    )
    selectors = alt.Chart(df_melt).mark_point(size=60, filled=True, opacity=0).encode(
        x='日期:T',
        y='收盤價:Q',
        color='股票:N',
        tooltip=['日期:T', '股票:N', '收盤價:Q']
    ).add_selection(nearest)
    # 垂直輔助線
    vline = alt.Chart(df_melt).mark_rule(color='gray', strokeDash=[4,4]).encode(
        x='日期:T'
    ).transform_filter(nearest)
    # 水平輔助線
    hline = alt.Chart(df_melt).mark_rule(color='gray', strokeDash=[4,4]).encode(
        y='收盤價:Q'
    ).transform_filter(nearest)
    chart = (line + selectors + vline + hline).interactive()
    st.altair_chart(chart, use_container_width=True)

    # 表格顯示（日期無時間）
    df_display = df_filtered.copy().round(2)
    df_display.index = df_display.index.strftime('%Y-%m-%d')
    st.dataframe(df_display, height=210)


if __name__ == "__main__":
    download_data()
    show_streamlit_table()