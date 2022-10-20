# Python Flask - Convert cidr address to subnet
Example Project on how to develop RESTful API with Flask and Python

Converts cidr address to subnet using API POST. 

JSON body example: 

```
{
    "cidr": "10.10.1.32/12"
} 
```

## Test Flask Code 

Command to run flask: 
flask run 

## Docker build commands: 

Pod error: 
standard_init_linux.go:228: exec user process caused: exec format error

Reason: 
This error could also occur if an image was built on a MacBook Pro with a Apple M1 Pro chip, which is ARM-based, so by default the Docker build command targets arm64.

Docker in fact detects the Apple M1 Pro platform as linux/arm64/v8

Specifying the platform to both the build command and version tag was enough:

Build for ARM64 (default):
docker build -t <image-name>:<version>-arm64 .

Build for ARM64:
docker build --platform=linux/arm64 -t <image-name>:<version>-arm64 .

Examples: 
docker build -t demo/flask-api:0.0 .
docker build -t flask-api-subnet2cidr .
docker build --platform=linux/amd64 -t flask-api-subnet2cidr:v1-amd64 .

Tag Image: 
docker tag flask-api-subnet2cidr:v1-amd64 pauldj/flask-api-subnet2cidr:v1-amd64

Push Image: 
docker push pauldj/flask-api-subnet2cidr:v1-amd64