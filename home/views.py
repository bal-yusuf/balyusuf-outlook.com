from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
# from nltk import pk
from django.contrib import messages

from content.models import Menu, Content, CImages, Comment
from home.forms import SignUpForm

from home.models import Setting, ContactFormMessage, ContactFormu, UserProfile


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Content.objects.filter(status='Evet', type='duyuru').order_by('-id')[:3]
    menu = Menu.objects.all()
    content = Content.objects.filter(status='Evet', type='duyuru').order_by('-id')[:4]
    content2 = Content.objects.filter(status='Evet', type='duyuru').order_by('-id')[:3]
    etkinlik = Content.objects.filter(status='Evet', type='etkinlik').order_by('-id')[:3]
    etkinlik2 = Content.objects.filter(status='Evet', type='etkinlik').order_by('-id')[:3]



    context = {'setting': setting,
               'page': 'home',
               'menu': menu,
               'sliderdata': sliderdata,
               'content': content,
               'etkinlik': etkinlik,
               'content2': content2,
               'etkinlik2': etkinlik2,

               }
    return render(request, 'index.html', context)


############################## TÜM DUYURULAR VE ETKİNİKLER VE İÇERİK DETAY ############

def duyuru(request):
    menu = Menu.objects.all()
    setting = Setting.objects.get(pk=1)
    content = Content.objects.filter(status='Evet', type='duyuru')
    comments = Comment.objects.filter(status='Evet').order_by('?')[:4]

    context = {
        'setting': setting,
        'menu': menu,
        'content': content,
        'comments': comments,
    }
    return render(request, 'duyuru.html', context)


def etkinlik(request):
    setting = Setting.objects.get(pk=1)
    menu = Menu.objects.all()
    content = Content.objects.filter(status='Evet', type='etkinlik')
    comments = Comment.objects.filter(status='Evet').order_by('?')[:4]

    context = {
        'setting': setting,
        'menu': menu,
        'content': content,
        'comments': comments,
    }
    return render(request, 'etkinlik.html', context)


def duyuru_Detay(request, id, slug):
    menu = Menu.objects.all()
    setting = Setting.objects.get(pk=1)
    content = Content.objects.get(pk=id)
    images = CImages.objects.filter(content_id=id)
    comments = Comment.objects.filter(content_id=id, status='Evet')
    content2 = Content.objects.filter(status='Evet', type='duyuru').order_by('-id')[:3]
    etkinlik2 = Content.objects.filter(status='Evet', type='etkinlik').order_by('-id')[:3]
    context = {

        'menu': menu,
        'setting': setting,
        'content': content,
        'content2': content2,
        'etkinlik2': etkinlik2,
        'images': images,
        'comments': comments,

    }

    return render(request, 'duyuruDetay.html', context)


############################## TÜM DUYURULAR VE ETKİNİKLER VE İÇERİK DETAY ############

############################## HAKKIMIZDA SAYFALARININ DETAYLARI ############>>>>>>>>>>>>>>>>

def hakkımızda(request, id, slug):
    menu = Menu.objects.all()
    setting = Setting.objects.get(pk=1)
    content = Content.objects.get(pk=id)
    images = CImages.objects.filter(content_id=id)

    context = {
        'menu': menu,
        'setting': setting,
        'content': content,
        'images': images,


    }
    return render(request, 'hakkımızda.html', context)


############################## HAKKIMIZDA SAYFALARININ DETAYLARI ############   <<<<<<<<<<<<<<<<<<<<<<<<<<


def menu(request, id):
    try:
        content = Content.objects.get(menu_id=id)
        link = '/content/' + str(content.id) + '/menu'
        return HttpResponseRedirect(link)
    except:
        messages.warning(request, 'Hata! İlgili İçerik bulunamadı')
        link = '/'
        return HttpResponseRedirect(link)


def referans(request):
    setting = Setting.objects.get(pk=1)
    content = Content.objects.filter(status='Evet', type='duyuru').order_by('-id')[:3]
    etkinlik = Content.objects.filter(status='Evet', type='etkinlik').order_by('-id')[:3]

    menu = Menu.objects.all()
    context = {'setting': setting,
               'menu': menu,
               'content': content,
               'etkinlik': etkinlik,
               'page': 'referans'}
    return render(request, 'referanslar.html', context)


def iletişim(request):
    menu = Menu.objects.all()
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarı ile gönderilmiştir.Teşekkür ederiz")
            return HttpResponseRedirect('/iletişim')
    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting': setting,
               'menu': menu,
               'form': form}
    return render(request, 'iletişim.html', context)

def siteHak(request):
    setting = Setting.objects.get(pk=1)
    content = Content.objects.filter(status='Evet', type='duyuru').order_by('-id')[:3]
    etkinlik = Content.objects.filter(status='Evet', type='etkinlik').order_by('-id')[:3]

    menu = Menu.objects.all()
    context = {'setting': setting,
               'content': content,
               'etkinlik': etkinlik,
               'menu': menu,
               'page': 'referans'}
    return render(request, 'siteHak.html', context)


##################################################
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
    menu = Menu.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'menu': menu,
               'setting': setting,

               }
    return render(request, 'login.html', context)


def join_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/users/userImage.png"
            data.save()
            return HttpResponseRedirect('/')
    form = SignUpForm()
    setting = Setting.objects.get(pk=1)
    menu = Menu.objects.all()
    context = {'menu': menu,
               'setting': setting,
               'form': form,

               }
    return render(request, 'kayıtol.html', context)
##################################################################

