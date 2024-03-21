FROM python:3.11-slim

# Update and upgrade the package lists from the repositories
RUN apt-get update && apt-get upgrade --yes

# Set the working directory in the Docker image
WORKDIR /app

# Copy the requirements.txt file and install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the src folder contents into the Docker image
COPY . .

# Command to run the application
CMD ["python", "-m", "src.main"]

