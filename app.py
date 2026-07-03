
import pandas as pd
import streamlit as st

# Configure the page
st.set_page_config (
page_title = "Superstore Sales Dashboard", layout = "wide")

# Load the Dataset
df = pd.read_excel("Superstore.xlsx")

# Display the Dashboard Title
st.title("📊 Superstore Sales Dashboard")

#Calculate the KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = len(df)
average_discount = df["Discount"].mean()

# arrange the KPIs with st.columns()
col1, col2, col3, col4 = st.columns(4)

#Displaying a KPI
with col1:
    st.metric("Total Sales", f"${total_sales:,.2f}")

with col2:
    st.metric("Total Profit", f"${total_profit:,.2f}")

with col3:
    st.metric("Total Orders", f"{total_orders}")

with col4:
    st.metric("Average Discount", f"{average_discount *100:.2f}%")

# Display Dataset on the Dashboard
st.subheader("Dataset Preview")
st.dataframe(df.head(10))

#==============================
# DASHBOARD CHARTS ANALYSIS
#===============================
#Chart1: Sales by Category
category_sales = (
df.groupby("Category")["Sales"].sum()
.sort_values(ascending=False))

st.subheader("📊Sales by Category")
st.bar_chart(category_sales)

#Chart 2: Profit by Category
category_profit = (
df.groupby("Category")["Profit"].sum()
.sort_values(ascending =False))

st.subheader("💰Profit by Category")
st.bar_chart(category_profit)

#Chart 3: Sales by Region
region_sales =(
df.groupby("Region")["Sales"].sum()
.sort_values (ascending =False))

st.subheader("📊Sales by Region")
st.bar_chart(region_sales)

#Chart 4: Profit by Region
region_profit =(
df.groupby("Region")["Profit"].sum()
.sort_values(ascending =False))

st.subheader("💰Profit by Region")
st.bar_chart(region_profit)

#Chart 5: Sales by Segments
segment_sales = (
df.groupby("Segment")["Sales"].sum()
.sort_values(ascending =False))

st.subheader("👥Sales by Segments")
st.bar_chart(segment_sales)

#Chart 6: Profit by Segments
segment_profit =(
df.groupby("Segment")["Profit"].sum()
.sort_values(ascending=False))

st.subheader("💵Profit by Segments")
st.bar_chart(segment_profit)

#Chart 7:Monthly Sales Trend
monthly_sales =(
df.groupby(df["Order Date"].dt.month)["Sales"].sum())

st.subheader("📈Monthly Sales Trend")
st.line_chart(monthly_sales)

#Chart 8:Monthly Profit Trend
monthly_profit =(
df.groupby(df["Order Date"].dt.month)["Profit"].sum())

st.subheader("📉Monthly Profit Trend")
st.line_chart(monthly_profit)

#Chart 9:Sales by Quarter
quarterly_sales =(
df.groupby(df["Order Date"].dt.quarter)["Sales"].sum())

st.subheader("📈Quarterly Sales")
st.bar_chart(quarterly_sales)

#Chart 10: Profit by Quarter
quarterly_profit =(
df.groupby(df["Order Date"].dt.quarter)["Profit"].sum())

st.subheader("📉Quarterly Profit")
st.bar_chart(quarterly_profit)

#Chart 11:Sales by Year
yearly_sales = (
df.groupby(df["Order Date"].dt.year)["Sales"].sum())

st.subheader("📈Yearly Sales")
st.bar_chart(yearly_sales)

#Chart 12: Profit by Year
yearly_profit = (
df.groupby(df["Order Date"].dt.year)["Profit"].sum())

st.subheader("📉 Yearly Profit")
st.bar_chart(yearly_profit)


#Chart 13:Top 10 Products by Sales
top_product_sales =(
df.groupby("Product Name")["Sales"].sum()
.sort_values(ascending=False)
.head(10))

st.subheader("📊Top 10 Products by Sales")
st.bar_chart(top_product_sales)

#Chart 14: Top 10 Products by Profit
top_product_profit =(
df.groupby("Product Name")["Profit"].sum()
.sort_values(ascending =False)
.head(10))

st.subheader("💰Top 10 Products by Profit")
st.bar_chart(top_product_profit)

#Chart 15: Top 10 State by Sales
state_sales =(
df.groupby("State")["Sales"].sum()
.sort_values(ascending=False)
.head(10))

st.subheader("🏙️Top State by Sales")
st.bar_chart(state_sales)

#Chart 16: Top 10 State by Profit
state_profit =(
df.groupby("State")["Profit"].sum()
.sort_values(ascending=False)
.head(10))

st.subheader("🏙️Top State by Profit")
st.bar_chart(state_profit)

#Chart 17:Sales by Sub-Category
subcategory_sales =(
df.groupby("Sub-Category")["Sales"].sum()
.sort_values(ascending=False)
.head(10))

st.subheader("📊Sales by Sub-Category")
st.bar_chart(subcategory_sales)

#Chart 18: Profit by Sub-Category
subcategory_profit = (
df.groupby("Sub-Category")["Profit"].sum()
.sort_values(ascending=False)
.head(10))

st.subheader("💰 Profit by Sub-Category")
st.bar_chart(subcategory_profit)
