FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "load_to_kafka.py"]

# docker build -t streaming_data:tag .

# # Run a Docker container
# docker run -p 9090:9090 -d streaming_data:tag
#docker stop  brave_davinci
#docker build -t streaming_data:tag .