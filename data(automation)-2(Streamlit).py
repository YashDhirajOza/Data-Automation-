import pandas as pd
import streamlit as st
from datetime import datetime
from io import StringIO
import matplotlib.pyplot as plt

def main():
    st.title("Data Analyzer")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        report = generate_report(data)
        
        st.subheader("Data Analysis Report")
        st.text(report)
        
        if st.button("Save Report"):
            save_report(report)
        
        st.subheader("Plot Data")
        
        x_column = st.selectbox("Select Column for X-axis:", data.columns.tolist())
        y_column = st.selectbox("Select Column for Y-axis:", data.columns.tolist())
        
        if st.button("Plot Histogram"):
            plot_histogram(data, x_column)
        
        if st.button("Plot Regression"):
            plot_regression(data, x_column, y_column)

def generate_report(data):
    report_lines = []

    report_lines.append("Data Analysis Report")
    report_lines.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("=" * 80)

    # Basic Information
    buffer = StringIO()
    data.info(buf=buffer)
    report_lines.append("Basic Information")
    report_lines.append(buffer.getvalue())
    report_lines.append("=" * 80)

    # First 5 Rows
    report_lines.append("First 5 Rows of the Dataset")
    report_lines.append(data.head().to_string())
    report_lines.append("=" * 80)

    # Statistics Summary
    report_lines.append("Basic Statistics Summary")
    report_lines.append(data.describe(include='all').to_string())
    report_lines.append("=" * 80)

    # Mean Values
    report_lines.append("Mean of Numerical Columns")
    report_lines.append(data.mean(numeric_only=True).to_string())
    report_lines.append("=" * 80)

    # Median Values
    report_lines.append("Median of Numerical Columns")
    report_lines.append(data.median(numeric_only=True).to_string())
    report_lines.append("=" * 80)

    # Standard Deviation
    report_lines.append("Standard Deviation of Numerical Columns")
    report_lines.append(data.std(numeric_only=True).to_string())
    report_lines.append("=" * 80)

    # Missing Values
    report_lines.append("Count of Missing Values in Each Column")
    report_lines.append(data.isnull().sum().to_string())
    report_lines.append("=" * 80)

    # Correlation Matrix
    report_lines.append("Correlation Matrix")
    report_lines.append(data.corr().to_string())
    report_lines.append("=" * 80)

    return "\n".join(report_lines)

def save_report(report):
    b64 = base64.b64encode(report.encode()).decode()
    href = f'<a href="data:file/txt;base64,{b64}" download="report.txt">Download Report</a>'
    st.markdown(href, unsafe_allow_html=True)

def plot_histogram(data, column):
    fig, ax = plt.subplots()
    data[column].hist(ax=ax)
    ax.set_title(f'Histogram of {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Frequency')
    st.pyplot(fig)9

def plot_regression(data, x_column, y_column):
    fig, ax = plt.subplots()
    data.plot(kind='scatter', x=x_column, y=y_column, ax=ax)
    ax.set_title(f'Regression Plot of {y_column} vs {x_column}')
    st.pyplot(fig)

if __name__ == "__main__":
    main()
