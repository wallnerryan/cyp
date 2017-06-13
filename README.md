#ChooseYourPro.com
=============================================

@author  Ryan Wallner
@contact wallnerryan@gmail.com

=============================================

ChooseYourPro.com is a comprehensive national golf lessons web application
for both the Player and the Pro.

Features include:
	-Pro Profile
	-Player Profile
	-Find lessons close to you
	-Bid on lesson price
	-Schedule your available lesson times.

www.chooseyourpro.com is not in affiliaiton with PGATour

# How to Run

- Docker
- Docker Compose

```
docker-compose build
docker-compose up -d
docker-compose run web python manage.py syncdb
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
```

Navigate to http://localhost:8000/admin/ and login with superuser.

1. Create a Country (USA/USA and add picture of USA flag)
2. Create a GeoMap (USA) 
3. Navigate to http://localhost:8000/ and click through
