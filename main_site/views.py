from django.shortcuts import render_to_response, HttpResponse


def index(request):
    return render_to_response("panel_index.html")
