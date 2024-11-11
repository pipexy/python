# python
python pipexy
```
docs/
├── getting-started/
│   ├── installation.md
│   ├── quick-start.md
│   └── basic-concepts.md
├── user-guide/
│   ├── pipeline-configuration.md
│   ├── processors/
│   │   ├── video-processor.md
│   │   ├── movement-detector.md
│   │   ├── object-detector.md
│   │   ├── transcriber.md
│   │   ├── captioner.md
│   │   ├── describer.md
│   │   └── rss-creator.md
│   └── deployment.md
├── api-reference/
│   ├── pipeline.md
│   ├── processors.md
│   └── data-types.md
├── development/
│   ├── architecture.md
│   ├── adding-processors.md
│   ├── testing.md
│   └── contributing.md
└── examples/
    ├── basic-pipeline.md
    ├── custom-processor.md
    └── configuration.md
```
# DataPipeX Documentation

## Overview
DataPipeX is a flexible, extensible framework for building data processing pipelines using gRPC and Python. It enables the creation of distributed data processing workflows with a focus on multimedia processing, analysis, and content generation.

## Table of Contents
1. [Installation](#installation)
2. [Architecture](#architecture)
3. [Quick Start](#quick-start)
4. [Core Components](#core-components)
5. [Pipeline Configuration](#pipeline-configuration)
6. [Process Modules](#process-modules)
7. [Development Guide](#development-guide)
8. [API Reference](#api-reference)
9. [Testing](#testing)
10. [Deployment](#deployment)
11. [Contributing](#contributing)

## Installation

### Requirements
- Python 3.8+
- OpenCV
- gRPC
- Protocol Buffers

### Setup
```bash
# Clone the repository
git clone https://github.com/your-org/datapipex.git
cd datapipex

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Generate gRPC code
python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. proto/pipeline.proto

# Start server
python pipeline_runner.py

python rtsp_pipeline.py
```

## Architecture

### High-Level Architecture
```
+----------------+     +----------------+     +----------------+
|   Input        |     |   Process     |     |   Output      |
|   Sources      |---->|   Pipeline    |---->|   Endpoints   |
|   (RTSP/HTTP)  |     |   (gRPC)      |     |   (RSS/HTTP)  |
+----------------+     +----------------+     +----------------+
```

### Component Overview
- **Pipeline Engine**: Core system managing data flow
- **Process Modules**: Individual processing units
- **gRPC Services**: Communication layer
- **Data Types**: Standardized data formats

## Quick Start

### Basic Usage
```python
from datapipex import Pipeline

# Create pipeline
pipeline = (Pipeline()
    .input("rtsp://localhost:554/stream")
    .data("grpc://localhost:50051/create-short_video", "MP4")
    .data("grpc://localhost:50051/detect-movement", "JPG")
    .output("rss://localhost/events"))

# Execute pipeline
pipeline.execute()
```

## Core Components

### Pipeline
The main class orchestrating the data flow:
- Input handling
- Process chaining
- Output management
- Error handling
- Resource management

### Processors
Base classes for implementing processing nodes:
```python
from datapipex.processors import BaseProcessor

class CustomProcessor(BaseProcessor):
    def process(self, data):
        # Process implementation
        return processed_data
```

## Pipeline Configuration

### Available Data Types
- `MP4`: Video data
- `JPG`: Image data
- `TEXT`: Text content
- `XML`: Structured data

### Configuration Example
```python
pipeline_config = {
    "input": {
        "type": "rtsp",
        "url": "rtsp://localhost:554/stream"
    },
    "processes": [
        {
            "name": "video_processor",
            "url": "grpc://localhost:50051/create-short_video",
            "type": "MP4"
        },
        # More processes...
    ],
    "output": {
        "type": "rss",
        "url": "rss://localhost/events"
    }
}
```

## Process Modules

### Video Processor
Handles video processing tasks:
- Format conversion
- Frame extraction
- Resolution adjustment
- Compression

### Movement Detector
Detects motion in video streams:
- Frame difference analysis
- Contour detection
- Motion tracking
- Event generation

### Object Detector
Identifies objects in images:
- Object classification
- Bounding box detection
- Confidence scoring

### Transcriber
Converts speech to text:
- Audio extraction
- Speech recognition
- Text formatting

### Captioner
Generates captions for videos:
- Scene analysis
- Caption generation
- Timing synchronization

### Describer
Creates content descriptions:
- Content analysis
- Summary generation
- Keyword extraction

### RSS Creator
Generates RSS feeds:
- Feed creation
- Entry formatting
- XML generation

## Development Guide

### Adding New Processors

1. Create new processor file:
```python
# src/processes/new_processor.py
from pipeline_pb2_grpc import NewProcessorServicer

class NewProcessor(NewProcessorServicer):
    def ProcessData(self, request, context):
        # Implementation
        return response
```

2. Update Protocol Buffer definition:
```protobuf
service NewProcessor {
    rpc ProcessData (DataRequest) returns (DataResponse) {}
}
```

3. Add tests:
```python
# tests/test_processes/test_new_processor.py
class TestNewProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = NewProcessor()
    
    def test_process_data(self):
        # Test implementation
```

### Error Handling
```python
try:
    result = processor.process(data)
except ProcessError as e:
    logging.error(f"Processing error: {e}")
    raise
```

## Testing

### Running Tests
```bash
# Run all tests
python -m pytest tests/

# Run specific test file
python -m pytest tests/test_processes/test_video_processor.py

# Run with coverage
python -m pytest --cov=src tests/
```

### Test Categories
- Unit Tests: Individual components
- Integration Tests: Component interaction
- System Tests: End-to-end pipeline
- Performance Tests: Load and stress testing

## Deployment

### Local Deployment
```bash
# Start server
python pipeline_runner.py

python rtsp_runner.py

# In another terminal, run pipeline
python run_pipeline.py
```

### Docker Deployment
```bash
# Build image
docker build -t datapipex .

# Run container
docker run -p 50051:50051 datapipex
```

## Contributing

### Development Process
1. Fork repository
2. Create feature branch
3. Implement changes
4. Add tests
5. Submit pull request

### Code Style
- Follow PEP 8
- Use type hints
- Document public APIs
- Write meaningful commit messages

## License
MIT License - see LICENSE file for details.