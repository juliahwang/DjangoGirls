from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import PostCreateForm

# 이럴 경우 같은 폴더 안에 있으므로 상대경로에 써주는 것이 좋다.

User = get_user_model()
# Create your views here.
def post_list(request):
    # return HttpResponse('<html><body>Post List</body></html>')
    # posts변수에 ORM을 이용해서 전체 Post의 리스트(쿼리셋)를 대입
    # posts = Post.objects.all()
    # print(posts)
    # posts변수에 ORM을 사용해서 전달할 쿼리셋이
    # Post의 published_date가 timezone.now()보다
    # 작은 값을 가질때만 해당하도록 필터를 사용한다.
    posts = Post.objects.order_by('-created_date')

    context = {
        'title': 'PostList from post_list view',
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context=context)


def post_detail(request, pk):
    context = {
        'post': Post.objects.get(pk=pk),
    }
    return render(request, 'blog/post_detail.html', context=context)

def post_create(request):
    if request.method == 'GET':
        form = PostCreateForm()
        context = {
        'form': form,
    }
        return render(request, 'blog/post_create.html', context=context)
    elif request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            user = User.objects.first()
            post = Post.objects.create(
                author=user,
                title=title,
                text=text
            )
            return redirect('post_detail', pk=post.pk)
        else:
            context = {
                'form': form,
            }
            return render(request, 'blog/post_create', context)