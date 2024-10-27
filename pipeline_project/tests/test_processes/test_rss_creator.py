import unittest
from unittest.mock import Mock
from pipeline_project.src.processes.rss_creator import RssCreator
from pipeline_pb2 import RssRequest

class TestRssCreator(unittest.TestCase):
    def setUp(self):
        self.rss_creator = RssCreator()
        
    def test_create_rss_entry(self):
        # Przygotowanie danych testowych
        request = RssRequest(
            title="Test Title",
            description="Test Description",
            content="Test Content",
            timestamp="2024-01-01T12:00:00Z"
        )
        
        # Wywołanie metody
        context = Mock()
        response = self.rss_creator.CreateRssEntry(request, context)
        
        # Sprawdzenie rezultatu
        self.assertIsNotNone(response)
        self.assertIsInstance(response.rss_xml, str)
        self.assertIn("<title>Test Title</title>", response.rss_xml)
        self.assertIn("<description>Test Description</description>", response.rss_xml)
