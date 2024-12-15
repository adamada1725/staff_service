# Use an official Python runtime as a parent image
FROM python:3.13.1-alpine

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in docker
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


RUN ["chmod", "+x", "entrypoint.sh"]

ENTRYPOINT ["sh", "entrypoint.sh"]