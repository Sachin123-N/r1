from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import FlatForm
from .models import Flat


@login_required(login_url="login_url")
def create_order(request):
    template_name = 'flatapp1/create.html'
    form = FlatForm()
    if request.method == "POST":
        form = FlatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url="login_url")
def show_order(request):
    template_name = 'flatapp1/show.html'
    orders = Flat.objects.all()
    context = {'orders': orders}
    return render(request, template_name, context)


def update_order(request, pk):
    obj = Flat.objects.get(id=pk)
    form = FlatForm(instance=obj)
    if request.method == "POST":
        form = FlatForm(request.POST, instance= obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {'form': form}
    return render(request, 'flatapp1/create.html', context)


def cancel_order(request, pk):
    obj = Flat.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('show_url')
    return render(request, 'flatapp1/confirmation.html')
