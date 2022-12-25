from django.shortcuts import render

def my_custom_page_not_found(request, exception):
    return render(request, 'error_page.html',status=404)