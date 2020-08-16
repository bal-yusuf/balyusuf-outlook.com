from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect

from content.models import Menu, Content, Comment, DuyuruForm, ContentImageForm, CImages
from home.models import Setting, UserProfile

from user.forms import UserUpdateForm, ProfileUpdateForm


def uyeProfil(request):
    menu = Menu.objects.all()
    setting = Setting.objects.get(pk=1)
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {
        'menu': menu,
        'setting': setting,
        'profile': profile,
    }
    return render(request, 'userProfile.html', context)
def updateProfil(request):

    if request.method == 'POST':
        user_form=UserUpdateForm(request.POST, instance=request.user)
        profile_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Güncellendi!')
            return HttpResponseRedirect('/user')
    else:
        menu = Menu.objects.all()
        setting = Setting.objects.get(pk=1)
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)

        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {
            'menu': menu,
            'setting': setting,
            'user_form': user_form,
            'profile_form': profile_form,
            'profile': profile,
        }
        return render(request, 'userUpdate.html', context)






def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Başarıyla şifre değiştirildi!')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error below.')
            return HttpResponseRedirect('/user/password')

    else:
        setting = Setting.objects.get(pk=1)
        menu = Menu.objects.all()
        form=PasswordChangeForm(request.user)
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.id)
        return render(request,'user_change_password.html', {
            'setting': setting,
            'form': form,
            'menu' : menu,
            'profile' : profile,

        })


@login_required(login_url='/login')
def contents(request):
    menu=Menu.objects.all()
    setting = Setting.objects.get(pk=1)
    current_user= request.user
    contents=Content.objects.filter(user_id=current_user.id)
    context = {
        'menu': menu,
        'setting': setting,
        'contents': contents,
    }
    return render(request, 'user_contents.html' ,context)

@login_required(login_url='/login')
def comments(request):
    menu=Menu.objects.all()
    setting = Setting.objects.get(pk=1)
    current_user= request.user
    comments=Comment.objects.filter(user_id=current_user.id)


    context = {
        'setting': setting,
        'menu': menu,
        'comments': comments,
        'contents': contents,

    }
    return render(request, 'user_comments.html' ,context)

@login_required(login_url='/login')
def contentedit(request, id):
    content = Content.objects.get(id=id)
    if request.method=='POST':
        form=DuyuruForm(request.POST, request.FILES, instance=content)
        if form.is_valid():
            form.save()


            messages.success(request, 'Başarıyla değiştirildi!')
            return HttpResponseRedirect('/user/contentedit/'+str(id))
        else:
            messages.error(request, 'Please correct the error below.')
            return HttpResponseRedirect('/user/contentedit/'+str(id))

    else:
        menu = Menu.objects.all()
        setting = Setting.objects.get(pk=1)
        form = DuyuruForm(instance=content)
        context = {
            'menu': menu,
            'setting': setting,
            'form': form,
        }
        return render(request, 'userDuyuruEkle.html', context)


@login_required(login_url='/login')
def deleteComment(request, id):
    current_user=request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Yorum kaldırıldı!!!!')
    return HttpResponseRedirect('/user/comments/')

@login_required(login_url='/login')
def deleteContent(request, id):
    current_user=request.user
    Content.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'İçerik kaldırıldı!!!!')
    return HttpResponseRedirect('/user/contents/')


def contentaddimage(request,id):
    if request.method == 'POST':
        lasturl = request.META.get('HTTP_REFERER')
        form = ContentImageForm(request.POST, request.FILES)
        if form.is_valid():
            data = CImages()
            data.title = form.cleaned_data['title']
            data.content_id = id
            data.image = form.cleaned_data['image']
            data.save()
            messages.success(request,'Yükleme başarılı')
            return HttpResponseRedirect(lasturl)
        else:
            messages.warning(request, 'Form error')
            return HttpResponseRedirect(lasturl)
    else:
        content =Content.objects.get(id=id)
        setting = Setting.objects.get(pk=1)

        images=CImages.objects.filter(content_id = id)
        form =ContentImageForm()
        context = {
            'content': content,
            'setting': setting,
            'images': images,
            'form': form,
        }
        return render(request, 'content_gallery.html', context)

