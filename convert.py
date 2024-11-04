import json
import os

def convert_to_yolo_format(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.json'):
            input_json = os.path.join(input_folder, filename)
            output_txt = os.path.join(output_folder, filename.replace('.json', '.txt'))

            with open(input_json, 'r', encoding='utf-8') as f:
                data = json.load(f)

            image_width = data['info']['width']
            image_height = data['info']['height']

            with open(output_txt, 'w', encoding='utf-8') as out_file:
                for annotation in data['annotations']:
                    label_id = 15  # 클래스 ID
                    annotation_type = annotation['annotation_type']

                    if annotation_type == 'bbox':
                        bbox = annotation['annotation_info'][0]
                        left = bbox[0]
                        top = bbox[1]
                        width = bbox[2]
                        height = bbox[3]

                        x_center = (left + (width / 2)) / image_width
                        y_center = (top + (height / 2)) / image_height
                        yolo_format = f"{label_id} {x_center} {y_center} {width / image_width} {height / image_height}\n"
                        out_file.write(yolo_format)

                    elif annotation_type == 'polygon':
                        points = annotation['annotation_info']
                        xs = [point[0] for point in points]
                        ys = [point[1] for point in points]

                        left = min(xs)
                        top = min(ys)
                        right = max(xs)
                        bottom = max(ys)
                        width = right - left
                        height = bottom - top

                        x_center = (left + (width / 2)) / image_width
                        y_center = (top + (height / 2)) / image_height
                        yolo_format = f"{label_id} {x_center} {y_center} {width / image_width} {height / image_height}\n"
                        out_file.write(yolo_format)

            print(f"{filename} 파일이 YOLO 형식으로 변환 완료: {output_txt}")


input_folder = 'C:\\Users\\gjw19\\OneDrive\\바탕 화면\\기프랩 ai\\data\\15\\jsons'  # JSON 파일이 있는 폴더 경로
output_folder = 'C:\\Users\\gjw19\\OneDrive\\바탕 화면\\기프랩 ai\\data\\15\\txt'  # 변환된 파일을 저장할 폴더 경로
convert_to_yolo_format(input_folder, output_folder)
