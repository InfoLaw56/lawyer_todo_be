from django.db import models

# Create your models here.
class Client(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(blank=True, null=True, default=1)
    legal_status = models.CharField(blank=True, null=True, max_length=254)
    uid = models.CharField(blank=True, null=True, max_length=11)
    name = models.CharField(blank=True, null=True, max_length=254)
    first_name = models.CharField(blank=True, null=True, max_length=254)
    last_name = models.CharField(blank=True, null=True, max_length=254)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True, max_length=254)
    email = models.EmailField(blank=True, null=True, max_length=254)

    class Meta:
        db_table = 'clients'


class Court(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(blank=True, null=True, default=1)
    name = models.CharField(blank=True, null=True, max_length=254)

    class Meta:
        db_table = 'courts'


class Judge(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(blank=True, null=True, default=1)
    first_name = models.CharField(blank=True, null=True, max_length=254)
    last_name = models.CharField(blank=True, null=True, max_length=254)
    assistant = models.CharField(blank=True, null=True, max_length=254)
    secretary = models.CharField(blank=True, null=True, max_length=254)
    phone = models.CharField(blank=True, null=True, max_length=254)
    email = models.EmailField(blank=True, null=True, max_length=254)

    class Meta:
        db_table = 'judges'


BOARD_CHOICES = [
    ("1", "ადმინისტრაციული"),
    ("2", "სამოქალაქო"),
    ("3", "ად. სამართალდარღვევა"),
    ("4", "წინასასამართო")
]

CLIENT_ROLES = [
    ("1", "მოსარჩელე"),
    ("2", "მოპასუხე")
]


class Case(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(blank=True, null=True, default=1)
    court = models.ForeignKey(Court, on_delete=models.CASCADE)
    board = models.CharField(max_length=1, choices=BOARD_CHOICES, default="1")
    judge = models.ForeignKey(Judge, on_delete=models.CASCADE)
    num_long = models.CharField(blank=True, null=True, max_length=254)
    num_short = models.CharField(blank=True, null=True, max_length=254)
    description = models.CharField(blank=True, null=True, max_length=254)
    start_date = models.DateTimeField(blank=True, null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    client_role = models.CharField(max_length=1, choices=CLIENT_ROLES, default="1")
    opponent = models.CharField(blank=True, null=True, max_length=254)

    class Meta:
        db_table = 'cases'
    

class Emplolyee(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(blank=True, null=True, default=1)
    pNo = models.CharField(blank=True, null=True, max_length=254)
    first_name = models.CharField(blank=True, null=True, max_length=254)
    last_name = models.CharField(blank=True, null=True, max_length=254)
    birth_date = models.DateField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True, max_length=254)
    email = models.EmailField(blank=True, null=True, max_length=254)

    class Meta:
        db_table = 'employees'


class Document(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(blank=True, null=True, default=1)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    description = models.CharField(blank=True, null=True, max_length=254)
    date = models.DateField(blank=True, null=True)
    organization = models.CharField(blank=True, null=True, max_length=254)
    author = models.CharField(blank=True, null=True, max_length=254)
    responsible = models.ForeignKey(Emplolyee, on_delete=models.CASCADE)

    class Meta:
        db_table = 'documents'


TYPE_CHOICES = [
    ("1", "პროცესი"),
    ("2", "შეხვედრა"),
    ("3", "პირადი")
]

IMPORTANCE_CHOICES = [
    ("1", "High"),
    ("2", "Medium"),
    ("3", "Low")
]


class Todo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(blank=True, null=True, default=1)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, default="1")
    importance = models.CharField(max_length=1, choices=IMPORTANCE_CHOICES, default="1")
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    place = models.CharField(blank=True, null=True, max_length=254)
    time = models.DateTimeField(null=True, blank=True)
    case = models.ForeignKey(Case, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'todos'
        