import json
import base64
import requests

# Assign your variables
token = ""
image_file_path = ""

# Open image file and encode to base64
with open(image_file_path, "rb") as image_file:
    base_64_image_file = base64.b64encode(image_file.read()).decode('utf-8')

# Set headers
headers = {
    "Authorization": f"Bearer {token}"
}

# Set payload
payload = json.dumps({
    "file_name": image_file_path,
    "image": base_64_image_file
})

# Upload image to Typeform
response = requests.request("POST", "https://api.typeform.com/images", headers=headers, data=payload)

# Print new image URL
json_response = response.json()
print(json_response["src"])
