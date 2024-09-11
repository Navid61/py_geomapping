# prerequests
import urllib.request
import json

url = 'https://donnees.montreal.ca/api/3/action/datastore_search?resource_id=a2f43996-87f9-4423-b800-2f2c41ac326e&limit=5&q=title:jones'

# Open the URL and handle potential errors
try:
  with urllib.request.urlopen(url) as response:
    # Read the response data
    data =json.loads(response.read().decode("utf-8"))  # Decode bytes to string (assuming UTF-8 encoding)
    if len(data) > 0:
      # Create a JSON file and write the results to it
      with open('results.json', 'w') as f:
        json.dump(data, f, indent=4)  # Indent the JSON output for better readability
    else:
      print("Data not found in the response.")
except urllib.error.URLError as e:
  print(f"An error occurred while fetching the data: {e}")


