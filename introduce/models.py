from django.db import models

# Create your models here.
class AccessLog(models.Model):
    """
    1. default : 기본적으로 사용될 날짜를 사용자가 지정
    2. auto_now : 데이터가 수정 될 때마다 갱신됨
    3. auto_now_add : 데이터가 생성 될 때 시간을 기록
    """
    created_at = models.DateTimeField("접속 시간", auto_now_add=True)
    location = models.CharField("접속 경로", max_length=50)
    
    def __str__(self):
        return f"{self.created_at} / {self.location}"
