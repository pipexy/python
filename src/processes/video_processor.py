import grpc
import cv2
import numpy as np
from pipeline_pb2 import VideoRequest, VideoResponse
from pipeline_pb2_grpc import VideoProcessorServicer

class VideoProcessor(VideoProcessorServicer):
    def CreateShortVideo(self, request, context):
        try:
            # Konwersja bytes na numpy array
            nparr = np.frombuffer(request.video_data, np.uint8)
            video = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            # Przetwarzanie wideo (przykład: zmiana rozmiaru)
            processed = cv2.resize(video, (640, 480))
            
            # Konwersja z powrotem do bytes
            _, buffer = cv2.imencode('.mp4', processed)
            video_bytes = buffer.tobytes()
            
            return VideoResponse(
                processed_video=video_bytes,
                format='mp4'
            )
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            raise
