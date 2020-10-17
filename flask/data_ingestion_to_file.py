import datetime
import os

class FileIngestion:
    def __init__(self):
        self.folder = "data"

    def ingest(self, data):
        date = datetime.datetime.now()
        today = date.strftime("%Y-%m-%d")
        file_path = os.path.join(self.folder, today + ".csv")
        file = open(file_path, 'a')
        data_line = str(data['timestamp']) + "," + str(data['url'])
        file.write(data_line + "\n")
