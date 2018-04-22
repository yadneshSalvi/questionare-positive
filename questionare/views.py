from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ResponseForm
from .models import Response
# Create your views here.

def questionare(request):
	if request.method == 'POST':
		form = ResponseForm(request.POST)
		if form.is_valid():
			response = form.save()

			return render(request,'thank_you.html')
	else:
		form = ResponseForm()
	return render(request,'questionare.html',{'form':form})