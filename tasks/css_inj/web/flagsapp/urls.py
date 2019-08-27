from django.urls import path
from django.views.generic import TemplateView

from .views import *


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('submit-flag/', FlagCreate.as_view(), name='submitflag'),
    path('thanks/', TemplateView.as_view(template_name='thanks.html'), name='thanks'),
    path('list/', FlagsList.as_view(), name='listflag'),
    path('bot/list/', flags_to_review, name='show_flag-list'),
    path('flag/<int:id>/show_flag', show_flag, name='show_flag'),
    path('flag/<int:id>/css.css', css, name='css'),
    path('flag/<int:id>/favourite', set_favourite, name='flag-favourite'),
]