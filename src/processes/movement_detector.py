from pipeline_pb2 import ImageRequest, DetectionResponse, Detection, BoundingBox
from pipeline_pb2_grpc import MovementDetectorServicer
import cv2
import numpy as np

class MovementDetector(MovementDetectorServicer):
    def __init__(self):
        self.previous_frame = None
        
    def DetectMovement(self, request, context):
        try:
            # Konwersja bytes na numpy array
            nparr = np.frombuffer(request.image_data, np.uint8)
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            if self.previous_frame is None:
                self.previous_frame = frame
                return DetectionResponse(detections=[])
            
            # Obliczenie różnicy między klatkami
            diff = cv2.absdiff(frame, self.previous_frame)
            gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
            blur = cv2.GaussianBlur(gray, (5, 5), 0)
            _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
            dilated = cv2.dilate(thresh, None, iterations=3)
            
            # Znalezienie konturów
            contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            
            # Tworzenie detekcji
            detections = []
            for contour in contours:
                if cv2.contourArea(contour) > 1000:
                    x, y, w, h = cv2.boundingRect(contour)
                    detections.append(Detection(
                        confidence=0.95,
                        bbox=BoundingBox(x=x, y=y, width=w, height=h),
                        class_name="movement"
                    ))
            
            self.previous_frame = frame
            return DetectionResponse(detections=detections)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            raise
