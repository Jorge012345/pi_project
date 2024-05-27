# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster AS base
FROM base as builder

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:80", "application:main()", "--workers", "1", "--threads", "1",  "--access-logfile", "-", "--timeout", "0"]