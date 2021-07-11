import random

from django.http import Http404
from django.shortcuts import render

from tours import data


def main_view(request):
    tours = dict(random.sample(data.tours.items(), 6))

    context = {
        'subtitle': data.subtitle,
        'description': data.description,
        'tours': tours
    }
    return render(request, "tours/index.html", context=context)


def departure_view(request, departure):
    if departure not in data.departures:
        return Http404
    tours = {tour_id: tour for tour_id, tour in data.tours.items() if tour['departure'] == departure}
    dep_title = 'Летим ' + data.departures[departure].replace('Из', 'из')
    prices = [tour['price'] for tour in tours.values()]
    price_min = min(prices)
    price_max = max(prices)
    nights = [tour['nights'] for tour in tours.values()]
    nights_min = min(nights)
    nights_max = max(nights)

    return render(request, "tours/departure.html", context={
        'dep_title': dep_title,
        'tours_total': len(tours),
        'tours': tours,
        'price_min': price_min,
        'price_max': price_max,
        'nights_min': nights_min,
        'nights_max': nights_max,
    })


def tour_view(request, tour_id):
    if tour_id not in data.tours:
        return Http404
    return render(request, 'tours/tour.html', context={
        'tour_id': tour_id,
        'tour': data.tours[tour_id]
    })
