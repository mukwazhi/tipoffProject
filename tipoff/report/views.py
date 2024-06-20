from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import IncidentForm
from django.core.mail import send_mail

from .models import IncidentReport


def report_form(request):
    # report form
    # brand = Brand.objects.all()
    incidentform = IncidentForm()
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            incidentform = form.save(commit=False)
            incidentform.save()
            send_mail(
                "Subject here",
                "Here is the message.",
                "from@example.com",
                ["to@example.com"],
                fail_silently=False,
            )
            # Tracking.objects.create(report_number=incidentform)
            # tracking_token = Tracking.objects.all().last().id
            # request.session['tracking_token'] = tracking_token
            return HttpResponseRedirect('thanks')
    else:

        context = {
            'incidentform': incidentform,
            # 'brand': brand
        }
        return render(request, 'report_form.html', context)

    context = {
        'incidentform': incidentform,
        # 'brand': brand
    }
    return render(request, 'base.html', context)


def thanks(request):
    if request.session.session_key:
        # tracking = Tracking.objects.all().last()
        return render(request, 'thanks.html',{})

    else:
        return HttpResponseRedirect('/report_form/')

