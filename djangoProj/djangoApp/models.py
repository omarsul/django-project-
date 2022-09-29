from django.db import models


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['password']) < 8:
            errors["password"] = "password must be 8 characters at leat"
        return errors


class User(models.Model):
	name = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	birthDate = models.DateField(null = True)
	friends = models.ManyToManyField("self", symmetrical=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	objects = UserManager()