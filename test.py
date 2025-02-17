import cv2
import random
from ultralytics import YOLO

# Load the YOLO model
model = YOLO('C:\\Users\\gjw19\\OneDrive\\바탕 화면\\기프랩 ai\\basicprojectlab-ai\\train_experiment11\\weights\\best.pt') 

# Label map for classes in Korean
label_map = {
    1: "스테인리스 볼라드", 2: "탄성 고무 볼라드", 3: "유도 표지판 (2줄)", 4: "유도 표지판 (3줄)",
    5: "보행자 안전 울타리", 6: "점자 블록", 7: "보도 (시멘트 콘크리트)", 8: "보도블록", 9: "자전거 도로",
    10: "맨홀", 11: "횡단보도", 12: "소화전", 13: "고정식 부착식 표지", 14: "통합 표지",
    15: "보행자 계단"
}


# Load image
image_path = 'C:\\Users\\gjw19\\Downloads\\KakaoTalk_20241104_203829189_02.jpg'
image = cv2.imread(image_path)

# Perform object detection
results = model(image)

# Annotate detected objects
for result in results:
    boxes = result.boxes.xyxy.numpy()  # Bounding box coordinates
    confidences = result.boxes.conf.numpy()  # Confidence scores
    class_ids = result.boxes.cls.numpy()  # Class IDs

    for box, conf, class_id in zip(boxes, confidences, class_ids):
        # Generate random color
        color = [int(c) for c in random.choices(range(256), k=3)]
        
        # Box coordinates
        xmin, ymin, xmax, ymax = map(int, box)

        # Draw bounding box
        cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color, 2)
        
        # Prepare label with class name and confidence
        label = f'{label_map.get(int(class_id), "Unknown")}: {conf:.2f}'
        cv2.putText(image, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
        # Print detected object's details
        print(f"Detected: {label_map.get(int(class_id), 'Unknown')} - Confidence: {conf:.2f} - Box: {xmin}, {ymin}, {xmax}, {ymax}")

# Save and display the annotated image
cv2.imwrite('annotated_image.jpg', image)
cv2.imshow('YOLOv8 Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

