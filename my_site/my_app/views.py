from django.shortcuts import render

# Create your views here.

def example_view(request):
    return render(request, 'my_app/example.html')


def variable_view(request):
    my_var = {
        'first_name':'Usama', 'last_name':'Amjid',
        'some_list': [1,2,3],
        'some_dict': {'inside_key':'inside_value'},
        'user_loged_in':True
    }
    userData = {
        'name':'Usama',
        'roll_no': 104,
    }
    return render(request, 'my_app/variable.html', context=userData)