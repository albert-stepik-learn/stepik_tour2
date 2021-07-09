import random

from django.shortcuts import render

from tours import data


# Prepare data for the departure_view:
deps = {}
for dep, val in data.departures.items():
    deps[dep] = {
        'title': data.title,
        'dep_title': 'Летим ' + val.replace('Из', 'из'),
        'tours': {},
        'departures': data.departures,
        'departure': dep
    }
for tid, tour in data.tours.items():
    deps[tour['departure']]['tours'][tid] = tour
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
    # Get 6 random tours:
    keys = data.tours.keys()
    tkeys = random.sample(keys, len(keys))[:6]
    tours = {k: data.tours[k] for k in tkeys}

    context = {
        'title': data.title,
        'subtitle': data.subtitle,
        'description': data.description,
        'departures': data.departures,
        'tours': tours
    }
    return render(request, "tours/index.html", context=context)


def departure_view(request, departure):
    return render(request, "tours/departure.html", context=deps[departure])


def tour_view(request, tour_id):
    context = {
        'title': data.title,
        'tour_id': tour_id,
        'departures': data.departures,
        'tour': data.tours[tour_id]
    }
    return render(request, 'tours/tour.html', context=context)
