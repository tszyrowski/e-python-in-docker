Setap for python develpement inside constainers
===============================================

# Usage
Build docker image:
```
docker build -t fastapi-image .
```
Run:
```
docker run --name fastapi-container -p 80:80 fastapi-image
```
Or in detached mode
```
docker run --name fastapi-container -p 80:80 -d fastapi-image
```
To stop it:
```
docker stop fastapi-container
```