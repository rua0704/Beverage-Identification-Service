# 딥러닝을 이용한 classification model 만들기를 공부하고 익숙해져보자.
Training/Validation 데이터셋은 aihub의 '상품 이미지 데이터' 사용  
- Training Data per Class : 114장
- Validation Data per Class : 15장
- Test Data per Class: 약 16장
  
### Highest Accuracy Model
- 10 Classes : Densenet161 (90.90 %)
- 30 Classes : NTS-Net (93.00 %)
  
---
## 1. CNN  
  
---
## 2. TransferLearning using Resnet34  
### V1 - Resnet34의 fc layer 변경
- Class 수 : 10
- Highest Accuracy : 77.92 %
<img width="294" alt="KakaoTalk_20210805_131915289" src="https://user-images.githubusercontent.com/51364769/128291423-e5472fde-f043-4d98-b959-703a6840819e.png">
  
### V2
- Class 수 : 30
- Highest Accuracy : 52.38 %
<img width="294" alt="dt1" src="https://user-images.githubusercontent.com/51364769/128653220-0f40d0c6-d5fd-4715-ab36-46e1fc5bd60e.JPG">
  
---
## 3. TransferLearning using Densenet161  
### V1 - Densenet161의 classifier layer 변경
- Class 수 : 10
- Highest Accuracy : 90.90 %
<img width="294" alt="dt3" src="https://user-images.githubusercontent.com/51364769/128653562-fbe6cba5-c090-4bb0-8a0e-8e0bfdaf1604.JPG">
  
### V2
- Class 수 : 30
- Highest Accuracy : 50.31 %
<img width="294" alt="dt4" src="https://user-images.githubusercontent.com/51364769/128653645-8f5298d3-808e-4705-8ed0-5f3232697097.JPG">
  
---
## 4. TransferLearning using Googlenet  
### V1 - Google의 fc layer 변경
- Class 수 : 10
- Highest Accuracy : 90.25 %
<img width="294" alt="dt7" src="https://user-images.githubusercontent.com/51364769/128653757-421cef09-ec5e-4fa2-a6f5-ea6dd9c05de9.JPG">
  
### V2
- Class 수 : 30
- Highest Accuracy : 67.70 %
<img width="294" alt="dt8" src="https://user-images.githubusercontent.com/51364769/128653868-471f2cbb-4f62-45f4-94ec-7ad74d8d9087.png">
  
---
## 5. NTS-Net
- Class 수 : 30
- Highest Accuracy : 93.0 %

<img width="294" alt="dt8" src="https://user-images.githubusercontent.com/84132245/129306822-5ff825d6-4ad7-433f-925d-9483a5c2655d.png">
<img width="294" alt="dt8" src="https://user-images.githubusercontent.com/84132245/129306812-e25b7e65-ed10-432b-bc8d-89cef69ac767.png">

논문: https://openaccess.thecvf.com/content_ECCV_2018/papers/Ze_Yang_Learning_to_Navigate_ECCV_2018_paper.pdf 


