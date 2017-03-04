from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView
from planner import views as planner_views

urlpatterns = [
    url(r'^$', planner_views.index),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^welcome/', planner_views.welcome, name="welcome"),
    url(r'^intake/', planner_views.intake, name="intake"),
    url(r'^options/', planner_views.options, name="options"),
    url(r'^timeline/ca/', planner_views.timeline_ca, name="timeline_ca"),
    url(r'^timeline/tx/', planner_views.timeline_tx, name="timeline_tx"),
    # url(r'^login/', login_view, name="login_view"),
    # url(r'^logout/', logout_view, name="logout_view"),    
]
