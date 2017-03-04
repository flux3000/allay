from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from planner import views as planner_views

urlpatterns = [
    url(r'^$', planner_views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^planner/', planner_views.planner, name="planner"),
    # url(r'^login/', login_view, name="login_view"),
    # url(r'^logout/', logout_view, name="logout_view"),    
]
