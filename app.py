import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Data visualization Dashboard")

# file uploader

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # with open("saved_file.csv", "wb") as f:
    #   f.write(uploaded_file.getbuffer())
    # by with(open), in the above code, we can save the uploaded file locally
    df = pd.read_csv(uploaded_file)
    num_rows = st.slider("Rows to display", 5, min(100, len(df)), 5)# Slider to select number of rows to display
    column = st.selectbox("Column to count unique values", df.columns)# Select a column to count unique values
    st.subheader("Data Preview")
    st.write(df.head(num_rows)) # Display the first few rows of the dataframe
    st.write(f"The data contains {df.shape[0]} rows and {df.shape[1]} columns.")
    st.write(df[column].value_counts())  # Display the count of unique values in the selected column

    st.subheader("Summary Statistics")
    st.write(df.describe())  # Display summary statistics of the dataframe

    st.subheader("Plot Charts")
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    all_columns = df.columns
    chart_type = st.selectbox("Choose Chart Type Of Your Choice", ["Bar Chart", "Line Chart", "Scatter Plot"])  # Add more chart types as needed
    x_axis = st.selectbox("x-axis", all_columns)
    y_axis = st.selectbox("y-axis", numeric_columns)
    
    
    if st.button("Generate Chart"):
        if chart_type == "Line Chart":
            fig = px.line(df, x=x_axis, y=y_axis, title=f"{y_axis} over {x_axis}")
            st.plotly_chart(fig)
            
        elif chart_type == "Bar Chart":
            fig = px.line(df, x=x_axis, y=y_axis, title=f"{y_axis} by {x_axis}")
            st.plotly_chart(fig)

        elif chart_type == "Scatter Plot":
            fig = px.scatter(df, x=x_axis, y=y_axis, title=f"The Scatter Plot Of {y_axis} by {x_axis}")
            st.plotly_chart(fig)
        else:
            st.error("Please select a valid chart type.")
    st.download_button("Download Data", data=df.to_csv(index=False), file_name="data.csv", mime="text/csv")

else:
    st.info("Please upload a CSV file to get started.")