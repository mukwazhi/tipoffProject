from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import IncidentForm, Tracking
from django.core.mail import send_mail

from .models import IncidentReport


def report_form(request):
    incidentform = IncidentForm()
    if request.method == 'POST':
        station= request.POST.get('station')
        other_location = request.POST.get('other_station')
        nature_of_report = request.POST.get('nature_of_report')
        other_nature = request.POST.get('other_nature')
        location_of_incident = request.POST.get('location_of_incident')
        date_of_incident = request.POST.get('date_of_incident')
        print(date_of_incident)
        time_of_incident = request.POST.get('time_of_incident')
        incident_detail = request.POST.get('incident_detail')
        upload_evidence = request.FILES.get('upload_evidence')
        full_Name = request.POST.get('full_Name')
        Position_Title= request.POST.get('Position_Title')
        Phone_no = request.POST.get('Phone_no')
        email = request.POST.get('email')

        # Create the report instance
        report = IncidentReport.objects.create(
            nature_of_report=nature_of_report,
            station=station,
            other_location=other_location,
            date_of_incident=date_of_incident,
            time_of_incident=time_of_incident,
            location_of_incident=location_of_incident,
            # name_of_party_involved=name_of_party_involved,
            # organisation=organisation,
            # gender=gender,
            # role=role,
            incident_detail=incident_detail,
            upload_evidence=upload_evidence,
            Full_Name=full_Name,
            Position_Title=Position_Title,
            Phone_no=Phone_no,
            email=email,
        )
        report.save()
        # form = IncidentForm(request.POST)
        # if form.is_valid():
        #     incidentform = form.save(commit=False)
        #     incidentform.save()
        #     send_mail(
        #         "Subject here",
        #         "Here is the message.",
        #         "from@example.com",
        #         ["to@example.com"],
        #         fail_silently=False,
        #     )
        #     Tracking.objects.create(report_number=incidentform)
        #     tracking_token = Tracking.objects.all().last().id
        #     request.session['tracking_token'] = tracking_token
        #     return HttpResponseRedirect('thanks')
    else:

        context = {
             'incidentform': incidentform,
            # 'brand': brand
        }
        return render(request, 'reportForm.html', context)

    context = {
        # 'incidentform': incidentform,
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
    return render(request, 'home2.html', context)

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
