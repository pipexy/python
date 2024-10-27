import unittest
import numpy as np
import cv2
from unittest.mock import Mock
from src.processes.video_processor import VideoProcessor
from pipeline_pb2 import VideoRequest

class TestVideoProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = VideoProcessor()
        
    def test_create_short_video(self):
        # Przygotowanie danych testowych
        test_video = np.zeros((480, 640, 3), dtype=np.uint8)
        _, buffer = cv2.imencode('.mp4', test_video)
        request = VideoRequest(video_data=buffer.tobytes(), format='mp4')
        
        # Wywołanie metody
        context = Mock()
        response = self.processor.CreateShortVideo(request, context)
        
        # Sprawdzenie rezultatu
        self.assertIsNotNone(response)
        self.assertEqual(response.format, 'mp4')
        self.assertGreater(len(response.processed_video), 0)
