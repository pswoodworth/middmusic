from middmusic.models import Band, Event, Classified, FAQ
from django.contrib import admin

class BandAdmin(admin.ModelAdmin):
	list_display=('name', 'description', 'photo', 'email', 'website', 'PIN')

class EventAdmin(admin.ModelAdmin):
	list_display=('name', 'date', 'description', 'photo', 'email', 'website', 'PIN', 'is_today', 'is_tomorrow', 'is_passed')

class ClassifiedAdmin(admin.ModelAdmin):
	list_display=('title','post_date', 'description', 'email', 'website', 'PIN')

class FAQAdmin(admin.ModelAdmin):
	list_display=('question', 'answer')

admin.site.register(Band, BandAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Classified, ClassifiedAdmin)
admin.site.register(FAQ, FAQAdmin)