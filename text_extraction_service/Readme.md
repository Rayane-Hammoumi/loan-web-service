# Run the docker file

## Build the image 

```bash
docker build -t text_extraction_service .
```

## Run the image 

```bash
docker run -p 8075:8080 text_extraction_service
```

You can add -d option to run it in background

So here the client can consume the service from the chosen port which is `8075` in our case