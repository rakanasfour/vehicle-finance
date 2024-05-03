# Use python 3.11 slim as the base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the entire application code
COPY . .

# Make the run.py file executable
RUN chmod +x run.py

# Expose the port your app runs on
EXPOSE 5000

# Run the application
CMD ["python", "run.py"]
