from django.urls import path, re_path
from bboard.views import index, by_rubric, BbCreateView

# app_name = 'bboard'

# urlpatterns = [
#     path('', index, name='index'),
#     path('<int:rubric_id>/', by_rubric, name='by_rubric'),
#     path('add/', BbCreateView.as_view(), name='add'),
# ]

urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^(?P<rubric_id>[0-9]*)/$', by_rubric, name='by_rubric'),
    re_path(r'^add/$', BbCreateView.as_view(), name='add'),
]
