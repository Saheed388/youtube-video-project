FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "extract_to_storage.py"]

# # Build the Docker image
# docker build -t collect_data:tag .

# # Run a Docker container
# docker run -p 9110:9191 -d collect_data:tag

#docker stop condescending_hertz