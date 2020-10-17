from flask import Flask, request
from flask.data_ingestion_to_file import FileIngestion

app = Flask(__name__)
ingestion = FileIngestion()


@app.route('/log-url', methods=['POST'])
def log_url():
    result = {"error": 0}
    data = request.json
    ingestion.ingest(data)
    return result


@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(port=6789)