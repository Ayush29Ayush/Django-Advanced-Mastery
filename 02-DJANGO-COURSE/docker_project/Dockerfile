# Use a specific version of the official Python image as the base image
FROM python:3.10.12

# Set environment variables to optimize Python behavior
# PYTHONDONTWRITEBYTECODE = 1 prevents Python from writing .pyc files to disk
# PYTHONBUFFERED = 1 ensures that the Python output is sent straight to the terminal (unbuffered)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

# Set the working directory inside the container to /code
WORKDIR /code

# Copy the requirements.txt file into the container
COPY requirements.txt /code/

# Install Python dependencies from the requirements.txt file
RUN pip install -r requirements.txt

# Copy the rest of the application files into the container
COPY . /code/
