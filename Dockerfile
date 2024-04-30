# Stage 1: Build the application
FROM python:3.11-slim AS builder

# Set working directory
WORKDIR /app

# Copy only the requirements file to install dependencies
COPY requirements.txt .

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt && \
    pip3 list
# Copy the entire application code
COPY . .

# Stage 2: Create the final lightweight image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only the required files from the previous stage
COPY --from=builder /app .

RUN chmod +x run.py

# Expose the port your app runs on
EXPOSE 5000

# Run the application
CMD ["python", "run.py"]
