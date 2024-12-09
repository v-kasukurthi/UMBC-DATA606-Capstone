import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data_path = '/Users/vamsikasukurthi/Desktop/streamlit/Chicago_Crimes_Filtered_Data.csv'  
df = pd.read_csv(data_path)

st.title("Chicago Crimes Data Analysis")
st.write("This Streamlit app provides insights into Chicago crime data.")

st.subheader("Data Preview")
if st.checkbox("Show raw data"):
    st.write(df.head())

df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y %I:%M:%S %p', errors='coerce')

st.sidebar.subheader("Filters")

crime_types = df['Primary Type'].unique()
selected_crime_types = st.sidebar.multiselect("Select Crime Types", crime_types, default=crime_types)

start_date = st.sidebar.date_input("Start Date", value=df['Date'].min())
end_date = st.sidebar.date_input("End Date", value=df['Date'].max())

if start_date > end_date:
    st.sidebar.error("End date must be after start date.")

if selected_crime_types:
    df = df[df['Primary Type'].isin(selected_crime_types)]
df = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]

st.subheader("Crime Count by Type")
crime_counts = df['Primary Type'].value_counts()
fig, ax = plt.subplots()
crime_counts.plot(kind='bar', ax=ax)
ax.set_xlabel("Crime Type")
ax.set_ylabel("Count")
st.pyplot(fig)

st.subheader("Crimes Over Time")
crime_over_time = df.set_index('Date').resample('M').size()  
fig, ax = plt.subplots()
crime_over_time.plot(ax=ax)
ax.set_xlabel("Date")
ax.set_ylabel("Number of Crimes")
st.pyplot(fig)

if 'Latitude' in df.columns and 'Longitude' in df.columns:
    df = df.rename(columns={'Latitude': 'lat', 'Longitude': 'lon'})
    st.subheader("Crime Locations")
    st.map(df[['lat', 'lon']].dropna())

st.write("This is a simple exploratory app. Add more filters or visualizations as needed.")