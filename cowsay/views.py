from django.shortcuts import render
import subprocess

from cowsay.models import Cowsay
from cowsay.forms import CowsayAddForm

def index(request):
    items = Cowsay.objects.last()
    return render(request, "index.html", {"data": items.text})

def history(request):
    items = Cowsay.objects.order_by('-created_date')[:10]
    return render(request, "history.html", {"data": items})
    

def cowsay_add_view(request):
    html = "generic_form.html"

    if request.method == "POST":
        form = CowsayAddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            process = subprocess.run(["cowsay", data['text']], stdout=subprocess.PIPE, encoding="UTF-8")
            output=process.stdout
            Cowsay.objects.create(
                text=output
            )
        
    form = CowsayAddForm()

    return render(request, html, {'form': form})

