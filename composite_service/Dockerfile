FROM python:3.8

WORKDIR /app

COPY . /app
# Remove db folder
RUN rm -rf /app/db

# Install dependencies
RUN pip install spyne
RUN pip install pysqlite3
RUN pip install lxml
RUN pip install twisted
RUN pip install suds

EXPOSE 8080

# Step 6: Define the entry point command
CMD ["python", "composite_service.py"]