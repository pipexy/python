import grpc
from pipeline_project.src.pipeline_pb2 import ImageRequest, DetectionResponse, Detection, BoundingBox
from pipeline_project.src.pipeline_pb2_grpc import MovementDetectorServicer
import cv2
import numpy as np

class MovementDetector(MovementDetectorServicer):
    def __init__(self):
        self.previous_frame = None
        
    def DetectMovement(self, request, context):
        try:
            # Convert bytes to numpy array
            nparr = np.frombuffer(request.image_data, np.uint8)
            current_frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            # For the first frame, just store it and return no detections
            if self.previous_frame is None:
                self.previous_frame = current_frame
                return DetectionResponse(detections=[])
            
            # TODO: Implement actual movement detection
            # This is a placeholder that returns no detections
            detections = []
            
            # Update previous frame
            self.previous_frame = current_frame
            
            return DetectionResponse(detections=detections)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            raise
