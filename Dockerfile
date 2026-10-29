# Dockerfile — packages training script for CI validation
# JD coverage: Docker, CI/CD
FROM python:3.11-slim

WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy training code
COPY src/train.py .

# default command (for local testing)
CMD ["python", "train.py"]