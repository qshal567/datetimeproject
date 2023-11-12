from django.shortcuts import render
from datetime import datetime

def current_datetime(request):
    # Get the current date and time
    now = datetime.now()
    
    # Format the date and time
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

    # Pass the formatted datetime to the template
    context = {'formatted_datetime': formatted_datetime}
    
    # Render the template with the context
    return render(request, 'myapp/current_datetime.html', context)

# Create your views here.
