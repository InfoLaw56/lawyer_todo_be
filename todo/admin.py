from django.contrib import admin
from .models import Todo, Case, Document, Judge, Emplolyee, Client, Court

# Register your models here.
admin.site.register(Todo)
admin.site.register(Case)
admin.site.register(Document)
admin.site.register(Judge)
admin.site.register(Emplolyee)
admin.site.register(Client)
admin.site.register(Court)