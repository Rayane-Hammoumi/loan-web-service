# Run the property evaluation service without docker 
Navigate to the property_evaluation_service folder 
run the following command

```bash
python3  property_evaluation_service.py
```
Open a new Terminal and run the following command

```bash
python3  property_service_client.py
```

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