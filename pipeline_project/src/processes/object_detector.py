import grpc
from pipeline_project.src.pipeline_pb2 import ImageRequest, ObjectsResponse
from pipeline_project.src.pipeline_pb2_grpc import ObjectDetectorServicer
import cv2
import numpy as np

class ObjectDetector(ObjectDetectorServicer):
    def DetectObjects(self, request, context):
        try:
            # Konwersja bytes na numpy array
            nparr = np.frombuffer(request.image_data, np.uint8)
            image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            # TODO: Implement actual object detection using a model
            # This is a placeholder that returns dummy objects
            detected_objects = ["person", "car", "dog"]
            
            return ObjectsResponse(objects=detected_objects)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            raise
