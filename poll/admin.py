from django.contrib import admin
from .models import AgentName, AnnouncedStateResult, AnnouncedWardResult, AnnouncedPuResult, AnnouncedLgaResult, State, Lga, Party, PollingUnit, Voter, Ward, TotalLgaPartyScores

# Register your models here.


@admin.register(AgentName)
class AgentNameAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'user_email', 'phone', 'pollingunit_uniqueid']
    list_filter = ['first_name', 'last_name', 'user_email', 'phone']
    search_fields = ['first_name', 'last_name', 'user_email']


@admin.register(AnnouncedStateResult)
class AnnouncedStateResultAdmin(admin.ModelAdmin):
    list_display = ['state', 'party', 'voter']
    list_filter = ['state', 'party', 'voter']


@admin.register(AnnouncedWardResult)
class AnnouncedWardResultAdmin(admin.ModelAdmin):
    list_display = ['ward_name', 'party', 'voter']
    list_filter = ['ward_name', 'party', 'voter']


@admin.register(AnnouncedPuResult)
class AnnouncedPuResultAdmin(admin.ModelAdmin):
    list_display = ['polling_unit', 'party', 'party_score', 'voter']
    list_filter = ['party', 'voter']
    list_per_page = 10


@admin.register(TotalLgaPartyScores)
class TotalLgaPartyScoresAdmin(admin.ModelAdmin):
    list_display = ['lga_id', 'scores']
    list_filter = ['lga_id', 'scores']
    list_per_page = 10


@admin.register(AnnouncedLgaResult)
class AnnouncedLgaResultAdmin(admin.ModelAdmin):
    list_display = ['lga', 'party', 'party_score', 'voter']
    list_filter = ['lga', 'party']
    list_per_page = 10


@admin.register(PollingUnit)
class PollingUnitAdmin(admin.ModelAdmin):
    list_display = ['poll_unit_id', 'ward_id', 'lga_id', 'unique_ward_id', 'polling_unit_number',
                    'polling_unit_name', 'polling_unit_desc', 'latitude', 'longitude', 'voter']
    list_filter = ['lga_id', 'voter']
    list_per_page = 10


@admin.register(Voter)
class VoterAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_ip_addr']
    list_filter = ['user_name', 'user_ip_addr']


@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ['ward_id', 'ward_name', 'lga_id', 'ward_desc', 'voter']
    list_filter = ['ward_id', 'lga_id']
    search_fields = ['ward_id', 'ward_name', 'lga_id', 'ward_desc']
    list_per_page = 10


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['state']
    list_filter = ['state']


@admin.register(Lga)
class LgaAdmin(admin.ModelAdmin):
    list_display = ['lga_id', 'lga_name', 'state_id', 'voter']
    list_filter = ['lga_id', 'lga_name', 'state_id', 'voter']


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ['party_name']
    list_filter = ['party_name']
