import zipfile
import requests
import base64
import json
import os


# Title: PPTX Image Extractor
# Description: This extension is used to extract images from PPTX documents and push them in an image bank source.
# Description: The extension should be applied only to PPTX files
# Required data: Original file

# Coveo API calls configuration
api_key = "GENERATE AN API KEY FROM THE ADMIN CONSOLE"
organization_id = "YOUR ORGANIZATION ID"
source_id = "YOUR SOURCE ID for Test PPTX Image Extraction Image Bank"
push_api_url = "https://push.cloud.coveo.com/v1/organizations/{organizationId}/sources/{sourceId}/documents".format(
    organizationId = organization_id,
    sourceId = source_id
)
headers = {
    'Authorization': 'Bearer ' + api_key,
    'content-type': 'application/json'
}

# filename: name of the file, with its extension
# returns true if then image is in the list of supported extensions
def is_supported_image_format(filename):
    return filename.lower().endswith((".png", "jpg", "jpeg"))


# image: binary data containing an image
# parent_uri: uri of the parent presentation
# permissions: permissions of the parent presentation
# returns: None
def push_image(image, filename, checksum, parent_uri, parenttitle, parent_concepts, permissions):
    params = {
        'documentId': "#".join(["file://" + parent_uri, filename])
    }

    encoded_data = base64.b64encode(image)

    body = json.dumps({
        "FileExtension": os.path.splitext(filename)[1],
        "foldfoldingfield": checksum,
        "foldchildfield": checksum,
        "parenturi": parent_uri,
        "parenttitle": parenttitle,
        "parentconcepts": parent_concepts,
        "base64data": encoded_data,
        "connectortype": "from_extension",
        "title": "Extracted image",
        "Permissions": permissions
    })

    r = requests.put(push_api_url, headers=headers, params=params, data=body)

    document_api.v1.log("#".join([parent_uri, filename]) + "::" + str(r.status_code) + "::" + r.text, severity='normal')

# get the document bytes, extract the images
# once extracted, push them in the image bank
with document_api.v1.get_data_stream('documentdata') as f:
    parent_concepts = document_api.v1.get_meta_data_value("concepts")[0]
    zipped_file = zipfile.ZipFile(f)
    parent_uri = document_api.v1.get_meta_data_value("gdfilelink")[0]
    checksum = document_api.v1.get_meta_data_value("gdfilechecksum")[0]
    parenttitle = document_api.v1.get_meta_data_value("gdfileoriginalname")[0]
    map(
        lambda image: push_image(zipped_file.read(image), image, checksum, parent_uri, parenttitle, parent_concepts, []),
        list(filter(lambda filename: is_supported_image_format(filename), zipped_file.namelist()))
    )
