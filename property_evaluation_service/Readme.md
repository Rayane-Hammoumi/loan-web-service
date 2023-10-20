# Run the docker file

## Build the image 

```bash
docker build -t property_service .
```

## Run the image 

```bash
docker run -p 8076:8080 -v "$(pwd)"/db:/app/db property_service
```

You can add -d option to run it in background

So here the client can consume the service from the chosen port which is `8076` in our case