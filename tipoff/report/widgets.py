# widgets.py
from django.forms import DateInput
from django.forms import TimeInput


class DatePicker(DateInput):
    input_type = "date"

    def format_value(self, value):
        return value.isoformat() if value is not None and hasattr(value, "isoformat") else ""


class TimePicker(TimeInput):
    input_type = "time"
