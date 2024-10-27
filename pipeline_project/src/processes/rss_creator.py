import grpc
from pipeline_project.src.pipeline_pb2 import RssRequest, RssResponse
from pipeline_project.src.pipeline_pb2_grpc import RssCreatorServicer
from datetime import datetime

class RssCreator(RssCreatorServicer):
    def CreateRssEntry(self, request, context):
        try:
            # Create RSS XML entry
            rss_xml = f"""
            <item>
                <title>{request.title}</title>
                <description>{request.description}</description>
                <content>{request.content}</content>
                <pubDate>{request.timestamp}</pubDate>
            </item>
            """
            
            return RssResponse(rss_xml=rss_xml)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            raise
