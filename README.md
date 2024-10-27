# DataPipeX

DataPipeX is a powerful, extensible framework for building distributed data processing pipelines using gRPC and Python. It specializes in handling multimedia data streams, performing real-time analysis, and generating structured output.

## Features

- **Flexible Pipeline Architecture**: Build complex data processing workflows with ease
- **gRPC-based Communication**: Efficient, scalable inter-process communication
- **Modular Design**: Easy to extend with new processing capabilities
- **Built-in Processors**:
  - Video processing
  - Motion detection
  - Object detection
  - Speech transcription
  - Caption generation
  - Content description
  - RSS feed generation
- **Comprehensive Testing**: Unit tests and integration tests included
- **Well-documented**: Full documentation and examples provided

## Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/your-org/datapipex.git
cd datapipex

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Generate gRPC code
python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. proto/pipeline.proto
```

### Basic Usage

```python
from datapipex import Pipeline

# Create and execute pipeline
pipeline = (Pipeline()
    .input("rtsp://localhost:554/stream")
    .data("grpc://localhost:50051/create-short_video", "MP4")
    .data("grpc://localhost:50051/detect-movement", "JPG")
    .output("rss://localhost/events"))

pipeline.execute()
```

## Documentation

Full documentation is available in the [docs](docs/) directory or at [https://datapipex.readthedocs.io](https://datapipex.readthedocs.io).

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- Issue Tracker: GitHub Issues
- Documentation: [https://datapipex.readthedocs.io](https://datapipex.readthedocs.io)
- Discussion: GitHub Discussions