import unittest
import numpy as np
import cv2
from unittest.mock import Mock
from pipeline_project.src.processes.captioner import Captioner
from pipeline_pb2 import VideoRequest

class TestCaptioner(unittest.TestCase):
    def setUp(self):
        self.captioner = Captioner()
        
    def test_generate_caption(self):
        # Przygotowanie danych testowych
        test_video = np.zeros((480, 640, 3), dtype=np.uint8)
        _, buffer = cv2.imencode('.mp4', test_video)
        request = VideoRequest(video_data=buffer.tobytes(), format='mp4')
        
        # Wywołanie metody
        context = Mock()
        response = self.captioner.GenerateCaption(request, context)
        
        # Sprawdzenie rezultatu
        self.assertIsNotNone(response)
        self.assertIsInstance(response.text, str)
        self.assertGreater(len(response.text), 0)
