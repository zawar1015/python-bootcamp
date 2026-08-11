print("===== File copy Utility =====")

source_file = input(r"Enter source path.")
destination_file = input("Enter destination path .")

bytes_copied = 0
chunk_count = 0

try:

    with open(source_file,"rb") as source:
        with open(destination_file,"wb") as destination:

            print("\n Copying...")

            while True:
                chunk =  source.read(4096)

                if not chunk:
                    break

                destination.write(chunk)


                bytes_copied+=len(chunk)
                chunk_count+=1

    print(f"Bytes copied : {bytes_copied:,}")
    print(f"chunks : {chunk_count}")
    print("\nfile copied successfully")


except FileNotFoundError:
    print("file not found.")
except PermissionError:
    print("permission denied.")
except Exception as e:
    print("unexpected error.")


