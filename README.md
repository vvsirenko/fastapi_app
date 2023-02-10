# fastapi_app

## Build the Docker Image

* Go to the project directory (in where your Dockerfile is, containing your app directory).
* Build your FastAPI image: 
```console
~$ docker build -t myimage .
```
* Run a container based on your image:
```console
~$ docker run -d --name mycontainer -p 80:80 myimage
```
* Check it

`http://127.0.0.1/docs`
