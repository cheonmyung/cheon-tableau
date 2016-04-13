# for social sharing
from urllib import quote_plus

from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
#from django.views.generic.base import TemplateView
from django.utils import timezone
from .models import Blog

from .forms import BlogForm





# create for all of Blog types
def blog_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form = BlogForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		#instance.industry_type = industry_type
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		if instance.blog_type == 'Basic Steps':
			return HttpResponseRedirect(instance.basic_url())
		elif instance.blog_type == 'Tableau Concepts':
			return HttpResponseRedirect(instance.concepts_url())
		elif instance.blog_type == 'Simple Techniques':
			return HttpResponseRedirect(instance.techniques_url())
		elif instance.blog_type == 'Tableau Desktop':
			return HttpResponseRedirect(instance.desktop_url())
		elif instance.blog_type == 'Tips':
			return HttpResponseRedirect(instance.tips_url())
		#elif instance.blog_type == 'HealthCare':
		#	return HttpResponseRedirect(instance.health_url())



	context = {
		"form": form,
	}
	return render(request, "create_form.html", context)





## -------------- Lists -------------------- ##

# list for Retail 
def basic_list(request):
	today = timezone.now().date()
	#queryset_list = Post.objects.active() #filter(draft=False).filter(publish__lte=timezone.now()) #all() #.order_by("-timestamp")
	#form = PostForm(request.POST or None, request.FILES or None)
	#banking_form = BankingForm(request.POST or None, request.FILES or None)
	#instance = Post()

	queryset_list = Blog.objects.filter(blog_type='Basic Steps')

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
			"title": "Basic Steps",
			"today": today,

	}
	return render(request, "tips/basic_list.html", context)


# list for Tableau Concepts 
def concepts_list(request):
	today = timezone.now().date()
	#queryset_list = Post.objects.active() #filter(draft=False).filter(publish__lte=timezone.now()) #all() #.order_by("-timestamp")
	#form = PostForm(request.POST or None, request.FILES or None)
	#banking_form = BankingForm(request.POST or None, request.FILES or None)
	#instance = Post()

	queryset_list = Blog.objects.filter(blog_type='Tableau Concepts')

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
			"title": "Tableau Concepts",
			"today": today,

	}
	return render(request, "tips/basic_list.html", context)


# list for Simple Techniques 
def techniques_list(request):
	today = timezone.now().date()
	
	queryset_list = Blog.objects.filter(blog_type='Simple Techniques')

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
			"title": "Tableau Concepts",
			"today": today,

	}
	return render(request, "tips/basic_list.html", context)


# list for Simple Techniques 
def desktop_list(request):
	today = timezone.now().date()
	
	queryset_list = Blog.objects.filter(blog_type='Tableau Desktop')

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
			"title": "Tableau Desktop",
			"today": today,

	}
	return render(request, "tips/basic_list.html", context)


# list for Tips 
def tips_list(request):
	today = timezone.now().date()
	
	queryset_list = Blog.objects.filter(blog_type='Tips')

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
			"title": "Tips",
			"today": today,

	}
	return render(request, "tips/basic_list.html", context)



## -------------- Details -------------------- ##



def basic_detail(request, slug=None):
	instance = get_object_or_404(Blog, slug=slug)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content) # for social sharing
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "tips/basic_detail.html", context)

def concepts_detail(request, slug=None):
	instance = get_object_or_404(Blog, slug=slug)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content) # for social sharing
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "tips/concepts_detail.html", context)


def techniques_detail(request, slug=None):
	instance = get_object_or_404(Blog, slug=slug)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content) # for social sharing
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "tips/techniques_detail.html", context)


def desktop_detail(request, slug=None):
	instance = get_object_or_404(Blog, slug=slug)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content) # for social sharing
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "tips/desktop_detail.html", context)


def tips_detail(request, slug=None):
	instance = get_object_or_404(Blog, slug=slug)
	if instance.publish > timezone.now().date() or instance.draft:
		if not request.user.is_staff or not request.user.is_superuser:
			raise Http404
	share_string = quote_plus(instance.content) # for social sharing
	context = {
		"title": instance.title,
		"instance": instance,
		"share_string": share_string,
	}
	return render(request, "tips/tips_detail.html", context)


## -------------- Updates -------------------- ##



# update for Basic
def basic_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Blog, slug=slug)
	form = BlogForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.basic_url())


	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}

	return render(request, "tips/basic_form.html", context)

# update for Tableau Concepts
def concepts_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Blog, slug=slug)
	form = BlogForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.concepts_url())


	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}

	return render(request, "tips/basic_form.html", context)

# update for Simple Techniques
def techniques_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Blog, slug=slug)
	form = BlogForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.techniques_url())


	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}

	return render(request, "tips/basic_form.html", context)


# update for Simple Techniques
def desktop_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Blog, slug=slug)
	form = BlogForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.desktop_url())


	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}

	return render(request, "tips/basic_form.html", context)



# update for Tips 
def tips_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Blog, slug=slug)
	form = BlogForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		# message success
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.tips_url())


	context = {
		"title": instance.title,
		"instance": instance,
		"form": form,
	}

	return render(request, "tips/basic_form.html", context)


## -------------- Delete -------------------- ##



# delete for Basic Steps 
def basic_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Blog, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")

	return redirect("basic_list")

# delete for Tableau Concepts  
def concepts_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Blog, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")

	return redirect("concepts_list")


# delete for Simple Techniques 
def techniques_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Blog, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")

	return redirect("techniques_list")


# delete for Tableau Desktop 
def desktop_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Blog, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")

	return redirect("desktop_list")


# delete for Tips  
def tips_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Blog, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")

	return redirect("tips_list")
