from django.http import JsonResponse
from django.shortcuts import render
from datetime import datetime
import difference.utils.maths as maths
from .models import DifferenceN, SeqABC

def index(request):
    return render(request, "build/index.html")

def difference(request):
	n: int = int(request.GET.get('number')) or 0
	if n < 1 or n > 100:
		return JsonResponse({
			'error': 'Not A Valid Number'
		})

	obj, created = DifferenceN.objects.get_or_create(n=n)
	if created:
		obj.value = maths.difference_value(n)

	obj.occurences += 1
	obj.save()

	res = {
		'datetime': datetime.now(),
		'value': obj.value,
		'number': n,
		'occurences': obj.occurences
	}
	return JsonResponse(res)

def pythagorean(request):
	a = int(request.GET.get('a')) or 0
	b = int(request.GET.get('b')) or 0
	c = int(request.GET.get('c')) or 0

	# Order the values so a < b < c
	(a,c) = maths.order_values((a,c))
	(b,c) = maths.order_values((b,c))
	(a,b) = maths.order_values((a,b))

	if c < 1 or c > 1000 or b < 1 or a < 1:
		return JsonResponse({
			'error': 'Not A Valid Number'
		})

	obj, created = SeqABC.objects.get_or_create(a=a, b=b, c=c)
	if created:
		obj.pythagorean_triple = maths.pythagorean_triples(a, b, c)
		obj.seq_sum = a * b * c

	obj.occurences += 1
	obj.save()

	res = {
		'datetime': datetime.now(),
		'(a, b, c)': (a, b, c),
		'pythagorean_triple': obj.pythagorean_triple,
		'product': obj.seq_sum,
		'occurences': obj.occurences
	}
	return JsonResponse(res)