import json
import string
from django.core.paginator import Paginator
from django.shortcuts import render

with open('db.json', 'r') as just_file:
    countries = json.load(just_file)


def home(request):
    return render(request, 'index.html')


def countries_list(request, page):
    abc = list(string.ascii_uppercase)

    pagination = Paginator(countries, 12)
    country_by_page = pagination.get_page(page)
    page_range = pagination.page_range
    pg = pagination.page(page)
    counter = pagination.num_pages
    start = pg.start_index()

    context = {
        "countries": countries,
        "abc": abc,
        "country_by_page": country_by_page,
        'pg': pg,
        "page_range": page_range,
        "counter": counter,
        "start": start,
    }

    return render(request, 'countries-list.html', context)


def country_page(request, name):
    for this_country in countries:
        if this_country['country'] == name:
            context = {
                "this_country": this_country
            }
    return render(request, 'country_page.html', context)


def countries_started_from(request, letter):
    countries_by_letter = []
    for this_country in countries:
        if list(this_country['country'])[0] == letter:
            countries_by_letter.append(this_country)
            context = {
                'countries_by_letter': countries_by_letter,
                'letter': letter
            }
    return render(request, 'countries-by-letter.html', context)


def languages(request):
    all_languages = set()
    for this_country in countries:
        country_langs = this_country['languages']
        for lang in country_langs:
            all_languages.add(lang)
    context = {
        'all_languages': all_languages
    }
    return render(request, 'languages.html', context)


def language(request, lang):
    countries_by_language = []
    for this_country in countries:
        country_langs = this_country['languages']
        for this_lang in country_langs:
            if this_lang == lang:
                countries_by_language.append(this_country)
    context = {
        'lang': lang,
        'countries_by_language': countries_by_language
    }
    return render(request, 'language.html', context)
