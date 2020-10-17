### development run 

Choose this mode if you are going to code.

```
export FLASK_APP=main.py flask run
```

# live run
Choose this mode if you are going to use it
```
nohup gunicorn -w 1 --bind 0.0.0.0:6789 main:app >> app.log
```

Your data will be save at web-server/data