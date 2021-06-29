import sys
from django.shortcuts import render

import tours.views
from tours import data


# Prepare data for the departure_view:
deps = {}
for dep, val in data.departures.items():
    deps[dep] = {
        'title': 'Летим ' + val.replace('Из', 'из'),
        'tours': {},
        'departures': data.departures,
        'departure': dep
    }
for tid, t in data.tours.items():
    deps[t['departure']]['tours'][tid] = t
for dep, val in deps.items():
    deps[dep]['tnumber'] = len(val['tours'])
    deps[dep]['price_min'] = f"{min([t['price'] for t in val['tours'].values()]):,}".replace(',', ' ')
    deps[dep]['price_max'] = f"{max([t['price'] for t in val['tours'].values()]):,}".replace(',', ' ')
    deps[dep]['nights_min'] = min([t['nights'] for t in val['tours'].values()])
    deps[dep]['nights_max'] = max([t['nights'] for t in val['tours'].values()])

# Format prices - separate thousands
for tour in data.tours.values():
    tour['price'] = f"{tour['price']:,}".replace(',', ' ')


def main_view(request):
    context = {
        'title': data.title,
        'subtitle': data.subtitle,
        'description': data.description,
        'departures': data.departures,
        'tours': data.tours
    }
    return render(request, "index.html", context=context)


def departure_view(request, departure):
    return render(request, "departure.html", context=deps[departure])


def tour_view(request, id):
    # tour = data.tours[id]
    # tour['stars'] = chr(0x2605) * int(tour['stars'])
    context = {
        'id': id,
        'departures': data.departures,
        'tour': data.tours[id]
    }
    return render(request, 'tour.html', context=context)
