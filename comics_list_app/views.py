from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from .models import ComicsList
from .forms import ComicsListForm


@login_required
def index(request):
    username = str(request.user)
    request.session['username'] = username
    comics_info_list = get_comics_info_list(username)
    return render(request, 'comics_list_app/index.html', comics_info_list)


def edit(request, id=None):

    if id:  # idがあるとき（編集の時）
        # idで検索して、結果を戻すか、404エラー
        comics_list = get_object_or_404(ComicsList, pk=id)
    else:  # idが無いとき（新規の時）
        # ComicsListを作成
        comics_list = ComicsList()
        # POSTの時（新規であれ編集であれ登録ボタンが押されたとき）
    if request.method == 'POST':
        # フォームを生成
        form = ComicsListForm(request.POST, instance=comics_list)
        if form.is_valid():  # バリデーションがOKなら保存
            comics_list = form.save(commit=False)
            comics_list.save()
            return redirect('comics_list_app:index')
    else:  # GETの時（フォームを生成）
        form = ComicsListForm(instance=comics_list, initial={
            'username': request.session.get('username')
           })
        print('GET:', form)
    return render(request, 'comics_list_app/edit.html', dict(form=form, id=id))


def delete(request, id):
    # return HttpResponse("削除")
    member = get_object_or_404(ComicsList, pk=id)
    member.delete()
    return redirect('comics_list_app:index')


def get_comics_info_list(username):
    comics_info_list = {
        'comics_list': ComicsList.objects.filter(username=username).order_by('title')
    }
    return comics_info_list
