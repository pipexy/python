import cv2
import os
import time
from datetime import datetime
from ftplib import FTP
import tempfile

class RtspProcessor:
    def __init__(self, rtsp_url, ftp_host, ftp_user, ftp_pass, ftp_dir="/videos"):
        """
        Initialize RTSP processor with stream and FTP credentials
        
        Args:
            rtsp_url: RTSP stream URL
            ftp_host: FTP server hostname
            ftp_user: FTP username
            ftp_pass: FTP password
            ftp_dir: Remote directory for video storage
        """
        self.rtsp_url = rtsp_url
        self.ftp_host = ftp_host
        self.ftp_user = ftp_user
        self.ftp_pass = ftp_pass
        self.ftp_dir = ftp_dir
        self.running = False

    def start_capture(self, segment_duration=60):
        """
        Start capturing RTSP stream and saving to FTP in segments
        
        Args:
            segment_duration: Duration of each video segment in seconds
        """
        self.running = True
        cap = cv2.VideoCapture(self.rtsp_url)
        
        if not cap.isOpened():
            raise Exception(f"Failed to open RTSP stream: {self.rtsp_url}")

        # Get video properties
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        while self.running:
            # Create temporary file for current segment
            with tempfile.NamedTemporaryFile(suffix='.mp4', delete=False) as temp_file:
                temp_path = temp_file.name
                
                # Initialize video writer
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')
                out = cv2.VideoWriter(
                    temp_path, 
                    fourcc, 
                    fps, 
                    (frame_width, frame_height)
                )

                start_time = time.time()
                frames_written = 0

                while time.time() - start_time < segment_duration and self.running:
                    ret, frame = cap.read()
                    if not ret:
                        break

                    out.write(frame)
                    frames_written += 1

                out.release()

                if frames_written > 0:
                    # Upload to FTP if we captured any frames
                    self._upload_to_ftp(temp_path)

            # Clean up temporary file
            os.unlink(temp_path)

        cap.release()

    def stop_capture(self):
        """Stop the capture process"""
        self.running = False

    def _upload_to_ftp(self, file_path):
        """
        Upload video file to FTP server
        
        Args:
            file_path: Path to local video file
        """
        try:
            ftp = FTP(self.ftp_host)
            ftp.login(self.ftp_user, self.ftp_pass)

            # Create remote directory if it doesn't exist
            try:
                ftp.mkd(self.ftp_dir)
            except:
                pass  # Directory might already exist
            
            ftp.cwd(self.ftp_dir)

            # Generate unique filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            remote_filename = f"video_{timestamp}.mp4"

            # Upload file
            with open(file_path, 'rb') as file:
                ftp.storbinary(f'STOR {remote_filename}', file)

            ftp.quit()
        except Exception as e:
            print(f"FTP upload failed: {str(e)}")
            raise
