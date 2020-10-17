### development run 

```
export FLASK_APP=main.py flask run
```

# live run 

```
nohup gunicorn -w 1 --bind 0.0.0.0:6789 main:app >> app.log
```