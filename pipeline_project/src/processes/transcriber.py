import grpc
from pipeline_project.src.pipeline_pb2 import AudioRequest, TextResponse
from pipeline_project.src.pipeline_pb2_grpc import TranscriberServicer

class Transcriber(TranscriberServicer):
    def Transcribe(self, request, context):
        try:
            # TODO: Implement actual audio transcription
            # This is a placeholder that returns dummy text
            transcribed_text = "This is a placeholder transcription."
            
            return TextResponse(text=transcribed_text)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            raise
