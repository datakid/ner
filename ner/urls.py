from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from ner.models import Person, Organisation, Vacancy, Requirement
from ner.admin import PersonAdmin, CertInline, ExperienceInline, ShipXPInline, FTCQualInline
import datetime

urlpatterns = patterns('ner.views',
        url(r'^$', 'index'),

        url(r'^everyone/$',
            ListView.as_view(queryset=Person.people.all().order_by('surname'))),

        url(r'^people/$', ListView.as_view(queryset=Person.workers.all())),
        
        url(r'^person/(?P<pk>\d+)/$',
            DetailView.as_view(
                model=Person)),

        url(r'^person/add/$',
            CreateView.as_view(
                template_name='ner/person_create.html',
                form_class=PersonAdmin)),

        url(r'^person/(?P<pk>\d+)/edit/$',
            UpdateView.as_view(
                model=Person)),
        
        url(r'^orgs/islands/$',
            ListView.as_view(
                queryset=Organisation.objects.all(),
                template_name="ner/org_island_list.html")),
        
        url(r'^orgs/isic/$',
            ListView.as_view(
                queryset=Organisation.objects.all(),
                template_name="ner/org_isic_list.html")),
        
        url(r'^orgs/category/$',
            ListView.as_view(
                queryset=Organisation.objects.all(),
                template_name="ner/org_cat_list.html")),
        
        url(r'^organisation/(?P<slug>[-\w]+)/$',
            DetailView.as_view(
                model=Organisation,
                template_name='ner/organisation_detail.html')),

        url(r'^organisation/(?P<pk>\d+)/$',
            DetailView.as_view(
                model=Organisation)),

        url(r'^vacancies/requirements/$',
            ListView.as_view(
                queryset=Requirement.objects.all().order_by("req_name"),
                template_name="ner/vac_req_list.html")),
        
        url(r'^vacancies/$',
            ListView.as_view(
                queryset=Vacancy.objects.all())),
        
        url(r'^vacancy/(?P<pk>\d+)/$',
            DetailView.as_view(
                model=Vacancy)),
)
