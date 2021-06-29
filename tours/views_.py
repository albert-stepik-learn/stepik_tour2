from django.shortcuts import render
from tours import data


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
    depart = data.departures[departure].replace('Из', 'из')

    context = {'departure': departure,
               'title': 'Летим ' + depart,
               'departures': data.departures,
               'tours': data.tours
    }
    return render(request, "departure.html", context=context)


def tour_view(request, id):
    context = {
        'id': id,
        'departures': data.departures
    }
    return render(request, 'tour.html', context=context)
