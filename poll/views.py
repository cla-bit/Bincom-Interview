from django.shortcuts import render
from django.urls import reverse
from .models import AgentName, AnnouncedStateResult, AnnouncedWardResult, AnnouncedPuResult, AnnouncedLgaResult, State, Lga, Party, PollingUnit, Voter, Ward, TotalLgaPartyScores
from django.views.generic import TemplateView, ListView, CreateView
from .forms import VoterForm, WardForm, PollingUnitForm, AnnouncedPuResultForm

# Create your views here.


class HomeView(ListView):
    template_name = 'index.html'
    model = AnnouncedPuResult
    paginate_by = 10
    context_object_name = 'individual_poll'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['state'] = State.objects.get(state="Delta")
        context['au'] = TotalLgaPartyScores.objects.all()

        return context


class AddVoterView(CreateView):
    model = AnnouncedPuResult
    form_class = AnnouncedPuResultForm
    template_name = 'voter.html'
    success_url = '/'


class AddWardView(CreateView):
    model = Ward
    form_class = WardForm
    template_name = 'ward.html'
    success_url = '/add-poll/'