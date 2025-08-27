
import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO

st.set_page_config(page_title="Pandas Playground", page_icon="🧪", layout="wide")

st.title("🧪 Streamlit + pandas sample app")
st.write(
    "Use this tiny app to test hosting. Upload a CSV, explore, filter, and download results."
)

@st.cache_data
def load_demo_data(rows: int = 1000, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({
        "id": np.arange(1, rows + 1),
        "category": rng.choice(list("ABCDE"), size=rows),
        "value": rng.normal(100, 15, size=rows).round(2),
        "score": rng.uniform(0, 1, size=rows).round(3),
        "date": pd.to_datetime("2024-01-01") + pd.to_timedelta(rng.integers(0, 200, size=rows), unit="D"),
    })
    return df

st.sidebar.header("Data source")
source = st.sidebar.radio(
    "Choose data source",
    ["Upload CSV", "Use demo data"],
    index=1,
)

if source == "Upload CSV":
    uploaded = st.file_uploader("Upload a CSV file", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
    else:
        st.info("Upload a CSV to continue, or switch to demo data in the sidebar.")
        st.stop()
else:
    rows = st.sidebar.slider("Demo rows", min_value=100, max_value=100000, value=2000, step=100)
    df = load_demo_data(rows)

st.subheader("Preview")
st.dataframe(df.head(50), use_container_width=True)

st.sidebar.header("Filters")
numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
date_cols = df.select_dtypes(include=["datetime64[ns]", "datetime64[ns, UTC]"]).columns.tolist()
cat_cols = df.select_dtypes(exclude=["number", "datetime64[ns]", "datetime64[ns, UTC]"]).columns.tolist()

# Category filter (first categorical col, if any)
if cat_cols:
    cat_col = st.sidebar.selectbox("Categorical column", options=cat_cols, index=0)
    cat_vals = sorted(df[cat_col].dropna().unique().tolist())
    chosen = st.sidebar.multiselect("Include values", options=cat_vals, default=cat_vals[: min(5, len(cat_vals))])
    if chosen:
        df = df[df[cat_col].isin(chosen)]

# Numeric range filter (first numeric col, if any)
if numeric_cols:
    num_col = st.sidebar.selectbox("Numeric column", options=numeric_cols, index=0)
    min_v, max_v = float(df[num_col].min()), float(df[num_col].max())
    rng = st.sidebar.slider(f"Range for {num_col}", value=(min_v, max_v), min_value=min_v, max_value=max_v)
    df = df[(df[num_col] >= rng[0]) & (df[num_col] <= rng[1])]

# Date range filter (first date col, if any)
if date_cols:
    date_col = st.sidebar.selectbox("Date column", options=date_cols, index=0)
    dmin, dmax = df[date_col].min(), df[date_col].max()
    start, end = st.sidebar.date_input("Date range", value=(dmin.date(), dmax.date()))
    if isinstance(start, tuple):  # streamlit returns tuple when not set
        start, end = start
    mask = (df[date_col] >= pd.to_datetime(start)) & (df[date_col] <= pd.to_datetime(end))
    df = df.loc[mask]

st.subheader("Quick stats")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Rows", len(df))
with col2:
    st.metric("Columns", df.shape[1])
with col3:
    st.metric("Missing values", int(df.isna().sum().sum()))

st.subheader("Summary by category")
if "category" in df.columns and "value" in df.columns:
    agg = df.groupby("category", dropna=False)["value"].agg(["count", "mean", "min", "max"]).reset_index()
    st.bar_chart(agg.set_index("category")["mean"])
    st.dataframe(agg, use_container_width=True)
else:
    st.info("Add 'category' and 'value' columns to see the grouped view (present in demo data).")

st.subheader("Download filtered data")
@st.cache_data
def to_csv_bytes(dataframe: pd.DataFrame) -> bytes:
    return dataframe.to_csv(index=False).encode("utf-8")

csv_bytes = to_csv_bytes(df)
st.download_button("Download CSV", data=csv_bytes, file_name="filtered.csv", mime="text/csv")

st.caption("Built with Streamlit + pandas. Safe to deploy as a sample.")
