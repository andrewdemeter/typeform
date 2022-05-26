import json
import requests

# Assign your variables
token = ""
image_url = ""

# Set headers
headers = {
    "Authorization": f"Bearer {token}"
}

# Set payload
payload = json.dumps({
    "url": image_url
})

# Upload image to Typeform
response = requests.request("POST", "https://api.typeform.com/images", headers=headers, data=payload)

# Print new image URL
json_response = response.json()
print(json_response["src"])
