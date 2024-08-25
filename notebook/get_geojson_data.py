import requests
import zipfile
import os

# URL of the file to download
url = "https://donnees.montreal.ca/dataset/4ad6baea-4d2c-460f-a8bf-5d000db498f7/resource/866a3dbc-8b59-48ff-866d-f2f9d3bbee9d/download/uniteevaluationfonciere.geojson.zip"

# Define the directory where the file should be saved
download_dir = "/home/navid/tut/geodata/geomap"  # Change this to your specific path

# Ensure the directory exists
os.makedirs(download_dir, exist_ok=True)

# Download the file
response = requests.get(url)
file_name = url.split("/")[-1]
file_path = os.path.join(download_dir, file_name)

# Save the file to the specified directory
with open(file_path, 'wb') as file:
    file.write(response.content)

# Check if the file is a ZIP file and unzip it
if zipfile.is_zipfile(file_path):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(download_dir)  # Extracts to the specified directory

    # Rename the extracted file
    old_name = os.path.join(download_dir, "uniteevaluationfonciere.geojson")
    new_name = os.path.join(download_dir, "properties_assessment_units.geojson")
    
    # Check if the old_name exists before renaming
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"Renamed file: {old_name} to {new_name}")
    else:
        print(f"File to rename not found: {old_name}")
else:
    print(f"Downloaded but not a zip file: {file_path}")
