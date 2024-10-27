import unittest
import numpy as np
import cv2
from unittest.mock import Mock
from src.processes.movement_detector import MovementDetector
from pipeline_pb2 import ImageRequest

class TestMovementDetector(unittest.TestCase):
    def setUp(self):
        self.detector = MovementDetector()
        
    def test_detect_movement(self):
        # Przygotowanie danych testowych
        test_image = np.zeros((480, 640, 3), dtype=np.uint8)
        _, buffer = cv2.imencode('.jpg', test_image)
        request = ImageRequest(image_data=buffer.tobytes(), format='jpg')
        
        # Wywołanie metody
        context = Mock()
        response = self.detector.DetectMovement(request, context)
        
        # Sprawdzenie rezultatu
        self.assertIsNotNone(response)
        self.assertEqual(len(response.detections), 0)  # First frame should have no detections
