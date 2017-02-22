#Liana - a publication posts start up
###powered by django

liana-nil.ir is coming soon...

you can change language in all pages with change this in lian/setting.py


```python
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
```
or
```python
LANGUAGE_CODE = 'fa'

TIME_ZONE = 'Asia'
```
**for usr:**
```bash
pip install -r requirments.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

for future:
[ ] multiuser
[ ] mobile application
[ ] telegram bot client
