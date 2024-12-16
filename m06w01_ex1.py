import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import streamlit as st
from PIL import Image
import torchvision.transforms as transforms


class LeNetClassifier(nn.Module):
    def __init__(self, num_classes):
        super(LeNetClassifier, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1,
                               out_channels=6,
                               kernel_size=5,
                               stride=1,
                               padding='same')
        self.avgpool1 = nn.AvgPool2d(kernel_size=2)
        self.conv2 = nn.Conv2d(in_channels=6,
                               out_channels=16,
                               kernel_size=5,
                               stride=1,
                               padding='same')
        self.avgpool2 = nn.AvgPool2d(kernel_size=2)
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(7*7*16, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, num_classes)

    def forward(self, x):
        out = self.conv1(x)
        out = self.avgpool1(out)
        out = F.relu(out)

        out = self.conv2(out)
        out = self.avgpool2(out)
        out = F.relu(out)

        out = self.flatten(out)
        out = self.fc1(out)
        out = self.fc2(out)
        out = self.fc3(out)
        return out


@st.cache_resource
def load_model(model_path, num_classes=10):
    lenet_model = LeNetClassifier(num_classes)
    lenet_model.load_state_dict(torch.load(model_path, weights_only=True,
                                           map_location=torch.device('cpu')))
    lenet_model.eval()
    return lenet_model


model = load_model('best_model.pt')


def inference(image, model):
    w, h = image.size

    # Khởi tạo image_transforms luôn nằm ngoài khối if
    image_transforms = transforms.Compose([
        transforms.Grayscale(),
        transforms.Resize(28),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.1307], std=[0.3081])
    ])

    # Cắt ảnh nếu không vuông
    if w != h:
        crop = transforms.CenterCrop(min(w, h))
        image = crop(image)

    # Áp dụng transform
    img_new = image_transforms(image)
    img_new = img_new.expand(1, 1, 28, 28)

    # Dự đoán với mô hình
    with torch.no_grad():
        predictions = model(img_new)
    preds = nn.Softmax(dim=1)(predictions)
    p_max, yhat = torch.max(preds.data, 1)
    return p_max.item() * 100, yhat.item()


def main():
    st.title('Digit Recognition')
    st.subheader('Model: LeNet. Dataset: MNIST')
    option = st.selectbox('How would you like to give the input?',
                          ('Upload Image File', 'Run Example Image'))
    if option == "Upload Image File":
        file = st.file_uploader(
            "Please upload an image of a digit", type=["jpg", "png"])
        if file is not None:
            image = Image.open(file)
            p, label = inference(image, model)
            st.image(image)
            st.success(f"The uploaded image is of the digit {
                       label} with {p:.2f} % probability.")

    elif option == "Run Example Image":
        image = Image.open('demo_8.png')
        p, label = inference(image, model)
        st.image(image)
        st.success(f"The image is of the digit {
                   label} with {p:.2f} % probability.")


if __name__ == '__main__':
    main()
