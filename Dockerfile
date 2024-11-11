FROM python:3.12-slim

WORKDIR /app

# Install system dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Copy all requirements files
COPY requirements.txt requirements.txt
COPY pipeline_project/requirements.txt pipeline_project_requirements.txt

# Install Python dependencies from both requirements files
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir -r pipeline_project_requirements.txt \
    && pip install protobuf>=4.21.0 pyftpdlib>=1.5.9

# Copy source code
COPY src/ ./src/
COPY pipeline_project/ ./pipeline_project/

# Copy main script
COPY rtsp_pipeline.py .

# Set PYTHONPATH to include project directories
ENV PYTHONPATH=/app:/app/pipeline_project

CMD ["python", "rtsp_pipeline.py"]
