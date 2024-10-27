import grpc
from pipeline_pb2 import VideoRequest, TextResponse
from pipeline_pb2_grpc import CaptionerServicer
import cv2
import numpy as np

class Captioner(CaptionerServicer):
    def GenerateCaption(self, request, context):
        try:
            # Konwersja bytes na numpy array
            nparr = np.frombuffer(request.video_data, np.uint8)
            video = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            # TODO: Implement actual video captioning
            # This is a placeholder that returns dummy caption
            caption = "A video showing various activities."
            
            return TextResponse(text=caption)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            raise
