# file inspector:

import os
print("------ file inspector ------")
file_path = input("Enter file path : ")
file = None

try: 
    if not os.path.exists(file_path):
        raise FileNotFoundError

    file = open(file_path,"r")

    content= file.read()

    print("\n File Exists : Yes")
    print("File name : ", os.path.basename(file_path))
    print("File Mode : ",file.mode)
    print("File Encoding : ", file.encoding)
    print("Closed status : ", file.closed)
    print("Characters length : ", len(content))

except FileNotFoundError:
    print("File exists : No")
    print("Error : File not found.")

finally:
    if file is not None:
        file.close()
        print("file closed : ", file.closed)
        