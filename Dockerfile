FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only dependency list first (for build cache)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files (static, templates, app.py, etc.)
COPY . .

# Expose port for Flask
EXPOSE 5001

# Run Flask
CMD ["python", "app.py"]
