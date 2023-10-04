#
# python script to download all the whl files of packages mentioned in a requirements.txt file
# Author - Anurag Rana
# upload these whl files to nexus repo using twine command 
# twine upload --repository nexus download_folder/*
#

import subprocess

# Specify the file path
file_path = "requirements.txt"

# Initialize an empty list to store the lines
lines = []

# Open the file and read its contents line by line
with open(file_path, "r") as file:
    for line in file:
        # Remove leading and trailing whitespace (e.g., newline characters)
        line = line.strip()
        # Append the cleaned line to the list
        lines.append(line)

# Now 'lines' contains each line from the file as separate elements
print(lines)

# List of package names for which you want to download .whl files
package_names = lines # ["package1", "package2"]

# Directory where you want to save the downloaded .whl files
download_directory = "downloaded_whl_files"

# Create the download directory if it doesn't exist
subprocess.run(["mkdir", "-p", download_directory])

# Loop through each package and download its .whl file
for package_name in package_names:
    try:
        # Execute the 'pip download' command to download the .whl file
        subprocess.run(["pip", "download", "--dest", download_directory, package_name])
        print(f"Downloaded {package_name} to {download_directory}")
    except Exception as e:
        print(f"Error downloading {package_name}: {str(e)}")

print("Download completed.")
