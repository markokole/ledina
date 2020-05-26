from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import IzbiraForm
from django.views.generic.edit import CreateView
from ledina2.models import jezik, polja
from django.contrib import messages
from django.core.exceptions import ValidationError

def izberi(request): 
		
	# create object of form 
	form = IzbiraForm(request.POST or None) 
	form.instance.kandidat = request.user
	if request.method == 'POST':
	
		set_jezik = set()
		_polja = polja()[1:]
		for p in _polja:
			if int(form[p].value()) > 0:
				set_jezik.add(form[p].value())
		
		print(set_jezik)
		if len(set_jezik) < len(polja()) - 1:
		#if 1 == 2:
			messages.warning(request, 'Napaka: jeziki niso izbrani, ali se podvajajo!')
			return render(request, "izberi.html", {'form': form}) 
		
		# check if form data is valid 
		if form.is_valid():
			# save the form data to model 
			form.save()
			request.session['izberi'] = form.cleaned_data
			return redirect("izhod")
	else:
		form = IzbiraForm()
		return render(request, "izberi.html", {'form': form}) 

def izhod(request):
	form = request.session.get('izberi')
	_jezik = jezik()

	for i in range(1, len(polja())):
		form['jezik' + str(i)] = _jezik[form['jezik' + str(i)]]

	
	return render(request, "izhod.html",  {'form': form}) 