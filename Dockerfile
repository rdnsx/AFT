# Base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the required dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the environment variable
ENV FLASK_APP=aft.py

# Expose the default Flask port
EXPOSE 5000

# Start the Flask application
CMD ["flask", "run", "--host", "0.0.0.0"]

