from djongo import models


class ServiceArea(models.Model):
    _id = models.ObjectIdField()
    provider_id = models.Field()
    name = models.CharField(max_length=255)
    price = models.FloatField()
    location = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Provider(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=50, unique=True)
    language = models.CharField(max_length=50)
    currency = models.CharField(max_length=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
