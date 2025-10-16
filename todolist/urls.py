from django.urls import path
from todolist.views import home, monday, tuesday, wednesday, thursday, friday, saturday, sunday



urlpatterns = [
    path('', home, name = 'home'),
    path('monday/', monday),
    path('tuesday/', tuesday),
    path('wednesday/', wednesday),
    path('thursday/', thursday),
    path('friday/', friday),
    path('saturday/', saturday),
    path('sunday/', sunday),
]
