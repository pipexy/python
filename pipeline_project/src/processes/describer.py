import grpc
from pipeline_project.src.pipeline_pb2 import ContentRequest, TextResponse
from pipeline_project.src.pipeline_pb2_grpc import DescriberServicer

class Describer(DescriberServicer):
    def GenerateDescription(self, request, context):
        try:
            # TODO: Implement actual content description generation
            # This is a placeholder that returns dummy description
            description = f"Description of content: {request.content[:100]}..."
            
            return TextResponse(text=description)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            raise
