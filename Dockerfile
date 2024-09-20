FROM python:3.9-slim

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy dependency files
COPY Pipfile ./

# Install pipenv
RUN pip install --no-cache-dir pipenv

# Install dependencies
RUN pipenv install --dev

# Copy the application code
COPY . .

EXPOSE 8000

# Command to run the application
CMD ["pipenv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
