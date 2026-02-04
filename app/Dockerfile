
# Dockerfile for FastAPI app
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements.txt from parent directory
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port (default FastAPI port)
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
