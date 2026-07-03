import pandas as pd
import streamlit as st

# ==========================
# PAGE CONFIGURATION
# ==========================
st.set_page_config(
    page_title="Superstore Sales Dashboard",
    layout="wide"
)

# ==========================
# LOAD DATASET
# ==========================
df = pd.read_excel("Superstore.xlsx")

# ==========================
# SIDEBAR FILTERS
# ==========================
st.sidebar.header("🔍 Dashboard Filters")

# Region Filter
region = st.sidebar.multiselect(
    "Select Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

# Category Filter
category = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

# Segment Filter
segment = st.sidebar.multiselect(
    "Select Segment",
    options=sorted(df["Segment"].unique()),
    default=sorted(df["Segment"].unique())
)

# State Filter
state = st.sidebar.multiselect(
    "Select State",
    options=sorted(df["State"].unique()),
    default=sorted(df["State"].unique())
)

# Ship Mode Filter
ship_mode = st.sidebar.multiselect(
    "Select Ship Mode",
    options=sorted(df["Ship Mode"].unique()),
    default=sorted(df["Ship Mode"].unique())
)

# Year Filter
year = st.sidebar.multiselect(
    "Select Year",
    options=sorted(df["Order Date"].dt.year.unique()),
    default=sorted(df["Order Date"].dt.year.unique())
)

# ==========================
# APPLY FILTERS
# ==========================
df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category)) &
    (df["Segment"].isin(segment)) &
    (df["State"].isin(state)) &
    (df["Ship Mode"].isin(ship_mode)) &
    (df["Order Date"].dt.year.isin(year))
]

# ==========================
# DASHBOARD TITLE
# ==========================
st.title("📊 Superstore Sales Dashboard")

# ==========================
# KPI CARDS
# ==========================
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = len(df)
average_discount = df["Discount"].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Sales", f"${total_sales:,.2f}")

with col2:
    st.metric("Total Profit", f"${total_profit:,.2f}")

with col3:
    st.metric("Total Orders", total_orders)

with col4:
    st.metric("Average Discount", f"{average_discount*100:.2f}%")

# ==========================
# DASHBOARD SUMMARY
# ==========================
st.markdown("---")

st.subheader("📌 Dashboard Summary")

col1, col2, col3 = st.columns(3)

with col1:
    st.info(f"Filtered Records: {len(df)}")

with col2:
    st.success(f"Categories: {df['Category'].nunique()}")

with col3:
    st.warning(f"States: {df['State'].nunique()}")

# ==========================
# DATASET PREVIEW
# ==========================
st.subheader("Dataset Preview")
st.dataframe(df.head(5))


# ==========================
# CHARTS ANALYSIS
# ==========================

# Chart 1 & 2: Sales and Profit by Category
category_sales = (
    df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
)

category_profit = (
    df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Total Sales by Category")
    st.bar_chart(category_sales)

with col2:
    st.subheader("💰 Total Profit by Category")
    st.bar_chart(category_profit)


# Chart 3 & 4: Sales and Profit by Region
region_sales = (
    df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
)

region_profit = (
    df.groupby("Region")["Profit"].sum().sort_values(ascending=False)
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("🌍 Total Sales by Region")
    st.bar_chart(region_sales)

with col2:
    st.subheader("💵 Total Profit by Region")
    st.bar_chart(region_profit)


# Chart 5 & 6: Sales and Profit by Segment
segment_sales = (
    df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
)

segment_profit = (
    df.groupby("Segment")["Profit"].sum().sort_values(ascending=False)
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("🛒 Total Sales by Segment")
    st.bar_chart(segment_sales)

with col2:
    st.subheader("💰 Total Profit by Segment")
    st.bar_chart(segment_profit)


# Month Order
month_order = [
    "Jan","Feb","Mar","Apr","May","Jun",
    "Jul","Aug","Sep","Oct","Nov","Dec"
]


# Chart 7 & 8: Monthly Sales and Profit
monthly_sales = (
    df.groupby(df["Order Date"].dt.strftime("%b"))["Sales"]
    .sum()
    .reindex(month_order)
)

monthly_profit = (
    df.groupby(df["Order Date"].dt.strftime("%b"))["Profit"]
    .sum()
    .reindex(month_order)
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Monthly Sales Trend")
    st.line_chart(monthly_sales)

with col2:
    st.subheader("📉 Monthly Profit Trend")
    st.line_chart(monthly_profit)


# Chart 9 & 10: Quarterly Sales and Profit
quarterly_sales = (
    df.groupby(df["Order Date"].dt.quarter)["Sales"].sum()
)

quarterly_profit = (
    df.groupby(df["Order Date"].dt.quarter)["Profit"].sum()
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Total Sales by Quarter")
    st.bar_chart(quarterly_sales)

with col2:
    st.subheader("📉 Total Profit by Quarter")
    st.bar_chart(quarterly_profit)


# Chart 11 & 12: Yearly Sales and Profit
yearly_sales = (
    df.groupby(df["Order Date"].dt.year)["Sales"].sum()
)

yearly_profit = (
    df.groupby(df["Order Date"].dt.year)["Profit"].sum()
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Total Sales by Year")
    st.bar_chart(yearly_sales)

with col2:
    st.subheader("📉 Total Profit by Year")
    st.bar_chart(yearly_profit)

# ==========================
# TOP PRODUCTS
# ==========================

# Chart 13 & 14: Top 10 Products by Sales and Profit

top_product_sales = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_product_profit = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Top 10 Products by Sales")
    st.bar_chart(top_product_sales)

with col2:
    st.subheader("💰 Top 10 Products by Profit")
    st.bar_chart(top_product_profit)


# ==========================
# TOP STATES
# ==========================

# Chart 15 & 16: Top States by Sales and Profit

state_sales = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

state_profit = (
    df.groupby("State")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("🏙️ Top 10 States by Sales")
    st.bar_chart(state_sales)

with col2:
    st.subheader("🏙️ Top 10 States by Profit")
    st.bar_chart(state_profit)


# ==========================
# SUB-CATEGORY
# ==========================

# Chart 17 & 18: Sales and Profit by Sub-Category

subcategory_sales = (
    df.groupby("Sub-Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

subcategory_profit = (
    df.groupby("Sub-Category")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 Top 10 Sub-Categories by Sales")
    st.bar_chart(subcategory_sales)

with col2:
    st.subheader("💰 Top 10 Sub-Categories by Profit")
    st.bar_chart(subcategory_profit)


# ==========================
# DOWNLOAD FILTERED DATASET
# ==========================

st.markdown("---")

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Dataset",
    data=csv,
    file_name="filtered_superstore.csv",
    mime="text/csv"
)


# ==========================
# FOOTER
# ==========================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;">
        <h4>📊 Superstore Sales Dashboard</h4>
        <p>Developed by <b>Okpanachi Ogwu</b></p>
    </div>
    """,
    unsafe_allow_html=True
)
