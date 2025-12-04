FROM python:3.12-slim

# Do not write .pyc files, and flush output immediately
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# System packages needed for scientific Python
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies from requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project into the image
COPY . /app

# Expose the port your app will run on
EXPOSE 8000
ENV PORT=8000

# Start Gunicorn server: "app" (file) : "app" (Flask object)
CMD gunicorn -b 0.0.0.0:$PORT app:app
