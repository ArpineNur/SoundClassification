### Importing necessary libraries
import os
from playsound import playsound as ps
import json

### Getting the list of .mp3 files
# Getting the directory path
path = input("Provide the path to data folder (skip if the 'data' folder is in the same directory with script): ")
path = './data' if path == '' else path

# Checking the directory existence
if not os.path.exists(path) or not os.path.isdir(path):
    raise Exception(f"{path}  -  Directory not found")

# Getting all files ans filtering .mp3 files
all_files = os.listdir(path)
mp3_files = list(filter(lambda file: ".mp3" in file, all_files))
print(f"Found {len(mp3_files)} mp3 file(s).")

### Playing the sounds
if mp3_files != []:
    print("Starting to play...")
    classified_files = {}

    for file in mp3_files:
        full_path = path + '/' + file
        print(f"Playing {file}...")
        ps(full_path)
    
        # Classification of the sound file
        while True:
            try:
                classifier = input("If the sound was noisy enter 'n', if the sound was clear enter 'c', type 'r' to replay: ")
                if classifier == "n" or classifier == "c":
                    break
                elif classifier == 'r':
                    ps(full_path)
                else:
                    print("Enter only 'n' or 'c'")
            except:
                continue
        classified_files.update({file: classifier})
    print("All files are successfully categorized!")

    ### Saving the results in json format

    # Getting the name of the file from the user
    output = input("Provide the name for the output file ('output.json' by default):")

    # Forcing the file to be JSON format
    if output == '':
        output = "output.json"
    elif ".json" not in output:
        print("The output is saved only in JSON format")
        output += ".json" 

    # Creating the file
    with open(output, 'w') as f:
        json.dump(classified_files, f,  indent=4)

    print("File is successfully saved.")
print("END of run.")