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
st.write("Thank you for using Streamlit to explore various widgets for data engineering!")


# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import base64

# # Title and description
# st.title("Data Engineering Dashboard")
# st.write("Welcome to the data engineering dashboard! Explore and analyze your data.")

# # Sidebar filters
# st.sidebar.subheader("Data Filters")
# dataset = st.sidebar.selectbox("Select Dataset", ("Dataset A", "Dataset B"))
# date_range_str = st.sidebar.date_input("Select Date Range")

# # Convert date_range_str to pandas Timestamp
# date_range = pd.to_datetime(date_range_str)

# # Data loading and processing
# if dataset == "Dataset A":
#     data = pd.read_csv("resources/dataset_a.csv")
# else:
#     data = pd.read_csv("resources/dataset_b.csv")

# # Convert 'Date' column to pandas Timestamp
# data['Date'] = pd.to_datetime(data['Date'])

# # Filter data based on date_range
# data = data[data["Date"] >= date_range]


# # Data loading and processing
# if dataset == "Dataset A":
#     data = pd.read_csv("resources/dataset_a.csv")
# else:
#     data = pd.read_csv("resources/dataset_b.csv")

# data = data[data["Date"] >= date_range]

# # Data summary
# st.subheader("Data Summary")
# st.write(data.head())

# # Bar chart
# st.subheader("Bar Chart")
# bar_data = data.groupby("Category")["Value"].sum()
# fig, ax = plt.subplots()
# ax.bar(bar_data.index, bar_data.values)
# plt.xticks(rotation=45)
# st.pyplot(fig)

# # Scatter plot
# st.subheader("Scatter Plot")
# x_col = st.selectbox("Select X-axis column", data.columns)
# y_col = st.selectbox("Select Y-axis column", data.columns)
# fig, ax = plt.subplots()
# ax.scatter(data[x_col], data[y_col])
# ax.set_xlabel(x_col)
# ax.set_ylabel(y_col)
# st.pyplot(fig)

# # Data export
# st.subheader("Data Export")
# export_format = st.radio("Select Export Format", ("CSV", "Excel"))
# export_button = st.button("Export Data")
# if export_button:
#     if export_format == "CSV":
#         data.to_csv("exported_data.csv", index=False)
#         st.success("Data exported as CSV.")
#     elif export_format == "Excel":
#         data.to_excel("exported_data.xlsx", index=False)
#         st.success("Data exported as Excel.")

# # Data download
# st.subheader("Data Download")
# download_button = st.button("Download Data")
# if download_button:
#     csv = data.to_csv(index=False)
#     b64 = base64.b64encode(csv.encode()).decode()
#     href = f'<a href="data:file/csv;base64,{b64}" download="downloaded_data.csv">Click here to download</a>'
#     st.markdown(href, unsafe_allow_html=True)

