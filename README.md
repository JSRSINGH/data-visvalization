# 📊 Data Visualization Dashboard

A Python + Streamlit app to upload CSV files, explore data, and generate interactive visualizations like bar, line, and scatter plots.  
Perfect for quick data analysis and presentations.

---

## Features

- 📂 Upload any `.csv` file from your computer  
- 🔍 Preview the dataset with customizable number of rows  
- 📈 Generate interactive:
  - Line Chart  
  - Bar Chart  
  - Scatter Plot  
- 📊 View summary statistics (mean, std, min, max, etc.)  
- 🧮 Count unique values for any selected column  
- 💾 Download the dataset as a CSV file

---

## How It Works

1. User uploads a CSV file  
2. App displays:
   - Top rows of the data
   - Data dimensions (rows × columns)
   - Summary statistics  
3. User picks columns for visualizations  
4. App displays selected charts using Plotly  
5. User can download the dataset back as CSV

---

## Built With

- [Python](https://www.python.org/)  
- [Streamlit](https://streamlit.io/) – interactive web app framework  
- [Pandas](https://pandas.pydata.org/) – for data manipulation  
- [Plotly](https://plotly.com/python/) – for interactive charts  

---

## Screenshots

![Dashboard Screenshot](/ScreenShots/1.png)
![Dashboard Screenshot](/ScreenShots/2.png)

---

## Getting Started

### Install dependencies

```bash
pip install -r requirements.txt

### Run the app

```bash
streamlit run app.py
