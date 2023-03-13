import hashlib
import os
import sys
from colorama import Fore, Back, Style

try:
    write_dir = str(input('Where should the output file be extracted to? Please include a trailing slash!: '))
except:
    print("Error detecting directory")


#folder_path = '/path/to/folder'
try:
    #option = int(input(Fore.YELLOW + 'Enter menu option: ' + Style.RESET_ALL))
    folder_path = str(input('Please enter directory containing files: '))
except:
    print(Fore.RED + 'Error detecting directory' + Style.RESET_ALL)

file_location = write_dir + "/output.txt"
sys.stdout = open(file_location, 'wt')

# Iterate through all files in the folder
for file_name in os.listdir(folder_path):
    # Check if current item is a file
    if os.path.isfile(os.path.join(folder_path, file_name)):
        # Open the file in read-only binary mode
        with open(os.path.join(folder_path, file_name), 'rb') as f:
            # Read the contents of the file in chunks to avoid loading large files into memory
            md5_hash = hashlib.md5()
            while chunk := f.read(8192):
                md5_hash.update(chunk)
            # Print the MD5 checksum of the file
            print(f"{file_name}: {md5_hash.hexdigest()}")
