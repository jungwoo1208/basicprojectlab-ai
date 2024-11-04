import os
import shutil

# 원본 폴더 경로
image_folder = 'C:\\Users\\gjw19\\Downloads\\119.보행 안전을 위한 도로 시설물 데이터\\01.데이터\\2.Validation\\원천데이터\\38. 보행자_계단\\1. 불량'  # 이미지 파일이 있는 폴더 경로
json_folder = 'C:\\Users\\gjw19\\Downloads\\119.보행 안전을 위한 도로 시설물 데이터\\01.데이터\\2.Validation\\라벨링데이터\\VL5\\38. 보행자_계단\\1. 불량'  # JSON 파일이 있는 폴더 경로
output_folder = 'C:\\Users\\gjw19\\OneDrive\\바탕 화면\\기프랩 ai\\data\\15'  # 결과를 저장할 폴더 경로

# 결과 저장 폴더가 없으면 생성
image_output_folder = os.path.join(output_folder, 'images')
json_output_folder = os.path.join(output_folder, 'jsons')

os.makedirs(image_output_folder, exist_ok=True)
os.makedirs(json_output_folder, exist_ok=True)

# 이미지 폴더에서 300개의 파일 선택
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))][:300]

for image_file in image_files:
    # 이미지 파일 경로
    image_path = os.path.join(image_folder, image_file)
    
    # JSON 파일 이름 생성
    json_file = os.path.splitext(image_file)[0] + '.json'  # 같은 이름의 JSON 파일
    json_path = os.path.join(json_folder, json_file)
    
    # 이미지 파일 복사
    shutil.copy(image_path, image_output_folder)

    # JSON 파일이 존재하는지 확인 후 복사
    if os.path.exists(json_path):
        shutil.copy(json_path, json_output_folder)
    else:
        print(f"{json_file} doesn't exist in {json_folder}")

print("파일 복사가 완료되었습니다.")
