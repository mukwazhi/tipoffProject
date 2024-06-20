from django.forms import ModelForm, Textarea
from datetimewidget.widgets import DateWidget, TimeWidget
from .models import IncidentReport, Tracking
from django.utils.translation import gettext_lazy as _
#from captcha.fields import CaptchaField
from .widgets import DatePicker, TimePicker


class IncidentForm(ModelForm):
    #captcha = CaptchaField()
    class Meta:
        model = IncidentReport
        fields = [
            'station',
            'other_location',
            'nature_of_report',
            'date_of_incident',
            'time_of_incident',
            'location_of_incident',
            # 'specific_location',
            'name_of_party_involved',
            'organisation',
            'gender',
            'role',
            'incident_detail',
            'upload_evidence',
            'Full_Name',
            'Position_Title',
            'Phone_no',
            'email'
        ]

        labels = {'nature_of_report': _('Nature Of Report'), }
        help_texts = {
            'station':"The name of the suboffice/airport where the incident occurred",
            'other_location':"Optional",
            'nature_of_report':"Category of violation ",
            'date_of_incident': "Date on which the incident occurred",
            'time_of_incident':'Estimated time when the incident occurred',
            'location_of_incident':'the exact location where the incident occurred',
            'specific_location': "specific area where the incident happened ",
            'name_of_party_involved':'Name of person involved if known',
            'organisation':'The organisation which the person involved works for',
            'gender':"Gender of person involved",
            'role':'',
            'incident_detail':'Please include sufficient detail describing: What happened, How it happened,Why you consider it took place  ',
            'upload_evidence':'',
            'Full_Name':'',
            'Position_Title':"",
            'Phone_no':"",
            'email':"",
        }

        widgets = {
            "date_of_incident": DatePicker(),
            'time_of_incident':TimePicker(),

        }
