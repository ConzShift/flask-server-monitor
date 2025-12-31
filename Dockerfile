# Use an official Python runtime
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your Flask app uses
EXPOSE 5000

# Run the Flask app
CMD ["python3", "app.py"]