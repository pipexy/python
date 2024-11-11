import os
import signal
import sys
from src.processes.rtsp_processor import RtspProcessor

def get_env_var(name, default=None):
    """Get environment variable with optional default value"""
    value = os.environ.get(name, default)
    if value is None:
        raise ValueError(f"Environment variable {name} is required")
    return value

def signal_handler(signum, frame):
    """Handle shutdown signals"""
    print("\nShutdown signal received. Stopping processor...")
    if processor:
        processor.stop_capture()
    sys.exit(0)

if __name__ == "__main__":
    # Register signal handlers for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Get configuration from environment variables
    rtsp_url = get_env_var("RTSP_URL")
    ftp_host = get_env_var("FTP_HOST")
    ftp_user = get_env_var("FTP_USER")
    ftp_pass = get_env_var("FTP_PASS")
    ftp_dir = get_env_var("FTP_DIR", "/videos")
    segment_duration = int(get_env_var("SEGMENT_DURATION", "60"))

    print(f"Starting RTSP processor with URL: {rtsp_url}")
    print(f"FTP Host: {ftp_host}")
    print(f"FTP Directory: {ftp_dir}")
    print(f"Segment Duration: {segment_duration} seconds")

    # Initialize and start the processor
    processor = RtspProcessor(
        rtsp_url=rtsp_url,
        ftp_host=ftp_host,
        ftp_user=ftp_user,
        ftp_pass=ftp_pass,
        ftp_dir=ftp_dir
    )

    try:
        processor.start_capture(segment_duration=segment_duration)
    except KeyboardInterrupt:
        print("\nShutdown requested. Stopping processor...")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    finally:
        if processor:
            processor.stop_capture()
