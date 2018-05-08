# Udacity 猫狗大战毕业项目
## 数据集
训练数据和测试数据下载:
https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition/data

## 使用到的库
- os
- shutil
- numpy
- random
- tqdm
- cv2
- h5py
- pandas
- keras
- sklearn
- matplotlib
- PIL

## 训练所用机器
- CPU:      i7-6700k
- Memory:   16G DDR4 2133
- GPU:      GTX1080

## 操作系统
Ubuntu 16.04 LTS 64位

## 运行时间
### 特征提取时间
- ResNet50:           200s
- InceptionV3:        200s
- Xception:           300s
- DenseNet201:        330s
- InceptionResNetV2:  450s

### 训练时间
- ResNet50,Xception,InceptionV3 merge:            1s/Epoch*8 Epochs
- InceptionResNetV2,Xception,InceptionV3 merge:   1s/Epoch*8 Epochs 

