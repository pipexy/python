import unittest
from unittest.mock import Mock
from pipeline_project.src.processes.transcriber import Transcriber
from pipeline_project.src.pipeline_pb2 import AudioRequest

class TestTranscriber(unittest.TestCase):
    def setUp(self):
        self.transcriber = Transcriber()
        
    def test_transcribe(self):
        # Przygotowanie danych testowych
        request = AudioRequest(audio_data=b"dummy_audio", format='wav')
        
        # Wywołanie metody
        context = Mock()
        response = self.transcriber.Transcribe(request, context)
        
        # Sprawdzenie rezultatu
        self.assertIsNotNone(response)
        self.assertIsInstance(response.text, str)
        self.assertGreater(len(response.text), 0)
