# Random
This service provides a RESTful API which provides random functionality. It is written in Python using Flask.

The [Swagger Spec](static/swagger.yaml) defines the interface of the service.

## Running Locally
The service can be run as a Docker container or as a Python process.

### Docker Container
```
docker run --pull always --publish 5000:5000 earnestresearch/random:latest
```

### Python Process
Install libraries:
```
pip3 install -r requirements.txt
```

Run:
```
python3 -m flask run
```

## Query
```
curl 'http://localhost:5000/random/default/choice?value=3&value=5&value=7'

{"value":"7"}
```

## Publishing the Docker Image
1. Bump the version in the [VERSION file](VERSION)
1. `./docker-build-and-publish`
