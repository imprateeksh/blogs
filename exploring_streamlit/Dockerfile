FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir  -r /app/requirements.txt
EXPOSE 8501

# Command to run the Streamlit app when the container starts
# Running Example 1 here
CMD ["streamlit", "run","/app/example1.py"]
