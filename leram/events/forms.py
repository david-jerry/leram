from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from bootstrap_datepicker_plus import DatePickerInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, HTML, Field, Fieldset, Layout, Row, Submit
from crispy_forms.bootstrap import InlineField, UneditableField
from crispy_forms import layout



from leram.events.models import Request

class MyDatePicker(DatePickerInput):
    template_name = "snippets/picker.html"

class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "serv_date",
            "service",
            "about_me",
            "about_needs",
            "referals",
        ]
        widgets = {
            'serv_date': MyDatePicker(options={
                "showClose": True,
                "showClear": True,
                "showTodayButton": True,
            }),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "sm-form-control border-form-control"
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class="form-group col-md-6"),
                Column('last_name', css_class="form-group col-md-6"),
                Column('email', css_class="form-group col-md-6"),
                Column('phone_number', css_class="form-group col-md-6"),
                Column('serv_date', css_class="form-group col-md-5"),
                Column('service', css_class="form-group col-md-7"),
                Column('about_me', css_class="form-group col-md-12"),
                Column('about_needs', css_class="form-group col-md-12"),
                Column('referals', css_class="form-group col-md-12"),
            ),
            Submit('submit', 'Make Request', css_class="btn-block button button-large button-color ml-0 topmargin-sm")
        )
