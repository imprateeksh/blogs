#####################################################################################
# Example demonstrating usage of Streamlit with CLI output (for non-data engineers)
######################################################################################
import pandas as pd
import random
import streamlit as st

# CONSTANTS
TITLE="Data from Multiple Clusters"
SUBHEADER_1="Raw Data"
SUBHEADER_2="Average CPU and Memory Usage per Cluster"
SUBHEADER_3="CPU Usage Distribution"
SUBHEADER_4="Memory Usage Distribution"

def collect_data_from_clusters():
    cluster_data = []

    # data collection from the first cluster
    for i in range(2):
        for _ in range(10):
            cluster_data.append({
                'Cluster': f'Cluster {i+1}',
                'CPU Usage (%)': random.randint(0, 100),
                'Memory Usage (%)': random.randint(0, 100)
            })

    return pd.DataFrame(cluster_data)

def main():
    st.title(TITLE)
    
    # Collect data from clusters using the CLI
    data = collect_data_from_clusters()
    
    # Display the raw data table
    st.subheader(SUBHEADER_1)
    st.write(data)
    
    # Display average CPU and Memory usage per cluster
    st.subheader(SUBHEADER_2)
    avg_data = data.groupby('Cluster').mean()
    st.write(avg_data)
    
    # Display CPU Usage distribution
    st.subheader(SUBHEADER_3)
    st.bar_chart(data['CPU Usage (%)'])
    
    # Display Memory Usage distribution
    st.subheader(SUBHEADER_4)
    st.bar_chart(data['Memory Usage (%)'])


if __name__ == "__main__":
    main()
