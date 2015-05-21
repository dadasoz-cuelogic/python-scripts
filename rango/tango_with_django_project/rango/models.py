from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_positive(value):
    if value < 0:
        raise ValidationError('%s is not an even number' % value)


class Category(models.Model):
	name = models.CharField(max_length = 128, unique = True)
	likes = models.IntegerField(default = 0)
	views = models.IntegerField(default = 0, validators=[validate_positive])
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	def __str__(self):
		return self.name


class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length = 150)
	views = models.IntegerField(default = 0)
	url = models.URLField()

	def __str__(self):
		return self.title


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	picture = models.ImageField(upload_to = 'profile_images', blank = True)
	website = models.URLField(blank = True)
	gender = models.CharField(blank = True, max_length = 20)

	def __str__(self):
		return self.user.username

