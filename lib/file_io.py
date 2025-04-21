from pathlib import Path

def write_file(file_name, file_content):
    path = Path(f"{file_name}.txt")
    with path.open('w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    path = Path(f"{file_name}.txt")
    with path.open('a') as file:
        file.write(append_content)

def read_file(file_name):
    path = Path(f"{file_name}.txt")
    with path.open('r') as file:
        return file.read()


        
