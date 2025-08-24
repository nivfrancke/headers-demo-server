# Use the official lightweight Python image
FROM python:3.11-slim

# Set an environment variable for Python
ENV PYTHONUNBUFFERED True

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Run the web server with Gunicorn, listening on the port defined by the PORT environment variable
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "8", "--timeout", "0", "main:app"]