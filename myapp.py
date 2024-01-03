import yfinance as yf
import streamlit as st
import plotly.express as px

# Set Streamlit App Title and Icon
st.set_page_config(
    page_title="Google Stock Price Analysis",
    page_icon=":chart_with_upwards_trend:"
)

# Customizing the Streamlit Theme
st.markdown(
    """
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .st-cm {
            color: #007bff;
        }
        .st-d6 {
            background-color: #007bff;
            color: #ffffff;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App Header
st.title("Google Stock Price Analysis")
st.write("""
Welcome to this colorful stock price app that displays the closing price and volume of Google's stock!
""")

# Get stock data
tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

# Date Range Selector with default values within the valid range
start_date = st.date_input("Select start date", min_value=tickerDf.index.min(), max_value=tickerDf.index.max(), value=tickerDf.index.min())
end_date = st.date_input("Select end date", min_value=start_date, max_value=tickerDf.index.max(), value=tickerDf.index.max())
tickerDf_filtered = tickerDf.loc[start_date:end_date]

# Closing Price Chart
fig_close = px.line(tickerDf_filtered, x=tickerDf_filtered.index, y='Close', title='Closing Price Over Time', labels={'Close': 'Closing Price'})
fig_close.update_traces(line_color='#17a2b8')
fig_close.update_layout(title_font_color='#343a40', paper_bgcolor='#ffffff', plot_bgcolor='#ffffff')
st.plotly_chart(fig_close)

# Volume Chart
fig_volume = px.line(tickerDf_filtered, x=tickerDf_filtered.index, y='Volume', title='Volume Over Time', labels={'Volume': 'Volume'})
fig_volume.update_traces(line_color='#28a745')
fig_volume.update_layout(title_font_color='#343a40', paper_bgcolor='#ffffff', plot_bgcolor='#ffffff')
st.plotly_chart(fig_volume)

# Summary Statistics
st.write("### Summary Statistics")
st.write(tickerDf_filtered.describe())

# Company Information
company_info = tickerData.info
st.write("### Company Information")
st.write(f"**Sector:** {company_info['sector']}")
st.write(f"**Industry:** {company_info['industry']}")
st.write(f"**Headquarters:** {company_info['city']}, {company_info['country']}")

# Footer
st.markdown("---")
st.write("Disclaimer: This app is for educational purposes only. Do your own research before making any investment decisions.")
