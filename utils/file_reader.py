import os

class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_config(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"{self.file_path} not found")
        
        with open(self.file_path, "r") as file:
            return file.read()