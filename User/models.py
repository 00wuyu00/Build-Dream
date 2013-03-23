# -*- coding: utf-8 -*-
from django.db import models
    
# Create your models here.
#
Direction_CHOICES = (
    ('T', 'Type'),
    ('L', 'Language'),
)  
class Image(models.Model):
    description=models.CharField(max_length=999)
    address=models.FilePathField()
    flag=models.BooleanField()#是否为标志
    
class Direction(models.Model): 
    name=models.CharField(max_length=20)
    type=models.CharField(max_length=1,choices=Direction_CHOICES)
    
class User(models.Model):
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField()
    grade=models.IntegerField(max_length=2)
    phone=models.CharField(max_length=11)
    student_id=models.CharField(max_length=14)
    good_direction=models.ManyToManyField(Direction,related_name="good_direction")
    follow_direction=models.ManyToManyField(Direction,related_name="follow_direction")
    introduction=models.CharField(max_length=100)
    image=models.ForeignKey(Image,null=True)
    
class Case(models.Model):
    time=models.DateTimeField()#事件发生时间
    description=models.CharField(max_length=999)#事件描述
    level=models.SmallIntegerField()#事件严重等级
        
Level_CHOICES=(
('a','院级'),
('s','校级'), 
('n','国家级'),
('w','世界级'),
)   
class Competition(models.Model):
    name=models.CharField(max_length=100)
    level=models.CharField(max_length=1,choices=Level_CHOICES)
    project_type=models.ManyToManyField(Direction)
    #Begin_time=models.DateTimeField() 先考虑可行性
    #End_time=models.DateTimeField()先考虑可行性
    description=models.CharField(max_length=999)
    #process_set 获得流程事件
    website=models.URLField()#比赛网址
    flag_process=models.BooleanField()

class New(models.Model):
    title=models.CharField(max_length=99)
    time=models.DateTimeField()
    content=models.CharField(max_length=999)
    author=models.CharField(max_length=10)
    times=models.IntegerField()
    
    



    