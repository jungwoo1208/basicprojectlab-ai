import os
import shutil
import random

# 경로 정의
image_folder = 'C:\\Users\\gjw19\\OneDrive\\바탕 화면\\기프랩 ai\\data\\15\\images'  # 이미지 파일이 있는 폴더 경로
txt_folder = 'C:\\Users\\gjw19\\OneDrive\\바탕 화면\\기프랩 ai\\data\\15\\txt'      # 텍스트 파일이 있는 폴더 경로
output_folder = 'C:\\Users\\gjw19\\OneDrive\\바탕 화면\\기프랩 ai\\dataset'  # 결과를 저장할 루트 폴더 경로 (예: 'coco8')

# train과 val 폴더 내의 이미지와 라벨 폴더 경로
image_train_folder = os.path.join(output_folder, 'images', 'train')
image_val_folder = os.path.join(output_folder, 'images', 'val')
label_train_folder = os.path.join(output_folder, 'labels', 'train')
label_val_folder = os.path.join(output_folder, 'labels', 'val')

# 디렉토리 생성 (없으면 생성)
os.makedirs(image_train_folder, exist_ok=True)
os.makedirs(image_val_folder, exist_ok=True)
os.makedirs(label_train_folder, exist_ok=True)
os.makedirs(label_val_folder, exist_ok=True)

# 이미지 및 텍스트 파일 목록 가져오기
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
txt_files = {os.path.splitext(f)[0]: f for f in os.listdir(txt_folder) if f.lower().endswith('.txt')}

# 이미지 파일을 70%는 train, 30%는 val로 분할
train_images = random.sample(image_files, k=int(len(image_files) * 0.7))
val_images = list(set(image_files) - set(train_images))

# 파일 복사 함수 정의
def copy_files(image_list, image_dest, label_dest):
    for image_file in image_list:
        # 이미지 파일 복사
        image_path = os.path.join(image_folder, image_file)
        shutil.copy(image_path, os.path.join(image_dest, image_file))

        # 대응되는 라벨 파일이 있으면 복사
        txt_file_name = os.path.splitext(image_file)[0]  # 확장자 제거한 파일 이름
        if txt_file_name in txt_files:
            txt_path = os.path.join(txt_folder, txt_files[txt_file_name])
            shutil.copy(txt_path, os.path.join(label_dest, txt_files[txt_file_name]))  # 파일 이름이 올바르게 사용되었는지 확인

# train과 val 이미지 및 라벨 복사
copy_files(train_images, image_train_folder, label_train_folder)
copy_files(val_images, image_val_folder, label_val_folder)

print("파일이 성공적으로 정리되었습니다.")
