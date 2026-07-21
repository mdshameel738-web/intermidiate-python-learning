from pathlib import Path

file_path = Path(__file__).resolve().parent / "my_file.txt"

# with file_path.open() as file:
#     contents = file.read()
#     print(contents)
    

with open("newfile.txt",mode="w") as file:
    file.write("\nhyyyyy")
    

# with file_path.open() as file:
#     contents = file.read()
#     print(contents)
#     file.close()
