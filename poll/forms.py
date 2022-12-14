from django.forms import ModelForm
from .models import Ward, Voter, PollingUnit, AnnouncedPuResult


class WardForm(ModelForm):
    class Meta:
        model = Ward
        fields = ['ward_id', 'ward_name', 'lga_id', 'ward_desc', 'voter']


class VoterForm(ModelForm):
    class Meta:
        model = Voter
        fields = ['user_name', 'user_ip_addr']


class PollingUnitForm(ModelForm):
    class Meta:
        model = PollingUnit
        fields = ['poll_unit_id', 'ward_id', 'lga_id', 'unique_ward_id', 'polling_unit_number',
                    'polling_unit_name', 'polling_unit_desc', 'latitude', 'longitude', 'voter']


class AnnouncedPuResultForm(ModelForm):
    class Meta:
        model = AnnouncedPuResult
        fields = ['polling_unit', 'party', 'party_score', 'voter']
