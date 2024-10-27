FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port (if necessary)
EXPOSE 5000

# Command to run your application
CMD ["python", "serve.py"]
