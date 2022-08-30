# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9-buster

COPY . ./

WORKDIR /

# Install production dependencies.
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "grpc_server.py"]
