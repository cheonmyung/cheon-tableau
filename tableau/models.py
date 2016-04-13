from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save

from django.utils.text import slugify

from django.utils import timezone


class PostManager(models.Manager):
	def active(self, *args, **kwargs):
		#Post.objects.all() = super(PostManager, self).all()
		return super(PostManager, self).filter(draft=False).filter(publish__lte=timezone.now())

	#def banking(self, *args, **kwargs):
	#	return super(PostManager, self).filter(industry_type='Banking')


def upload_location(instance, filename):
	#filebase, extension = filename.split(".")
	#return "%s/%s.%s" %(instance.id, instance.id, extension)
	return "%s/%s" %(instance.id, filename)


CATEGORY_CHOICES = (
    ('Retail', 'Retail'),
    ('Banking', 'Banking'),
    ('Social Network', 'Social Network'),
    ('Travel', 'Travel'),
    ('HealthCare', 'HealthCare'),
    ('Real Estate', 'Real Estate'),
    #('Psychology', 'Psychology'),
    #('Trade', 'Trade'),
    )


class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True)
	industry_type = models.CharField(choices=CATEGORY_CHOICES, max_length=50)
	image = models.FileField(upload_to=upload_location,
			null=True, 
		    blank=True,
		    )
	#width_field="width_field",
	#height_field="height_field"
	#height_field = models.IntegerField(default=0)
	#width_field = models.IntegerField(default=0)

	# Embed Tableau from Tableau Server
	embed_code = models.CharField(max_length=500, null=True, blank=True)
	content = models.TextField()
	draft = models.BooleanField(default=False)
	publish = models.DateField(auto_now=False, auto_now_add=False)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


	objects = PostManager()

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("detail", kwargs={"slug": self.slug})

	def banking_url(self):
		banking = reverse("banking_detail", kwargs={"slug": self.slug})
		return banking

	def social_url(self):
		social = reverse("social_detail", kwargs={"slug": self.slug})
		return social

	def travel_url(self):
		travel = reverse("travel_detail", kwargs={"slug": self.slug})
		return travel

	def health_url(self):
		health = reverse("health_detail", kwargs={"slug": self.slug})
		return health

	def real_url(self):
		real = reverse("real_detail", kwargs={"slug": self.slug})
		return real

	class Meta:
		ordering = ["-timestamp", "-updated"]



def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Post.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug



def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)
	

pre_save.connect(pre_save_post_receiver, sender=Post)












