import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Widgets for user input
st.title("Data Engineering with Streamlit")

# Slider for selecting the number of data points
num_points = st.slider("Select the number of data points:", 10, 100, 50)

# Checkbox to include noise in the data
include_noise = st.checkbox("Include noise in the data", value=True)

# Dropdown to select a feature
selected_feature = st.selectbox("Select a feature:", ['Feature 1', 'Feature 2', 'Feature 3'])

# Text input to enter a custom label
custom_label = st.text_input("Enter a custom label:")

# Generate random data
np.random.seed(42)
data = np.random.rand(num_points, 3) * 100

# Add noise if selected
if include_noise:
    noise = np.random.randn(num_points, 3) * 10
    data += noise

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=['Feature 1', 'Feature 2', 'Feature 3'])

# Display the selected feature's statistics
st.subheader("Selected Feature Statistics:")
st.write(df[selected_feature].describe())

# Plot the data based on two selected features
st.subheader("Scatter Plot:")
selected_feature_2 = st.selectbox("Select another feature for the y-axis:", ['Feature 1', 'Feature 2', 'Feature 3'])
st.set_option('deprecation.showPyplotGlobalUse', False)
plt.scatter(df[selected_feature], df[selected_feature_2])
plt.xlabel(selected_feature)
plt.ylabel(selected_feature_2)
st.pyplot()

# Show Line chart
# Sample data
data_for_line_chart = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 5, 12, 8, 3]
})

# Create a line chart using st.line_chart()
st.line_chart(data_for_line_chart['y'])

# Show a data table
st.subheader("Data Table:")
st.write(df)

# Download link for the data
st.subheader("Download Data:")
if st.button("Download CSV"):
    st.download_button("Click here to download the data", df.to_csv(index=False), file_name="data.csv")

# Progress bar example
st.subheader("Progress Bar:")
progress = st.progress(0)
for i in range(1, 101):
    progress.progress(i)
    st.experimental_rerun()

# Placeholder for displaying custom label
st.subheader("Custom Label:")
st.write(custom_label)

# Show alert message
st.subheader("Alert Message:")
st.warning("Warning: Data points might not be real!")

# Sidebar with additional information
st.sidebar.title("Sidebar")
st.sidebar.write("This is the sidebar where you can add extra information.")

# Explanation for the app
st.sidebar.subheader("About")
st.sidebar.write("This app demonstrates the use of different Streamlit widgets for data engineering purposes.")

# End of the app
st.subheader("End of the App")
st.write("Hope you explored various widgets!")
