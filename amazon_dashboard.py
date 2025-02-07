import streamlit as st
import pandas as pd
import plotly.express as px

# Load CSV File (Use your correct file path)
file_path = "C:/Users/NISHANT/Downloads/Amazon_Sales_Analysis.csv"  
df = pd.read_csv(file_path)

# Convert 'Order Date' to datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Streamlit App Title
st.title("📊 Amazon Sales Analysis Dashboard")

# Sidebar Filters
st.sidebar.header("🔍 Filter Options")
category_filter = st.sidebar.multiselect("Select Category", df['Category'].unique(), default=df['Category'].unique())
region_filter = st.sidebar.multiselect("Select Region", df['Region'].unique(), default=df['Region'].unique())

# Apply Filters
df_filtered = df[(df['Category'].isin(category_filter)) & (df['Region'].isin(region_filter))]

# Display Key Metrics
col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Sales", f"${df_filtered['Sales'].sum():,.2f}")
col2.metric("📦 Total Orders", df_filtered.shape[0])
col3.metric("📊 Total Profit", f"${df_filtered['Profit'].sum():,.2f}")

# 📅 Sales Trend Over Time
st.subheader("📅 Sales Trend Over Time")
sales_trend = df_filtered.groupby('Order Date')['Sales'].sum().reset_index()
fig_trend = px.line(sales_trend, x='Order Date', y='Sales', title="Sales Over Time", markers=True)
st.plotly_chart(fig_trend)

# 📦 Category-wise Sales
st.subheader("📦 Sales by Category")
category_sales = df_filtered.groupby('Category')['Sales'].sum().reset_index()
fig_category = px.bar(category_sales, x='Category', y='Sales', text='Sales', title="Revenue by Category", color='Category')
st.plotly_chart(fig_category)

# 🌍 Region-wise Sales
st.subheader("🌍 Sales by Region")
region_sales = df_filtered.groupby('Region')['Sales'].sum().reset_index()
fig_region = px.pie(region_sales, names='Region', values='Sales', title="Revenue by Region")
st.plotly_chart(fig_region)

# 📊 Profitability by Customer Segment
st.subheader("👥 Profit by Customer Segment")
segment_profit = df_filtered.groupby('Customer Segment')['Profit'].sum().reset_index()
fig_segment = px.bar(segment_profit, x='Customer Segment', y='Profit', text='Profit', title="Profit by Customer Segment", color='Customer Segment')
st.plotly_chart(fig_segment)

st.write("📌 **Tip:** Use the sidebar to filter and analyze different categories and regions.")

