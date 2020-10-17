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

Your data will be save at web-server/data