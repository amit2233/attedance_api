from django.conf.urls import url
from .views import SubjectView,LectureView




urlpatterns=[
     url(r'^register',UserCreateView.as_view(),name='register'),
    #  url(r'^login',UserLoginView.as_view(),name='login'),
     url(r'^subject/add',SubjectView.as_view(),name='s-add'),
    #  url(r'^day/add',DaysView.as_view(),name='d-add'),
     url(r'^lec/add',LectureView.as_view(),name='s-add')
]
