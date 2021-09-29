## Fine-grained Classification 관련 논문 서치 및 요약본 업로드  
  
### 1. 논문명 : Learning to navigate for fine-grained Classification
 - Navigator: 모델의 초점을 가장 유용한 영역에 맞춤. 이미지의 각 영역에 대해 영역이 얼마나 유용한지 예측하고 예측은 가장 유용한 영역 제안
 - Teacher: Navigaotor가 제안한 지역 평가, 피드백 제공 ground-truth class에 속하는 확률 평가, 신뢰도 평가는 손실함수로 더 많은 정보를 제공할 수 있도록 함
 - Scrutinizer: Navigator에서 제안된 영역 면밀히 조사
* 새로운 손실함수 제안


논문 목차
#####  1. Introduction
#####  2. Related Work(Fine-grained classification, Object detection, Learning to Rank)
#####  3. Methods(Approach Overview,  Navigator and Teacher,  Scrutinizer, Network Architecture, Loss function and Optimization)
#####  4. Experiments
  
### 2. 논문명 : Object Detection using Fine-grained Feature Extraction and Localization  
  
### 3. 논문명 : A coarse-to-fine capsule network for fine-grained image categorization  
Uses coarse-to-fine Capsule Network (CTS-CapsNet) arranged in Region Proposal Network (RPN) that works in multiple scales. 
Expert CapsNet overal pipeline: 
- multi-scale convolutional layer (MS-CONV)
- primary capsules layer (PrimCaps)
- entity capsules layer 
- DropConnect layer
- Decoder layer

### 4. 논문명 : Dynamic Routing Between Capsules
- Capsule
- CapsNet
- Dynamic Routing

### 5. NTS-net 요약
