from time import timezone

from django.shortcuts import render
from django.template import Context
from ..models import Closet, Musinsa_Closet, preferences, codi_clothes
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required

from user.aws_settings import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME, REGION, CLOUD_FRONT
import boto3
from io  import BytesIO
from PIL import Image

import numpy as np
#import cv2
from yolov5 import detect
from yolov5.cloth_style_update import extract_color
import os
import urllib
from yolov5.utils.plots import output_to_target
from django.core.files.storage import FileSystemStorage
import random
import sqlite3
from recommendation.recommendation import recommendation
#from simirarity.import_data import database


def musinsa_closet_data(obj):
    data = []
    data.append(obj.clothesId)
    data.append(obj.fit)
    data.append(obj.closet_color)
    data.append(obj.closet_style)
    data.append(obj.spring)
    data.append(obj.summer)
    data.append(obj.autumn)
    data.append(obj.winter)
    data.append(obj.subCategory )
    data.append(obj.mainCategory)
    return data



def preference_data(obj):
    data = []
    data.append(obj.userId)
    data.append(obj.codiId_id)
    return data

def codi_clothes_data(obj):
    data = []
    data.append(obj.codi_Id_id)
    data.append(obj.clothesId_id)

    return data



# 추천 페이지
@login_required(login_url='login:login')
def detail(request, author_user, closet_id):
    Closet.author = author_user
    closet = get_object_or_404(Closet, pk=closet_id)
    
    recommend_list = [] 
    #db = database('../db.sqlite3.db')
    input_obj = [
        Musinsa_Closet.objects.only(
            'clothesId', 'fit', 'closet_color', 'closet_style', 
            'spring', 'summer', 'autumn', 'winter', 'subCategory', 'mainCategory'), 
        preferences.objects.only('userId', 'codiId_id'), 
        codi_clothes.objects.only('codi_Id_id', 'clothesId_id')]
    
    input_data = []
    input_data.append([musinsa_closet_data(obj) for obj in input_obj[0]])
    input_data.append([preference_data(obj) for obj in input_obj[1]])
    input_data.append([codi_clothes_data(obj) for obj in input_obj[2]])
    user_selection = Closet.objects.filter(closet_id=closet_id)[0]
    #print(user_selection.closet_spring)
    user_clothes = {
        'clothesId': closet_id,
        'fit': user_selection.closet_fit,
        'color': user_selection.closet_color,
        'style': user_selection.closet_style,
        'spring': user_selection.closet_spring,
        'summer': user_selection.closet_summer,
        'autumn': user_selection.closet_fall,
        'winter': user_selection.closet_winter,
        'subCategory': user_selection.closet_sub_category,
        'mainCategory': user_selection.closet_main_category
    }
    clotheses = recommendation(author_user, input_data, user_clothes)
    #clotheses=[407344, 407344,407344]
    #print(user_clothes.values())
    #print(f'user_id: {author_user}')
    print(clotheses)
    for clothes in clotheses:
        recommend_list.append(Musinsa_Closet.objects.filter(clothesId=clothes)[0])   
    
    if user_clothes['mainCategory'] == '상의' or user_clothes['mainCategory'] == '아우터':
        categroies = ['스커트', '바지']
    else:
        categroies = ['상의', '아우터']
    my_recommend_list = []
    my_recommend_list.extend(Closet.objects.filter(closet_main_category = categroies[0]))
    my_recommend_list.extend(Closet.objects.filter(closet_main_category = categroies[1]))
    # recommendations = []
    # for recommend in recommend_list:
    #     recommendations.append([
    #         recommend.imgUrl,
    #         f"https://www.musinsa.com/app/goods/{recommend.clothesId}"
    #     ])
    # context = {}
    # for i, recommend in enumerate(recommendations):
    #     context[f'img{i}'] = recommend[0]
    #     context[f'url{i}'] = recommend[1]
    # print(context)
    context = {
        'closet' : closet,
        'recommend_list' : recommend_list,     
        'my_recommend_list' : my_recommend_list
        # 'recommend_list_1' : recommend_list_1,      
        # 'recommend_list_2' : recommend_list_2,       
        # 'recommend_list_3' : recommend_list_3,       
    }
    
    return render(request, 'closet/closet_detail.html', context)


# 상의 등록
@login_required(login_url='login:login')
def closet_create(request, author_user):

    if request.method == "POST":        

        closet_top_title = request.POST["closet_title"]     
        image = request.FILES['closet_uploadedFile']  # 이미지 (title.jpg)
        sub = request.POST['sub']
        fit = request.POST['closet_fit']
        #section = '1'   # 상의 카테고리

        #top = request.POST["top"]        
        
        closet_spring = request.POST.get('closet_spring',False)
        if closet_spring == "on":
            closet_spring = True
        
        closet_summer = request.POST.get('closet_summer',False)
        if closet_summer == "on":
            closet_summer = True
            
        closet_fall = request.POST.get('closet_fall',False)
        if closet_fall == "on":
            closet_fall = True
            
        closet_winter = request.POST.get('closet_winter',False)
        if closet_winter == "on":
            closet_winter = True

        user = str(request.user)    # user.id       
        
        # s3 이미지 업로드
        bucket_name = BUCKET_NAME
        region = REGION
        
        num = random.randrange(1, 99999)
        image_type = (image.content_type).split("/")[1]
        image_name = user + '/top-' + str(num) + "." + image_type
        image_uri = CLOUD_FRONT
        image_url = image_uri + image_name
        # image_url = "https://"+ bucket_name + '.s3.' + region + '.amazonaws.com/' + image_name  # 업로드된 이미지의 url이 설정값으로 저장됨
        #image_url = "https://"+ bucket_name + '.s3.' + region + '.amazonaws.com/' + user +'/'+ closet_top_title +"."+image_type  # 업로드된 이미지의 url이 설정값으로 저장됨

        im = Image.open(image)   # 추가
        buffer = BytesIO()
        im.save(buffer, image_type)
        buffer.seek(0)
        
        s3_client = boto3.client(
                's3',
                aws_access_key_id = AWS_ACCESS_KEY_ID,
                aws_secret_access_key = AWS_SECRET_ACCESS_KEY
            )
        
        s3_client.upload_fileobj(
            buffer,
            bucket_name, # 버킷이름
            image_name,
            ExtraArgs = {
                "ContentType" : image.content_type
            }
        )
        
        extract_images_info = detect.run(weights = 'yolo\\best.pt',
                        source = str(image_url),
                        #source = 'media\\images\\3.jpg',
                        data = 'yolov5\\data\\data.yaml',
                        conf_thres = 0.3,
                        line_thickness = 4,
                        project = 'media\\detect',
                        view_img = False)
        
        # 스타일, 색상 추출 모델
        items_to_list = list(extract_images_info.items())
        save_list = []
        for key, value in items_to_list: # key : 이미지 경로 value[0] 스타일 value[1] 사각형좌표
            if value:
                style = value[0]   # per image
                color, test_image = extract_color(key, value)   # per image 
                save_list.append({'image_path':key, 'style':style, 'color':color})
            else:
                save_list.append({'image_path':key, 'style':'', 'color':''})
        print(save_list)
        
        if save_list[0]['style'] == '':
            s3_client.delete_object(Bucket=bucket_name, Key=image_name) # 이미지 삭제
        
        else:
            pil_image = Image.fromarray(test_image)
            buffer = BytesIO()
            #print(pil_image)
            #im = Image.open(pil_image)   # 잘린이미지
            # image_l = img_trim.tobytes()
            # image_l.save(image_type)
            #pil_image.save('media/test.jpg',image_type)
            pil_image.save(buffer, image_type)
            buffer.seek(0)

            s3_client.upload_fileobj(
                buffer,
                bucket_name, # 버킷이름
                image_name,
                ExtraArgs = {
                    "ContentType" : image.content_type
                }
            )
            
            #num = random.randrange(1, 99999)
            #image_name = user + closet_top_title + str(num) +"." + image_type
            #image_url = "https://"+ bucket_name + '.s3.' + region + '.amazonaws.com/' + image_name  # 업로드된 이미지의 url이 설정값으로 저장됨
            
            # Saving the information in the database
            closet_top = Closet(
                author = request.user,   # author_id 속성에 user.id 값 저장
                closet_title = closet_top_title,               
                closet_url = image_url,

                closet_main_category = '상의',
                closet_sub_category = sub,
                closet_spring = closet_spring,
                closet_summer = closet_summer,
                closet_fall = closet_fall,
                closet_winter = closet_winter,
                closet_fit = fit,
                #color_style = request.POST[save_list[0][style]],
                #closet_color = request.POST[save_list[0][color]],    
                closet_style = save_list[0]['style'], #스타일 저장
                closet_color = save_list[0]['color'], #색 저장
            )        
            closet_top.save()
            

        #image_url = "https://"+ bucket_name + '.s3.' + region + '.amazonaws.com/' + user +'/'+ closet_top_title +"."+image_type  # 업로드된 이미지의 url이 설정값으로 저장됨

        #im     = Image.open(image)   # 추가
        #buffer = BytesIO()
        #im.save(buffer, image_type)
        #buffer.seek(0)
        
        # Saving the information in the database     
        # closet_top = Closet(
        #     closet_title = closet_top_title,
        #     # closet_top_url = image_url,
        #     closet_url = image_url,
        #     author = request.user,   # author_id 속성에 user.id 값 저장
        #     # author = author_user <-- 에러
        # )        
        # closet_top.save()

        # s3_client = boto3.client(
        #         's3',
        #         aws_access_key_id = AWS_ACCESS_KEY_ID,
        #         aws_secret_access_key = AWS_SECRET_ACCESS_KEY
        #     )
        
        # s3_client.upload_fileobj(
        #     buffer,
        #     bucket_name, # 버킷이름
        #     user +'/'+ closet_top_title+"."+image_type,
        #     ExtraArgs = {
        #         "ContentType" : image.content_type
        #     }
        # )

    closet_top = Closet.objects.all()
    context = { "closet": closet_top }
    return render(request, "closet/closet_form_top.html", context) 


