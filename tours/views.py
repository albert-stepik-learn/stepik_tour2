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
