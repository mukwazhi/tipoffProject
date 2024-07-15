from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import IncidentForm, Tracking
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
            Tracking.objects.create(report_number=incidentform)
            tracking_token = Tracking.objects.all().last().id
            request.session['tracking_token'] = tracking_token
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
        return HttpResponseRedirect(' ')

def home(request):
    context = {

    }
    return render(request, 'home.html', context)

def track(request):
    q = request.GET.get('q')
    if  q:
        try:
            tracking = Tracking.objects.get(tracking_number=q)
            return render(request,'tracker.html',{'tracking':tracking})
        except ObjectDoesNotExist:
            invalid = "Please enter a valid code"
            return render(request, 'tracking_access.html', {"invalid": invalid})
    else:

        return render(request, 'tracking_access.html', {})
