# Run the docker file

## Build the image 

```bash
docker build -t solvency_verification_service .
```

## Run the image 

```bash
docker run -p 8078:8080 solvency_verification_service
```

You can add -d option to run it in background

So here the client can consume the service from the chosen port which is `8078` in our case