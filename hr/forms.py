from django import forms
from .models import Person, City

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'birthdate', 'country', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        data = kwargs.get('data')
        if data is not None:
            try:
                country_id = int(data.get('country'))
                self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
            except ValueError:
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance:
            self.fields['city'].queryset = self.instance.country.city_set.order_by('name')
