from django.contrib import admin
from .models import Polls,Choice
# Register your models here.
admin.site.register(Choice)
admin.site.register(Polls)
'''
anothe way to simplefid the register in the admin page use all the models in one sentance
admin.site.register(Choice,Polls)
'''
