from django.contrib import admin
from stocks.models import TopGainer, TopLoser

# Register your models here.
admin.site.register(TopGainer)
admin.site.register(TopLoser)