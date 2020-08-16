from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from content.models import CommentForm, Comment, Menu, DuyuruForm, Content
from home.models import Setting


def index(request):

    return HttpResponse('page')
@login_required(login_url='/login')
def addComment(request, id):
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            current_user = request.user
            data = Comment()
            data.user_id = current_user.id
            data.content_id = id
            data.rate = form.cleaned_data['rate']
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Yorumunuz başarı ile gönderilmiştir.Teşekkür ederiz")
            return HttpResponseRedirect(url)

    return HttpResponseRedirect(url)

@login_required(login_url='/login')
def addContent(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = DuyuruForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Content()
            data.user_id = current_user.id

            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            data.type = form.cleaned_data['type']
            data.slug = form.cleaned_data['slug']
            data.detail = form.cleaned_data['detail']
            data.status = 'Hayır'
            data.save()
            messages.success(request, 'Duyurunuz başarı ile gönderilmiştir.Teşekkür ederiz')
            return HttpResponseRedirect(url)
        else:
            messages.warning(request, 'Form Hatalı!!' )
            return HttpResponseRedirect(url)
    else:
        menu = Menu.objects.all()
        setting = Setting.objects.get(pk=1)
        form = DuyuruForm()
        context = {
            'setting': setting,
            'menu': menu,
            'form': form,
        }
        return render(request, 'userDuyuruEkle.html', context)


