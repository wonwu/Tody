
# TODY : 융복합 팀프로젝트_식스센스

## 1. 프로젝트 개요
- AI 기반 디지털 옷장, 나만의 코디네이터 서비스

## 2. 기능
1. 사용자 맞춤 코디 추천 : 카테고리, 스타일, 색상 맞춤 코디 추천
    - 카테고리
        - 상의 : 블라우스, 티셔츠, 니트, 후드티
        - 하의 : 청바지, 팬츠, 스커트, 레깅스, 조거팬츠
        - 아우터 : 코트, 재킷, 점퍼, 패딩, 베스트, 가디건, 집업
    - 스타일 : 내추럴 / 캐주얼 / 페미닌 / 트래디셔널 / 스포티 / 젠더리스 / 서브컬쳐 / 매니시 / 에스닉 / 컨템포러리 중 분류

2. 쇼핑몰 구매 링크 제공
    - 추천된 코디 링크를 제공하여 제품 구매를 원하는 경우 상세 페이지로 이동
3. 디지털 옷장
    - 사용자 현재 가지고 있는 옷을 웹에서 확인
4. 습도 알림 및 제어
    - 사용자 옷장의 습도가 55% 이상일 경우, 사용자에게 알림 및 제습기 작동

## 3. 구성도

![aws_architecture](https://github.com/wonwu/Tody/blob/master/cloud/aws_architecture.png)
- 그림1. 클라우드 AWS architecture 

![project_architecture](https://github.com/wonwu/Tody/blob/master/cloud/project_architecture2.png)
- 그림2. 전체 프로젝트 architecture 


## 4. 역할
- AI : 모델링, 데이터 전처리, 라벨링, 색 추출 알고리즘
- BD : 무신사 데이터 크롤링, 전처리, 라벨링, 추천 시스템 구현
- IoT : 웹 인터페이스, Raspberry Pi 연동
- Cloud : 클라우드 인프라 구축, DB 설계, 웹 방화벽 구축


## 5. 구현 기술
 ### 1) Kubernetes Service
 - SVC, Deployment, Statefulset, Secret, ConfigMap, Cronjob, Namespace, HPA 
 
 ### 2) AWS 
 - ECR
 - ACM
 - AWS WAF
 - Amazon CloudWatch
 - ELB
 - AWS Lambda
 - AWS IoT Core
 - Amazon SNS
 - Amazon S3
 - Amazon CloudFront
 - Amazon RDS
 - Amazon EC2
 - Amazon EKS
 - Route53

 ### 3) Github
 - GithubAction을 활용한 CI/CD 

 ### 4) Web Server
 - nginx

 ### 5) WAS (Web Application Server)
 - django 
  
