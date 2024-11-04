from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import cv2
from ultralytics import YOLO

app = Flask(__name__)
CORS(app)  # CORS 활성화

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# YOLO 모델 로드
#모델 위치는 자신의 경로에 맞게 설정
model = YOLO('C:\\Users\\gjw19\\OneDrive\\바탕 화면\\기프랩 ai\\train_experiment11\\weights\\best.pt')

# 클래스 이름 매핑 (한국어)
label_map = {
    1: "스테인리스 볼라드", 2: "탄성 고무 볼라드", 3: "유도 표지판 (2줄)", 4: "유도 표지판 (3줄)",
    5: "보행자 안전 울타리", 6: "점자 블록", 7: "보도 (시멘트 콘크리트)", 8: "보도블록", 9: "자전거 도로",
    10: "맨홀", 11: "횡단보도", 12: "소화전", 13: "고정식 부착식 표지", 14: "통합 표지",
    15: "보행자 계단"
}


# 이미지 감지를 위한 엔드포인트
@app.route('/detect', methods=['POST'])
def classify_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # 파일 저장 경로
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # 이미지 로드
    image = cv2.imread(filepath)

    # 객체 감지 수행
    results = model(image)
    detected_classes = set()  # 중복된 클래스 제거를 위해 set 사용

    for result in results:
        boxes = result.boxes.xyxy.numpy()  # 바운딩 박스 좌표
        class_ids = result.boxes.cls.numpy()  # 클래스 ID

        for class_id in class_ids:
            detected_classes.add(label_map.get(int(class_id), "Unknown"))

    # 리스트로 변환
    detected_classes = list(detected_classes)
    print('Detected classes:', detected_classes)

    return jsonify({'detected_class': detected_classes}), 200


if __name__ == '__main__':
    app.run(debug=True)
