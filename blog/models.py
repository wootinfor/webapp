from django.db import models

# Create your models here.

class Article(models.Model):
    #文章的唯一id
    article_id=models.AutoField(primary_key=True)
    #文章标题
    title=models.TextField(null=True)
    #文章摘要
    brief_content=models.TextField(null=True)
    #文章的主要内容
    content=models.TextField(null=True)
    #文章发布日期
    publish_data=models.DateTimeField(auto_now=True)
