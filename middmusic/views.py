# Create your views here.

from django.template import Context, loader
from middmusic.models import Band, Event, Classified, FAQ
from django.http import HttpResponse

def index(request):
	band_list = Band.objects.all().order_by('name')
	event_list = Event.objects.all()
	event_list_today = []
	event_list_tomorrow = []
	event_list_later = []
	for event in event_list:
		if event.is_today():
			event_list_today += [event]
		elif event.is_tomorrow():
			event_list_tomorrow += [event]
		elif not event.is_passed():
			event_list_later += [event]

	event_lists = [event_list_today, event_list_tomorrow, event_list_later]


	classified_list = Classified.objects.all().order_by('post_date')
	faq_list = FAQ.objects.all()
	t = loader.get_template('middmusic/index.html')
	c = Context({
		'band_list': band_list,
		'event_list_today': event_list_today,
		'event_list_tomorrow': event_list_tomorrow,
		'event_list_later': event_list_later,
		'classified_list': classified_list,
		'faq_list': faq_list,
	})
	return HttpResponse(t.render(c))
