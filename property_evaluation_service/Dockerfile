FROM python:3.8

WORKDIR /app

COPY . /app
# Remove db folder
RUN rm -rf /app/db

# Install dependencies
RUN pip install Flask

EXPOSE 8080

# Step 6: Define the entry point command
CMD ["python", "property_evaluation_service.py"]