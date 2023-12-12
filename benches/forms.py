from django import forms
from .models import Bench, BenchImage

class BenchForm(forms.ModelForm):
    class Meta:
        model = Bench
        fields = ['location_latitude', 'location_longitude', 'avatar', 'rating', 'has_backrest', 'has_bin', 'deskription', 'type', 'district', 'environment']

    def __init__(self, *args, **kwargs):
        super(BenchForm, self).__init__(*args, **kwargs)
        self.fields['avatar'].widget.attrs.update({'accept': 'image/*'})  # Ограничиваем типы файлов, которые можно загрузить

class BenchImageForm(forms.ModelForm):
    class Meta:
        model = BenchImage
        fields = ['image']
