from django.shortcuts import render, redirect, get_list_or_404
from .models import CurrencyRate
from .forms import CurrencyRateForm
from django.http import Http404
from datetime import datetime


# View for our main page with chart
def main_page(request):
    try:
        # Checking if our database has data, otherwise getting appropriate response
        currency = get_list_or_404(CurrencyRate)
        # Creating list for storing parsed data
        full_data_list = []
        date_list = []
        # Filling lists
        for obj in currency:
            full_data_list.append([str(obj.date), obj.uah_rate])
            date_list.append(str(obj.date))
        # Sorting our dates
        sorted_date_list = sorted(date_list)
        # Formating our dates to more simple appearance
        for i in range(len(sorted_date_list)):
            sorted_date_list[i] = datetime.strptime(sorted_date_list[i], '%Y-%m-%d').strftime('%b %Y')
        # Filling context to pass it in our template
        context = {'full_data_list': sorted(full_data_list), 'date_list': sorted_date_list}
        # Rendering template with context
        return render(request, 'CurrencyChecker/main-page.html', context)
    # Handling our error when database is empty
    except Http404:
        return render(request, 'CurrencyChecker/404-page.html')


# View for page which adds new currency rate
def add_currency_page(request):
    # If we posting (request method is POST), the new object will be created
    if request.method == 'POST':
        # Calling our model from
        form = CurrencyRateForm(request.POST)
        # Validating user input
        if form.is_valid():
            # Saving new object in database
            form.save()
            # Redirecting to main page
            return redirect('/currency_checker/main/')
    # If our request method is GET, we just receive page with form
    else:
        form = CurrencyRateForm()
    return render(request, 'CurrencyChecker/add-currency-page.html', {'form': form})
