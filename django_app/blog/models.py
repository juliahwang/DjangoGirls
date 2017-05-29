from django.db import models
from django.utils import timezone  # 장고모델 안에 현재시간을 알려주는 모듈을 불러옴.
# Create your models here.


class Post(models.Model):  # models모듈 안에 Model 클래스를 상속받는다.
    """
    기본 테이블 하나를 만드는 클래스
    """
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()   # 발행시간을 현재시각으로 정해주고 저장하는 메소드
        self.save()

    def __str__(self):
        return self.title
