from flask import Flask, request


from flask_cors import CORS
import os
app = Flask(__name__)
CORS(app) # fix CORS policy

DB_MODE = os.environ.get("DB_MODE", default="FILE")
print("DB_MODE ", DB_MODE)
if DB_MODE == "FILE":
    from data_ingestion_to_file import FileIngestion
    ingestion = FileIngestion()
elif DB_MODE == "MONGO":
    from data_ingestion_to_mongodb import MongoIngestion
    MONGGO_CONNECTION_STRING = os.environ.get("MONGGO_CONNECTION_STRING", default="")
    MONGGO_DATABASE = os.environ.get("MONGGO_DATABASE", default="")
    ingestion = MongoIngestion(MONGGO_CONNECTION_STRING, MONGGO_DATABASE)
    print("MONGGO_CONNECTION_STRING ", MONGGO_CONNECTION_STRING)
    print("MONGGO_DATABASE ", MONGGO_DATABASE)

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