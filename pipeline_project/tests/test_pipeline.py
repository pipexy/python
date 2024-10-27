import unittest
from unittest.mock import Mock, patch
import numpy as np
from pipeline_project.src.pipeline import Pipeline, PipelineExecutor

class TestPipeline(unittest.TestCase):
    def setUp(self):
        self.pipeline = Pipeline()
        
    def test_pipeline_creation(self):
        pipeline = (self.pipeline
            .input("rtsp://localhost:554/stream")
            .data("grpc://localhost:50051/create-short_video", "MP4")
            .output("rss://localhost/events"))
            
        self.assertEqual(pipeline.input_url, "rtsp://localhost:554/stream")
        self.assertEqual(pipeline.output_url, "rss://localhost/events")
        self.assertEqual(len(pipeline.steps), 1)
        
    @patch('cv2.VideoCapture')
    def test_pipeline_execution(self, mock_video_capture):
        # Przygotowanie mocków
        mock_video_capture.return_value.isOpened.return_value = True
        mock_video_capture.return_value.read.return_value = (True, np.zeros((480, 640, 3)))
        
        pipeline = (Pipeline()
            .input("rtsp://localhost:554/stream")
            .data("grpc://localhost:50051/create-short_video", "MP4")
            .output("rss://localhost/events"))
            
        executor = PipelineExecutor(pipeline)
        
        # Test wykonania pipeline'u
        try:
            executor.execute()
            self.assertTrue(True)  # Pipeline wykonany bez błędów
        except Exception as e:
            self.fail(f"Pipeline execution failed: {str(e)}")
