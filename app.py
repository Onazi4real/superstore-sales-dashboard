import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime

# ==========================
# PAGE CONFIGURATION
# ==========================
st.set_page_config(
    page_title="Okpanachi | Superstore Dashboard",
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

st.caption(f"Updated: {datetime.now().strftime('%d %B %Y')}")

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


st.markdown("### 📈 Business Insights")

col1, col2, col3 = st.columns(3)

best_region = df.groupby("Region")["Sales"].sum().idxmax()
best_category = df.groupby("Category")["Sales"].sum().idxmax()
best_product = df.groupby("Product Name")["Sales"].sum().idxmax()

with col1:
    st.success(f"🏆 Best Region\n\n{best_region}")

with col2:
    st.info(f"📦 Best Category\n\n{best_category}")

with col3:
    st.warning(f"⭐ Best Product\n\n{best_product}")

# ==========================
# DATASET PREVIEW
# ==========================
st.subheader("Dataset Preview")
st.dataframe(df)


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
    st.subheader("📊 Sales by Category")

    fig = px.bar(
        x=category_sales.index,
        y=category_sales.values,
        labels={"x": "Category", "y": "Sales"},
        color=category_sales.values,
        color_continuous_scale="Blues"
    )

    st.plotly_chart(fig, use_container_width=True)


with col2:
    st.subheader("💰 Profit by Category")

    fig = px.bar(
        x=category_profit.index,
        y=category_profit.values,
        labels={"x": "Category", "y": "Profit"},
        color=category_profit.values,
        color_continuous_scale="Greens"
    )

    st.plotly_chart(fig, use_container_width=True)


# Chart 3 & 4: Sales and Profit by Region
region_sales = (
    df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
)

region_profit = (
    df.groupby("Region")["Profit"].sum().sort_values(ascending=False)
)

col1, col2 = st.columns(2)

with col1:
    st.subheader("🌍 Sales by Region")

    fig = px.bar(
        x=region_sales.index,
        y=region_sales.values,
        labels={"x": "Region", "y": "Sales"},
        color=region_sales.values,
        color_continuous_scale="Blues"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("💵 Profit by Region")

    fig = px.bar(
        x=region_profit.index,
        y=region_profit.values,
        labels={"x": "Region", "y": "Profit"},
        color=region_profit.values,
        color_continuous_scale="Greens"
    )

    st.plotly_chart(fig, use_container_width=True)




# Chart 5 & 6: Sales and Profit by Segment
segment_sales = (
    df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
)

segment_profit = (
    df.groupby("Segment")["Profit"].sum().sort_values(ascending=False)
)

col1, col2 = st.columns(2)


with col1:
    st.subheader("🛒 Sales by Segment")

    fig = px.bar(
        x=segment_sales.index,
        y=segment_sales.values,
        labels={"x": "Segment", "y": "Sales"},
        color=segment_sales.values,
        color_continuous_scale="Blues"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("💰 Profit by Segment")

    fig = px.bar(
        x=segment_profit.index,
        y=segment_profit.values,
        labels={"x": "Segment", "y": "Profit"},
        color=segment_profit.values,
        color_continuous_scale="Greens"
    )

    st.plotly_chart(fig, use_container_width=True)


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

    fig = px.line(
        x=monthly_sales.index,
        y=monthly_sales.values,
        markers=True,
        labels={"x": "Month", "y": "Sales"}
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📉 Monthly Profit Trend")

    fig = px.line(
        x=monthly_profit.index,
        y=monthly_profit.values,
        markers=True,
        labels={"x": "Month", "y": "Profit"}
    )

    st.plotly_chart(fig, use_container_width=True)


# Chart 9 & 10: Quarterly Sales and Profit
quarterly_sales = (
    df.groupby(df["Order Date"].dt.quarter)["Sales"].sum()
)

quarterly_profit = (
    df.groupby(df["Order Date"].dt.quarter)["Profit"].sum()
)

col1, col2 = st.columns(2)


with col1:
    st.subheader("📈 Quarterly Sales")

    fig = px.bar(
        x=quarterly_sales.index.astype(str),
        y=quarterly_sales.values,
        labels={"x": "Quarter", "y": "Sales"},
        color=quarterly_sales.values,
        color_continuous_scale="Blues"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📉 Quarterly Profit")

    fig = px.bar(
        x=quarterly_profit.index.astype(str),
        y=quarterly_profit.values,
        labels={"x": "Quarter", "y": "Profit"},
        color=quarterly_profit.values,
        color_continuous_scale="Greens"
    )

    st.plotly_chart(fig, use_container_width=True)



# Chart 11 & 12: Yearly Sales and Profit
yearly_sales = (
    df.groupby(df["Order Date"].dt.year)["Sales"].sum()
)

yearly_profit = (
    df.groupby(df["Order Date"].dt.year)["Profit"].sum()
)

col1, col2 = st.columns(2)


with col1:
    st.subheader("📈 Yearly Sales")

    fig = px.bar(
        x=yearly_sales.index.astype(str),
        y=yearly_sales.values,
        labels={"x": "Year", "y": "Sales"},
        color=yearly_sales.values,
        color_continuous_scale="Blues"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("📉 Yearly Profit")

    fig = px.bar(
        x=yearly_profit.index.astype(str),
        y=yearly_profit.values,
        labels={"x": "Year", "y": "Profit"},
        color=yearly_profit.values,
        color_continuous_scale="Greens"
    )

    st.plotly_chart(fig, use_container_width=True)

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

    fig = px.bar(
        x=top_product_sales.values,
        y=top_product_sales.index,
        orientation="h",
        labels={"x": "Sales", "y": "Product"},
        color=top_product_sales.values,
        color_continuous_scale="Blues"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("💰 Top 10 Products by Profit")

    fig = px.bar(
        x=top_product_profit.values,
        y=top_product_profit.index,
        orientation="h",
        labels={"x": "Profit", "y": "Product"},
        color=top_product_profit.values,
        color_continuous_scale="Greens"
    )

    st.plotly_chart(fig, use_container_width=True)


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
    st.subheader("🏙️ Top States by Sales")

    fig = px.bar(
        x=state_sales.values,
        y=state_sales.index,
        orientation="h",
        labels={"x": "Sales", "y": "State"},
        color=state_sales.values,
        color_continuous_scale="Blues"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("🏙️ Top States by Profit")

    fig = px.bar(
        x=state_profit.values,
        y=state_profit.index,
        orientation="h",
        labels={"x": "Profit", "y": "State"},
        color=state_profit.values,
        color_continuous_scale="Greens"
    )

    st.plotly_chart(fig, use_container_width=True)


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
    st.subheader("📊 Sales by Sub-Category")

    fig = px.bar(
        x=subcategory_sales.values,
        y=subcategory_sales.index,
        orientation="h",
        labels={"x": "Sales", "y": "Sub-Category"},
        color=subcategory_sales.values,
        color_continuous_scale="Blues"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("💰 Profit by Sub-Category")

    fig = px.bar(
        x=subcategory_profit.values,
        y=subcategory_profit.index,
        orientation="h",
        labels={"x": "Profit", "y": "Sub-Category"},
        color=subcategory_profit.values,
        color_continuous_scale="Greens"
    )

    st.plotly_chart(fig, use_container_width=True)


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
<center>

### 📊 Superstore Sales Dashboard

Developed by **Okpanachi Ogwu**

Python • Pandas • Plotly • Streamlit

</center>
""",
unsafe_allow_html=True
)

#===============================
#MAKE IT LOOK PREMIUM 
#===============================

hide_st_style = """
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""

st.markdown(hide_st_style, unsafe_allow_html=True)
