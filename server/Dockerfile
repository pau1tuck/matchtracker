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
# This tells Python not to write .pyc files, which are compiled bytecode. Skipping these can make your Docker images smaller and can be useful for development when you want to avoid having compiled files around that might obscure the source.

ENV PYTHONUNBUFFERED 1
# Normally, Python buffers its output; this setting forces it to run in unbuffered mode. It means Python's output (like print statements or logs) is sent straight to the terminal without being buffered. This is really useful in Docker, where you want to see your logs in real-time, especially when debugging.

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]
