# RTSP to FTP Video Pipeline

This project implements a pipeline that captures video from an RTSP stream and saves it in segments to an FTP server. The pipeline is containerized using Docker and can be easily deployed using Docker Compose.

## Features

- Captures video from RTSP streams
- Segments video into configurable duration chunks
- Automatically uploads video segments to FTP server
- Containerized deployment with Docker
- Includes test RTSP stream server for development

## Prerequisites

- Docker
- Docker Compose

## Configuration

The pipeline is configured using environment variables in the `.env` file. Copy the example configuration file and modify as needed:

```bash
cp .env.example .env
```

### Environment Variables

#### RTSP Configuration
- `RTSP_URL`: URL of the RTSP stream
- `SEGMENT_DURATION`: Duration of video segments in seconds

#### FTP Configuration
- `FTP_HOST`: Hostname of the FTP server
- `FTP_USER`: FTP username for pipeline
- `FTP_PASS`: FTP password for pipeline
- `FTP_DIR`: Directory on FTP server for video storage

#### FTP Server Configuration
- `FTP_SERVER_USER`: Username for FTP server
- `FTP_SERVER_PASS`: Password for FTP server
- `PASV_ADDRESS`: Passive mode address
- `PASV_MIN_PORT`: Minimum port for passive mode range
- `PASV_MAX_PORT`: Maximum port for passive mode range

## Quick Start

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Configure environment:
```bash
cp .env.example .env
# Edit .env file with your configuration
```

3. Start the services:
```bash
docker-compose up -d
```

This will start:
- An FTP server
- A test RTSP stream server
- The RTSP to FTP pipeline

4. Monitor the logs:
```bash
docker-compose logs -f pipeline
```

## Development Setup

The docker-compose.yml includes a test environment with:
- An FTP server (fauria/vsftpd)
- An RTSP simulator (aler9/rtsp-simple-server)
- The pipeline service

Default test credentials are provided in `.env.example`.

## Directory Structure

```
.
├── src/
│   └── processes/
│       └── rtsp_processor.py    # Main RTSP processing logic
├── docker-compose.yml          # Docker Compose configuration
├── Dockerfile                  # Pipeline service Dockerfile
├── requirements.txt           # Python dependencies
├── rtsp_pipeline.py          # Main entry point
├── .env                      # Environment configuration
└── .env.example             # Example environment configuration
```

## Testing

The included docker-compose setup provides a complete test environment. Video segments will be saved in the ./ftp_data directory, which is mounted to the FTP container.

To test with your own RTSP stream:
1. Modify the RTSP_URL in your .env file
2. Restart the services:
```bash
docker-compose down
docker-compose up -d
```

## Stopping the Services

To stop all services:
```bash
docker-compose down
