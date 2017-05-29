from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post_list(request):
    # return HttpResponse('<html><body>Post List</body></html>')
    return render(request, 'blog/post_list.html')  # 특정파일을 읽은 다음 결과를 httpresponse로 넘겨준다