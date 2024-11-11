#!/usr/bin/env python3

import grpc
from concurrent import futures
import logging
import time
from src.processes.video_processor import VideoProcessor
from src.processes.movement_detector import MovementDetector
from src.pipeline import Pipeline, PipelineExecutor
import pipeline_pb2_grpc

# get RTSP variable from env
RTSP_URL = os.getenv("RTSP_URL")

if not RTSP_URL:
    raise ValueError("RTSP_URL environment variable is required")

# Ustawienie logowania


def serve():
    # Utworzenie serwera gRPC
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Dodanie serwisów
    pipeline_pb2_grpc.add_VideoProcessorServicer_to_server(
        VideoProcessor(), server)
    pipeline_pb2_grpc.add_MovementDetectorServicer_to_server(
        MovementDetector(), server)

    # Uruchomienie serwera
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info("Server started on port 50051")

    try:
        while True:
            time.sleep(86400)  # 24 godziny
    except KeyboardInterrupt:
        server.stop(0)
        logging.info("Server stopped")


def run_pipeline():
    # Utworzenie i uruchomienie pipeline'u
    pipeline = (Pipeline()
                .input(RTSP_URL)
                .data("grpc://localhost:50051/create-short_video", "MP4")
                .data("grpc://localhost:50051/detect-movement", "JPG")
                .data("grpc://localhost:50051/detect-object", "TEXT")
                .data("grpc://localhost:50051/transcription", "TEXT")
                .data("grpc://localhost:50051/captioning", "TEXT")
                .data("grpc://localhost:50051/description", "TEXT")
                .data("grpc://localhost:50051/create-rss", "XML")
                .output("rss://localhost:8081/events"))

    executor = PipelineExecutor(pipeline)
    executor.execute()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Uruchom serwer w osobnym wątku
    import threading

    server_thread = threading.Thread(target=serve)
    server_thread.start()

    # Poczekaj na uruchomienie serwera
    time.sleep(2)

    try:
        # Uruchom pipeline
        run_pipeline()
    except KeyboardInterrupt:
        logging.info("Pipeline stopped by user")
    except Exception as e:
        logging.error(f"Pipeline error: {str(e)}")
        raise