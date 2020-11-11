from django.http import HttpResponse
from django.shortcuts import redirect


# View to automatically redirect us on main page
def redirect_main(request):
    return redirect('main_page')
