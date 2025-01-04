

import os

file_path = input("Please provide the name of the file or directory: ")



permissions=0o775
try:
   os.chmod(file_path,permissions)
   print(f"Permissions for '{file_path}' successfully set to rwxrwxr-x.")
except FileNotFoundError:
     print(f"The file '{file_path}' does not exist.")
except PermissionError:
    print(f"Permission denied. Cannot change permissions for '{file_path}'.")
except Exception as e:
    print(f"An error occurred: {e}")