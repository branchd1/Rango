from django.shortcuts import render

from django.http import HttpResponse

from rango.forms import CategoryForm
from django.shortcuts import redirect

def index(request):
	context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
	return render(request, 'rango/index.html', context=context_dict)
	
def about(request):
	return render(request, 'rango/about.html')

def add_category(request):
	form = CategoryForm()
	# A HTTP POST?
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		# Have we been provided with a valid form?
	if form.is_valid():
		# Save the new category to the database.
		form.save(commit=True)
		# Now that the category is saved, we could confirm this.
		# For now, just redirect the user back to the index view.
		return redirect('/rango/')
	else:
		# just print them to the terminal.
		print(form.errors)
		
	return render(request, 'rango/add_category.html', {'form': form})
	
