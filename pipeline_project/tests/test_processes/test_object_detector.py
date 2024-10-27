import unittest
import numpy as np
import cv2
from unittest.mock import Mock
from pipeline_project.src.processes.object_detector import ObjectDetector
from pipeline_pb2 import ImageRequest

class TestObjectDetector(unittest.TestCase):
    def setUp(self):
        self.detector = ObjectDetector()
        
    def test_detect_objects(self):
        # Przygotowanie danych testowych
        test_image = np.zeros((480, 640, 3), dtype=np.uint8)
        _, buffer = cv2.imencode('.jpg', test_image)
        request = ImageRequest(image_data=buffer.tobytes(), format='jpg')
        
        # Wywołanie metody
        context = Mock()
        response = self.detector.DetectObjects(request, context)
        
        # Sprawdzenie rezultatu
        self.assertIsNotNone(response)
        self.assertGreater(len(response.objects), 0)
        self.assertIn("person", response.objects)
