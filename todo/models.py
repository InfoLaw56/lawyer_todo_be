from django.db import models

# Create your models here.
class Client(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(blank=True, null=True)
    legal_status = models.CharField(blank=True, null=True, max_length=255)
    uid = models.CharField(blank=True, null=True, max_length=11)
    name = models.CharField(blank=True, null=True, max_length=255)
    first_name = models.CharField(blank=True, null=True, max_length=255)
    last_name = models.CharField(blank=True, null=True, max_length=255)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True, max_length=255)
    email = models.CharField(blank=True, null=True, max_length=255)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'clients'


class Saqme(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.ImageField(blank=True, null=True)
    description = models.CharField(blank=True, null=True, max_length=255)
    start_date = models.DateTimeField(blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        db_table = 'saqmeebi'
    

class Emplolyee(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(blank=True, null=True)
    pNo = models.CharField(blank=True, null=True, max_length=255)
    first_name = models.CharField(blank=True, null=True, max_length=255)
    last_name = models.CharField(blank=True, null=True, max_length=255)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True, max_length=255)
    email = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        db_table = 'employees'


class Document(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(blank=True, null=True)
    saqme = models.ForeignKey(Saqme, on_delete=models.CASCADE)
    description = models.CharField(blank=True, null=True, max_length=255)
    link = models.URLField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    organization = models.CharField(blank=True, null=True, max_length=255)
    author = models.CharField(blank=True, null=True, max_length=255)
    responsible = models.ForeignKey(Emplolyee, on_delete=models.CASCADE)

    class Meta:
        db_table = 'documents'


class Todo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(blank=True, null=True)
    type = models.CharField(blank=True, null=True, max_length=255)
    importance = models.CharField(blank=True, null=True, max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    place = models.CharField(blank=True, null=True, max_length=255)
    time = models.DateTimeField(null=True, blank=True)
    saqme = models.ForeignKey(Saqme, on_delete=models.CASCADE)

    class Meta:
        db_table = 'todos'
        