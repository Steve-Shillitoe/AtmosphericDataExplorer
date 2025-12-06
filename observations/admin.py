from django.contrib import admin

from .models import Observation  # import your model
  
# register model in admin site
@admin.register(Observation)
class ObservationAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'temperature', 'humidity', 'rainfall')
    list_filter = ('timestamp',)
    search_fields = ('timestamp',)