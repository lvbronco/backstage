from django.http import HttpResponse, JsonResponse
from datetime import datetime

def index(request):
	n = int(request.GET.get('number')) or 0
	res = {
		'datetime': datetime.now(),
		'value': 0,
		'number': n,
		'occurences': 0
	}
	if n == 0:
		return HttpResponse("No number was inputted")
	elif n > 100:
		return HttpResponse("Number too large")
	else:
		return JsonResponse(res)