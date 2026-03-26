# Use an optimized Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies (needed for LightGBM/XGBoost)
RUN apt-get update && apt-get install -y \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set PYTHONPATH so src is discoverable
ENV PYTHONPATH=/app

# Default command
CMD ["python", "src/pipeline.py"]