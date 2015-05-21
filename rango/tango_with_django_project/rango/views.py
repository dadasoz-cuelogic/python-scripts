from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	pages = Page.objects.order_by('-views')[:5]
	context_dict = {'category' : category_list, 'pages' : pages}
	return render(request, 'rango/index.html', context_dict)


def category(request, category_name_slug):
	context_dict = {}
	try:
		category = Category.objects.get(slug = category_name_slug)
		category.views += 1
		category.save()
		context_dict['category_name'] = category.name
		pages = Page.objects.filter( category = category)
		context_dict['pages'] = pages
		context_dict['category'] = category
	except Category.DoesNotExist:
		pass
	return render(request, 'rango/category.html', context_dict)


@login_required
def add_category(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save(commit = True)
			return index(request)
		else:
			print form.errors
	else:
		form = CategoryForm()
	return render(request, 'rango/add_category.html',
		{'form' : form})


@login_required
def add_page(request, category_name_slug):
	try:
		cat = Category.objects.get(slug = category_name_slug)
	except Category.DoesNotExist:
		cat = None
	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			if cat:
				page = form.save(commit= False)
				page.category = cat
				page.views = 0
				page.save()
				return category(request, category_name_slug)
		else:
			print form.errors
	else:
		form = PageForm()
	context_dict = {'form' : form,
	'category' : cat}
	return render(request, 'rango/add_page.html', context_dict)


def register(request):
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data = request.POST)
		profile_form = UserProfileForm(data = request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit = False)
			profile.user = user
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
			registered = True
		else:
			print user_form.errors(), profile_form.errors()
	else:
		user_form = UserForm()
		profile_form = UserProfileForm
	return render(request, 'rango/register.html', { 'profile_form' : profile_form,
		'user_form' : user_form, 'registered' : registered})


def user_login(request):
	print request.GET
	print request.path
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username = username, password = password)
		if user:
			if user.is_active:
				login(request, user)
				if request.POST['next']:
					return HttpResponseRedirect(request.POST['next'])
				else:
					return HttpResponseRedirect('/rango/')
			else:
				HttpResponse('Your django account is disabled')
		else:
			HttpResponse('Invalid login details')
	else:
		return render(request, 'rango/login.html', {})


@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/rango/')


def track_url(request):
	if request.method == 'GET':
		if 'pageid' in request.GET:
			pageid = request.GET['pageid']
			page = Page.objects.get(id = pageid)
			page.views += 1
			page.save() 
			return HttpResponseRedirect(page.url)
	else:
		return HttpResponse("Sorry!!! Something went wrong")
	return HttpResponse("Sorry!!! Something went wrong")


@login_required
def like_category(request):
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['category_id']	
    likes = 0
    if cat_id:
        cat = Category.objects.get(id=int(cat_id))
        if cat:
            likes = cat.likes + 1
            cat.likes =  likes
            cat.save()
    return HttpResponse(likes)


def get_category_list(max_list = 0, starts_with = ''):
	cat_list = []
	if starts_with:
		cat_list = Category.objects.filter(name__istartswith = starts_with)
	if max_list > 0:
		if len(cat_list) > max_list:
			cat_list = cat_list[:max_list]
	return cat_list


def suggest_category(request):
	starts_with = ''
	cat_list = []
	if request.method == 'GET':
		starts_with = request.GET['suggestion']
		print starts_with
	cat_list = get_category_list(8, starts_with)
	print cat_list
	return render(request, 'rango/cats.html', {'cat_list' : cat_list})

@login_required
def user_profile(request):
	user = request.user
	userprofile = user.userprofile
	return render(request, "rango/profile.html", {'user' : user})


def about(request):
	return render(request, 'rango/about.html', {}) 