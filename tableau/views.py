# for social sharing
from urllib import quote_plus

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
#from django.views.generic.base import TemplateView
from django.utils import timezone
from .models import Post

from .forms import PostForm




# Landing Page
def home_page(request):
	return render(request, "tableau/tableau_home.html", {})

def about_me(request):
	return render(request, "about_me.html", {})


# create for all of Industries
def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		#instance.industry_type = industry_type
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		if instance.industry_type == 'Retail':
			return HttpResponseRedirect(instance.get_absolute_url())
		elif instance.industry_type == 'Banking':
			return HttpResponseRedirect(instance.banking_url())
		elif instance.industry_type == 'Social Network':
			return HttpResponseRedirect(instance.social_url())
		elif instance.industry_type == 'Real Estate':
			return HttpResponseRedirect(instance.real_url())
		elif instance.industry_type == 'Travel':
			return HttpResponseRedirect(instance.travel_url())
		elif instance.industry_type == 'HealthCare':
			return HttpResponseRedirect(instance.health_url())



	context = {
		"form": form,
	}
	return render(request, "create_form.html", context)



## -------------- Details -------------------- ##


def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content) # for social sharing
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "post_detail.html", context)


def banking_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content) # for social sharing
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "banking_detail.html", context)


def social_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content) # for social sharing
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "social_detail.html", context)


def real_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content) # for social sharing
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "real_detail.html", context)


def travel_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content) # for social sharing
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "travel_detail.html", context)

def health_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content) # for social sharing
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "health_detail.html", context)




## -------------- Lists -------------------- ##

# list for Retail 
def post_list(request):
	today = timezone.now().date()
	#queryset_list = Post.objects.active() #filter(draft=False).filter(publish__lte=timezone.now()) #all() #.order_by("-timestamp")
	#form = PostForm(request.POST or None, request.FILES or None)
	#banking_form = BankingForm(request.POST or None, request.FILES or None)
	#instance = Post()

	queryset_list = Post.objects.filter(industry_type='Retail')
	#if instance.industry_type == 'Banking':
	#	queryset_list = Post.objects.filter(industry_type='Banking')
	
		#queryset_list = Post.objects.filter(industry_type='Retail & Wholesale')
		#if industry.industry_type == 'Retail & Wholesale':
		#if request.user.is_staff or request.user.is_superuser:
		#	queryset_list =Post.objects.all()
	#	paginator = Paginator(queryset_list, 3) # Show 25 queryset per page

	#	page = request.GET.get('page')
	#	try:
	#		queryset = paginator.page(page)
	#	except PageNotAnInteger:
			# If page is not an integer, deliver first page.
	#		queryset = paginator.page(1)
	#	except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
	#		queryset = paginator.page(paginator.num_pages)

	#	context = {
	#		"object_list": queryset,
	#		"title": "Banking",
	#		"today": today,

	#	}
	#	return render(request, "banking_list.html", context)

	#queryset_list = Post.objects.filter(industry_type='Retail & Wholesale')
	#if industry.industry_type == 'Retail & Wholesale':
	#if request.user.is_staff or request.user.is_superuser:
	#	queryset_list =Post.objects.all()
	paginator = Paginator(queryset_list, 3) # Show 25 queryset per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)



	context = {
			"object_list": queryset,
			"title": "Retail",
			"today": today,

	}
	return render(request, "post_list.html", context)





# list for Banking
def banking_list(request):
	today = timezone.now().date()
	#queryset_list = Post.objects.active() #filter(draft=False).filter(publish__lte=timezone.now()) #all() #.order_by("-timestamp")
	#queryset_list = Post.objects.filter(industry_type='Banking')
	#queryset_list = Post.objects.active()
	#instance = Post()

	#queryset_list = Post.objects.filter(industry_type='Retail & Wholesale')
	#if instance.industry_type == 'Banking':
	query_list = Post.objects.filter(industry_type='Banking')

	#if request.user.is_staff or request.user.is_superuser:
	#	queryset_list =Post.objects.all()
	paginator = Paginator(query_list, 3) # Show 25 queryset per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"title": "Banking",
		"today": today,
	}
	return render(request, "post_list.html", context)
	# In order to display only "banking" in banking industy list page, 
	# I just changed banking_list.html to post_list.html. But how come did it happen?
	# I need to find the reasons why it did happen.....


# list for Social Network
def social_list(request):
	today = timezone.now().date()
	#queryset_list = Post.objects.active() #filter(draft=False).filter(publish__lte=timezone.now()) #all() #.order_by("-timestamp")
	#queryset_list = Post.objects.filter(industry_type='Banking')
	#queryset_list = Post.objects.active()
	#instance = Post()

	#queryset_list = Post.objects.filter(industry_type='Retail & Wholesale')
	#if instance.industry_type == 'Banking':
	query_list = Post.objects.filter(industry_type='Social Network')

	#if request.user.is_staff or request.user.is_superuser:
	#	queryset_list =Post.objects.all()
	paginator = Paginator(query_list, 3) # Show 25 queryset per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"title": "Social Network",
		"today": today,
	}
	return render(request, "post_list.html", context)


# list for Real Estate
def real_list(request):
	today = timezone.now().date()
	#queryset_list = Post.objects.active() #filter(draft=False).filter(publish__lte=timezone.now()) #all() #.order_by("-timestamp")
	#queryset_list = Post.objects.filter(industry_type='Banking')
	#queryset_list = Post.objects.active()
	#instance = Post()

	#queryset_list = Post.objects.filter(industry_type='Retail & Wholesale')
	#if instance.industry_type == 'Banking':
	query_list = Post.objects.filter(industry_type='Real Estate')

	#if request.user.is_staff or request.user.is_superuser:
	#	queryset_list =Post.objects.all()
	paginator = Paginator(query_list, 3) # Show 25 queryset per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"title": "Real Estate",
		"today": today,
	}
	return render(request, "post_list.html", context)


# list for Travel
def travel_list(request):
	today = timezone.now().date()
	#queryset_list = Post.objects.active() #filter(draft=False).filter(publish__lte=timezone.now()) #all() #.order_by("-timestamp")
	#queryset_list = Post.objects.filter(industry_type='Banking')
	#queryset_list = Post.objects.active()
	#instance = Post()

	#queryset_list = Post.objects.filter(industry_type='Retail & Wholesale')
	#if instance.industry_type == 'Banking':
	query_list = Post.objects.filter(industry_type='Travel')

	#if request.user.is_staff or request.user.is_superuser:
	#	queryset_list =Post.objects.all()
	paginator = Paginator(query_list, 3) # Show 25 queryset per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"title": "Travel",
		"today": today,
	}
	return render(request, "post_list.html", context)


# list for HealthCare
def health_list(request):
	today = timezone.now().date()
	#queryset_list = Post.objects.active() #filter(draft=False).filter(publish__lte=timezone.now()) #all() #.order_by("-timestamp")
	#queryset_list = Post.objects.filter(industry_type='Banking')
	#queryset_list = Post.objects.active()
	#instance = Post()

	#queryset_list = Post.objects.filter(industry_type='Retail & Wholesale')
	#if instance.industry_type == 'Banking':
	query_list = Post.objects.filter(industry_type='HealthCare')

	#if request.user.is_staff or request.user.is_superuser:
	#	queryset_list =Post.objects.all()
	paginator = Paginator(query_list, 3) # Show 25 queryset per page

	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"title": "HealthCare",
		"today": today,
	}
	return render(request, "post_list.html", context)



## -------------- Updates -------------------- ##


# update for Retail
def post_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())


	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}

	return render(request, "post_form.html", context)



# update for Banking
def banking_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.banking_url())


	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}

	return render(request, "post_form.html", context)

# update for Social Network
def social_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.social_url())


	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}

	return render(request, "post_form.html", context)


# update for Social Network
def real_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.real_url())


	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}

	return render(request, "post_form.html", context)


# update for Travel 
def travel_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.travel_url())


	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}

	return render(request, "post_form.html", context)

# update for HealthCare 
def health_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.health_url())


	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}

	return render(request, "post_form.html", context)




## -------------- Deletes -------------------- ##


# delete for Retail 
def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")

	return redirect("list")

# delete for Banking
def banking_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")

	return redirect("banking_list")

# delete for Social Network
def social_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")

	return redirect("social_list")


# delete for Real Estate
def real_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")

	return redirect("real_list")

# delete for Travel 
def travel_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")

	return redirect("travel_list")


# delete for HealthCare 
def health_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")

	return redirect("health_list")

