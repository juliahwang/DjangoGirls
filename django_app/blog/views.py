from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Post

# 이럴 경우 같은 폴더 안에 있으므로 상대경로에 써주는 것이 좋다.

# Create your views here.
def post_list(request):
    # return HttpResponse('<html><body>Post List</body></html>')
    # posts변수에 ORM을 이용해서 전체 Post의 리스트(쿼리셋)를 대입
    # posts = Post.objects.all()
    # print(posts)
    # posts변수에 ORM을 사용해서 전달할 쿼리셋이
    # Post의 published_date가 timezone.now()보다
    # 작은 값을 가질때만 해당하도록 필터를 사용한다.
    posts = Post.objects.filter(
        published_date__lte=timezone.now())

    context = {
        'title': 'PostList from post_list view',
        'posts': posts,
    } # 데이터셋은 딕셔너리 형태로 전달한다.
    return render(request, 'blog/post_list.html', context=context)  # 특정파일을 가공하여(render) 결과를 httpresponse로 넘겨준다