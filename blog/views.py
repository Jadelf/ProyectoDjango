from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Equipo,Medico
from .forms	import EquipoForm,MedicoForm
from django.contrib.auth.decorators	import login_required

#Views de equipo
def equipo_list(request):
    posts = Equipo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/equipo_list.html',{'posts':posts})

def	equipo_detail(request,pk):
	post = get_object_or_404(Equipo, pk=pk)
	return	render(request, 'blog/equipo_detail.html',{'post':post})

@login_required
def	equipo_new(request):
	form = EquipoForm()
	return render(request,'blog/equipo_edit.html',{'form':form})

@login_required
def equipo_new(request):
    if request.method =="POST":
        form = EquipoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect('equipo_detail', pk=post.pk)
    else:
        form = EquipoForm()
    return render(request,'blog/equipo_edit.html',{'form':form})

@login_required
def equipo_edit(request,pk):
    post = get_object_or_404(Equipo, pk=pk)
    if request.method == "POST":
        form = EquipoForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('equipo_detail', pk=post.pk)
    else:
        form = EquipoForm(instance=post)
    return render(request, 'blog/equipo_edit.html',{'form':form})

@login_required
def equipo_draft_list(request):
    posts = Equipo.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/equipo_draft_list.html', {'posts': posts})

@login_required
def equipo_publish(request,pk):
    post = get_object_or_404(Equipo,pk=pk)
    post.publish()
    return redirect('equipo_detail', pk=pk)

@login_required
def equipo_remove(request, pk):
    post = get_object_or_404(Equipo, pk=pk)
    post.delete()
    return redirect('equipo_list')

#Views de medico
def medic_list(request):
    posts = Medico.objects.filter(register_date__lte=timezone.now()).order_by('register_date')
    return render(request, 'blog/medic_list.html',{'posts':posts})

def	medic_detail(request,pk):
	post = get_object_or_404(Medico, pk=pk)
	return	render(request, 'blog/medic_detail.html',{'post':post})

@login_required
def	medic_new(request):
	form = MedicoForm()
	return render(request,'blog/medic_edit.html',{'form':form})

@login_required
def medic_new(request):
    if request.method =="POST":
        form = MedicoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
        return redirect('medic_detail', pk=post.pk)
    else:
        form = MedicoForm()
    return render(request,'blog/medic_edit.html',{'form':form})

@login_required
def medic_edit(request,pk):
    post = get_object_or_404(Medico, pk=pk)
    if request.method == "POST":
        form = MedicoForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('medic_detail', pk=post.pk)
    else:
        form = MedicoForm(instance=post)
    return render(request, 'blog/medic_edit.html',{'form':form})

@login_required
def medic_publish(request,pk):
    post = get_object_or_404(Medico,pk=pk)
    post.publish()
    return redirect('medic_detail', pk=pk)

@login_required
def medic_remove(request, pk):
    post = get_object_or_404(Medico, pk=pk)
    post.delete()
    return redirect('medic_list')
