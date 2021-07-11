from tours import data


def common_context(request):
    return {
        'main_title': data.title,
        'all_departures': data.departures
    }
