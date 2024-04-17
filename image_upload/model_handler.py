import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

class_names = {
    0: "바게트빵",
    1: "베이글",
    2: "베이글 샌드위치",
    3: "BLT 샌드위치",
    4: "보리빵",
    5: "브라우니",
    6: "참치 샌드위치",
    7: "치즈빵",
    8: "초코 케이크",
    9: "초코 머핀",
    10: "크루아상",
    11: "당근 케이크",
    12: "도넛",
    13: "에그 타르트",
    14: "고로케",
    15: "햄치즈 샌드위치",
    16: "햄 샌드위치",
    17: "호두파이",
    18: "호밀빵",
    19: "잡곡식빵",
    20: "쨈빵",
    21: "케이크",
    22: "마들렌",
    23: "머핀",
    24: "파니니",
    25: "프레즐",
    26: "프렌치 토스트",
    27: "빵",
    28: "롤 케이크",
    29: "샌드위치",
    30: "생크림 케이크",
    31: "사과파이",
    32: "찐빵",
    33: "슈크림",
    34: "토스트",
    35: "통밀빵"
}

# 모델을 불러오는 함수
def load_model(model_path, num_classes):
    model = models.resnet50(pretrained=False)
    num_ftrs = model.fc.in_features
    model.fc = nn.Linear(num_ftrs, num_classes)
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()
    return model

# 이미지 전처리 함수
def preprocess_image(image_file):
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    image = Image.open(image_file)
    image_tensor = preprocess(image)
    return image_tensor

# 이미지로부터 예측을 얻는 함수
def get_prediction_from_image(image_tensor, model_path, num_classes, topk=5):
    model = load_model(model_path, num_classes)  # 모델을 불러옵니다.
    with torch.no_grad():
        outputs = model(image_tensor.unsqueeze(0))
        _, predicted = torch.max(outputs, 1)
    predicted_name = class_names[predicted.item()]
    top_probs, top_classes = torch.topk(outputs, topk)

    print("Top classes indices:", top_classes)
    print("Top classes names:", [class_names[idx.item()] for idx in top_classes[0]])

    top_predictions = []
    for i in range(topk):
        class_name = class_names[top_classes[0][i].item()]
        probability = top_probs[0][i].item()
        top_predictions.append((class_name, probability))

    return predicted_name, top_predictions

model_path = r'C:\PYWork\myproject10\image_upload\data\resnet50 model.pth'
num_classes = 36
