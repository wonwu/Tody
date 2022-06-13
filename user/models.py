from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from datetime import datetime


# sub_categories = (
#     (0, '기타'), (1, '셔츠/블라우스'), (2, '민소매 티셔츠'), (3, '기타 상의'), (4, '반소매 티셔츠'), 
#     (5, '피케/카라 티셔츠'), (6, '긴소매 티셔츠'), (7, '맨투맨/스웨트셔츠'), (8, '후드 티셔츠'), (9, '니트/스웨터'), 
#     (10, '숏 팬츠'), (11, '점프 슈트/오버올'), (12, '데님 팬츠'), (13, '코튼 팬츠'), (14, '슈트 팬츠/슬랙스'), (15, '기타 바지'), 
#     (16, '트레이닝/조거 팬츠'), (17, '레깅스'),  (18, '미디스커트'), (19, '롱스커트'), (20, '미니스커트'), (21, '롱스커트'), 
#     (22, '플리스/뽀글이'), (23, '기타 아우터'), (24, '베스트'), (25, '슈트/블레이저 재킷'), (26, '카디건'), (27, '숏패딩/숏헤비 아우터'), 
#     (28, '나일론/코치 재킷'), (29, '환절기 코트'), (30, '롱패딩/롱헤비 아우터'), (31, '트러커 재킷'), (32, '겨울 더블 코트'), 
#     (33, '겨울 기타 코트'), (34, '겨울 싱글 코트'), (35, '무스탕/퍼'), (36, '트레이닝 재킷'), (37, '사파리/헌팅 재킷'), 
#     (38, '패딩 베스트'), (39, '스타디움 재킷'), (40, '아노락 재킷'), (41, '레더/라이더스 재킷'), (42, '원피스')
#     )    

class Closet(models.Model): #옷장모델

    closet_id = models.BigAutoField(primary_key=True) 
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    closet_title = models.CharField(max_length=200) #제목
    closet_url = models.CharField(max_length=300) #s3 url
    closet_create_date = models.DateTimeField(auto_now = True) #날짜
    closet_uploadedFile = models.ImageField(upload_to='images/', blank=True, null=True)#사진추가   

    closet_main_category =  models.CharField(max_length=20, default='')
    #closet_outer_category = ( (1,'Coat'), (2,'Jacket'), (3,'Jumper'), (4,'Padding'), (5,'Best'), (6,'Cardigan '), (7,'Zip-Up'))
    #sub_section = sub_categories
    closet_sub_category =  models.TextField(max_length=20, default='')
    

    closet_spring = models.BooleanField(default = True)
    closet_summer = models.BooleanField(default = True)
    closet_fall = models.BooleanField(default = True)
    closet_winter = models.BooleanField(default = True)

    
    closet_color = models.CharField(max_length=100,default='')
    closet_style = models.CharField(max_length=100, default='')
    closet_fit = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)

    #section = ((1, 'Top'),(2,'Pants'),(3, 'Outer'),(4, 'Onepiece'))
    

    def __str__(self):
        return self.closet_title


class Musinsa_Closet(models.Model):
    clothesId = models.IntegerField( primary_key= True )
    closet_title = models.CharField(max_length=200, default='')
    imgUrl = models.CharField(max_length=50, default='')
    closet_maincategory = ((1, 'Top'),(2,'Pants'),(3, 'Outer'),(4, 'Onepiece'))
    mainCategory =  models.TextField(max_length=20, choices = closet_maincategory, default='')
    subCategory =  models.TextField(max_length=20, default='')
    #closet_top_category = ( (0,'no'),(1,'Blouse'), (2,'T-shirt'), (3,'Knit'), (4,'Hoodie' ) )
    #top =  models.TextField(max_length=20, choices = closet_top_category, default='0')
    #closet_pants_category = ( (0,'no'),(1,'Blue jeans'), (2,'Pants'), (3,'Skirt'), (4,'Leggings'), (5,'Jogger pants') )
    #pants =  models.TextField(max_length=20, choices = closet_pants_category, default='0')
    #closet_onepiece_category = ((0,'no'),(1,'onepiece'),(2,'twopiece'))
    #onepiece =  models.TextField(max_length=20, choices = closet_onepiece_category, default='0')
    
    closet_style = models.CharField(max_length=100, default='')
    closet_color = models.CharField(max_length=100,default='')
    barndName = models.CharField(max_length=50, default ='' )
    spring = models.BooleanField(default = True)
    summer = models.BooleanField(default = True)
    autumn = models.BooleanField(default = True)
    winter = models.BooleanField(default = True)
    fit = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(9)], default = 1)
    elasticity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)
    transparency = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)
    thickness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)
    texture = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1, null=True)
    price = models.IntegerField(default=1, null=True)
    ragisterDate = models.DateTimeField(max_length=200, default='')

class codi(models.Model):
    codiId = models.IntegerField(primary_key=True)
    # codiId = models.OneToOneField(codi_clothes,on_delete=models.CASCADE, primary_key=True)
    # codiId = models.ManyToManyField(codi_clothes,on_delete=models.CASCADE, primary_key=True)
    coditype = models.CharField( max_length=10, default='')
    codiUrl = models.CharField( max_length=100, default='')
    codiStyle = models.CharField( max_length=10, default='')
    registerDate = models.DateField(datetime.now)
    

# 무신사 클로젯
class codi_clothes(models.Model):
    cId = models.IntegerField( primary_key=True)
    codi_Id = models.ForeignKey(codi,on_delete=models.CASCADE, default= '')
    clothesId = models.ForeignKey(Musinsa_Closet, on_delete=models.CASCADE ,default='')
    regDate = models.DateField(datetime.now)


class preferences(models.Model):
    preferences_id1= models.IntegerField( primary_key=True )
    #userId = models.ForeignKey(User, on_delete=models.CASCADE, null=True,  default= '')
    userId = models.IntegerField(default='')
    codiId = models.ForeignKey(codi,on_delete=models.CASCADE, default= '')
    ratingDate = models.DateField(datetime.now)