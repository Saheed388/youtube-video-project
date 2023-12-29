from confluent_kafka import Consumer, KafkaError
from google.cloud import storage
import csv

# Replace with your Kafka and GCP credentials
kafka_config = {
    'bootstrap.servers': '34.42.19.194:9092',
    'group.id': '1111',
    'auto.offset.reset': 'earliest'
}

gcp_bucket_name = 'alt_new_bucket'
gcp_blob_name = 'spotify_file.csv'  # Replace with your desired output file name

# Set up Kafka consumer
consumer = Consumer(kafka_config)
consumer.subscribe(['my2_topic'])

# Set up Google Cloud Storage client
storage_client = storage.Client()
bucket = storage_client.bucket(gcp_bucket_name)

try:
    while True:
        msg = consumer.poll(timeout=1000)  # Adjust the timeout as needed

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break

        # Process the message (assuming CSV data)
        csv_data = msg.value().decode('utf-8')

        # Save the CSV data to Google Cloud Storage
        blob = bucket.blob(gcp_blob_name)
        blob.upload_from_string(csv_data, content_type='text/csv')

        print("CSV Data successfully uploaded to GCP bucket:", gcp_bucket_name)

except KeyboardInterrupt:
    pass
finally:
    consumer.close()
