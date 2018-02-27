from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView,UpdateAPIView,DestroyAPIView,CreateAPIView
from record.models import User,Subjects,Lecture,Days,Attendance
from .serializer import USubject,ULectures


Uesr=get_user_model
class UserCreateView(CreateAPIView):
    serializer_class=UserCreate
    queryset=User.object.all()


class UserLoginView(APIView):
    serializer_class=UserLogin
    queryset=User.object.all()



class SubjectView(CreateAPIView):
    serializer_class=USubject
    queryset=Subjects.objects.all()

class SubjectUpdateView(UpdateAPIView):
    serializer_class=USubject
    queryset=Subjects.objects.all()

class SubjectDeleteView(DestroyAPIView):
    serializer_class=USubject
    queryset=Subjects.objects.all()



# class DaysView(CreateAPIView):
#     serializer_class=UDays
#
#     queryset=Days.objects.all()



#   this for lecture Timetable

class LectureView(CreateAPIView):
    serializer_class=Timetable
    queryset=Lec1.objects.all()
    queryset=Lec2.objects.all()
    queryset=Lec3.objects.all()
    queryset=Lec4.objects.all()
    queryset=Lec5.objects.all()



class LectureUpdateView(UpdateAPIView):
    serializer_class=Timetable
    queryset=Lec1.objects.all()
    queryset=Lec2.objects.all()
    queryset=Lec3.objects.all()
    queryset=Lec4.objects.all()
    queryset=Lec5.objects.all()


class LectureDeleteView(DestroyAPIView):
    serializer_class=Timetable
    queryset=Lec1.objects.all()
    queryset=Lec2.objects.all()
    queryset=Lec3.objects.all()
    queryset=Lec4.objects.all()
    queryset=Lec5.objects.all()











class AttedanceView(CreateAPIView):
    serializer_class=Present
    queryset=Lec1.objects.all()
    queryset=Lec2.objects.all()
    queryset=Lec3.objects.all()
    queryset=Lec4.objects.all()
    queryset=Lec5.objects.all()

class AttedanceUpdateView(UpdateAPIView):
    serializer_class=USubject
    queryset=Lec1.objects.all()
    queryset=Lec2.objects.all()
    queryset=Lec3.objects.all()
    queryset=Lec4.objects.all()
    queryset=Lec5.objects.all()
