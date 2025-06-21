import streamlit as st
import pandas as pd

def main():
    st.title("我的第一個Streamlit App")
    st.write("歡迎來到我的應用程式！")
    
    df = pd.read_csv("taiwan.csv")
    st.write(df)

if __name__ == "__main__":
    main()