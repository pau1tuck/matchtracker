# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Precautionary Debian Linux update
RUN apt-get update && apt-get install -y gettext && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]
