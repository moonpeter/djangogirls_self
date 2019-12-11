# Create your views here.
from django.shortcuts import render


def post_list(requst):
    # Template을 찾을 경로에서
    # post_list.html을 찾아서
    # 그 파일을 text로 만들어서 HttpResponse형태로 돌려준다.
    # 위 기능을 하는 shorcut함수
    return render(requst, 'post_list.html')
