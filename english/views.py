from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.
def index(request):
    return render(request, "index.html")


def word(request):
    search = request.GET.get("search")
    dictionary = PyDictionary()
    meaning = dictionary.meaning(search)
    synonyms = dictionary.getSynonyms(search)
    antonyms = dictionary.getAntonyms(search)
    context = {
        "meaning": meaning,
        "antonyms": antonyms,
        "synonyms": synonyms,
        "search": search,
    }
    return render(request, "word.html", context)
