import unittest
from unittest.mock import Mock
from pipeline_project.src.processes.describer import Describer
from pipeline_pb2 import ContentRequest

class TestDescriber(unittest.TestCase):
    def setUp(self):
        self.describer = Describer()
        
    def test_generate_description(self):
        # Przygotowanie danych testowych
        test_content = "This is a test content that needs to be described."
        request = ContentRequest(content=test_content)
        
        # Wywołanie metody
        context = Mock()
        response = self.describer.GenerateDescription(request, context)
        
        # Sprawdzenie rezultatu
        self.assertIsNotNone(response)
        self.assertIsInstance(response.text, str)
        self.assertGreater(len(response.text), 0)
