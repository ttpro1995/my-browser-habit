### development run 

Choose this mode if you are going to code. Your working directory should be in web-server/

```
export FLASK_APP=main.py flask run
```

# live run
Choose this mode if you are going to use. Your working directory should be in web-server/
```
nohup gunicorn -w 1 --bind 0.0.0.0:6789 main:app >> app.log &
```

If you run with mongo database

```
nohup DB_MODE=MONGO MONGGO_CONNECTION_STRING=yourconnectionstring MONGGO_DATABASE=your_mongo_db_name gunicorn -w 1 --bind 0.0.0.0:6789 main:app >> app.log &
```

Data will be save to collection 

```your_mongo_db_name.visited```

Your data will be save at web-server/data