import streamlit as st
import pandas as pd
# 他の必要なライブラリをインポート

# DataFrameを作成するコード

# DataFrame 'df'作成

# Streamlitアプリの開始
def main():
    st.title('物件検索アプリ')

    # サイドバーに価格範囲スライダーを配置
    price_range = st.sidebar.slider(
        '価格範囲',
        min_value=0,
        max_value=100000,
        value=(100000, 200000)
    )

    # サイドバーに間取りの複数選択ボックスを配置
    layout_options = st.sidebar.multiselect(
        '間取りを選択',
        ['2K', '2DK', '2LDK', '3K', '3DK', '3LDK', '4K以上'],
        ['2K', '2DK', '2LDK']
    )

    # フィルタリングされたデータの表示
    #filtered_data = df[(df['家賃'] >= price_range[0]) & (df['家賃'] <= price_range[1]) & (df['間取り'].isin(layout_options))]
    #st.write(filtered_data)

# Streamlitアプリの実行
if __name__ == '__main__':
    main()