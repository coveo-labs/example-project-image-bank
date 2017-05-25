import boto3
import json
import base64


# Title: Image tagging With AWS Rekognition
# Description: This extension is used send an image to AWS Rekognition to detect the content of the image.
# Description: Then, we add a tag containing the different labels, for use as a facet.
# Required data: Original file

# configure the boto client
client = boto3.client(
    "rekognition",
    aws_access_key_id="YOUR ACCESS KEY HERE",
    aws_secret_access_key="YOUR SECRET HERE",
    region_name="us-east-1"
)

# decode to bytes
byte_data = base64.b64decode(document.get_meta_data_value("base64data")[0])

# send to Rekognition
r = client.detect_labels(
    Image={
        "Bytes": byte_data
    },
    MaxLabels=20
)

# add labels
document.add_meta_data({
    "awsrekognition": ";".join([label["Name"] for label in r["Labels"]])
})
