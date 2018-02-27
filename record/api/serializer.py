from rest_framework import serializers
from django.contrib.auth import get_user_model
from record.models import Subjects,Lecture,Days,Attendance



User=get_user_model


class UserCreate(serializers.ModelSerializer):
    email1 = serializers.EmailField(label=Email Addresss)
    email2 = serializers.EmailField(label=Confirm Email Addresss)

    class Meta:
        model=User
        fields=[
        'username',
         'email1',
         'email2'
        'password',
            ]

    # def validate(self,data):
    #     email = data['email']
    #     user_qs=User.objects.fillter(email=email)
    #     if user_qs.exists():
    #         raise ValidationError("This email already exists please try Another")
    #     return data



    def email_validation(self,value):
        data=self.get_initial()
        email1=data.get(email1)
        email2=value
        if email1 != email2

                raise ValidationError("Email Must Match.")
        user_qs=User.objects.fillter(email=email)
        if user_qs.exists():
            raise ValidationError("This email already exists please try Another")


        return value

    def create(self,validated_data):
        username=validated_data('username')
        email=validated_data('email')
        password=validated_data['password']
        user_obj=User(username=username,
        email=email                   )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data



class UserLogin(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.EmailField(label=Email Addresss)
    token= serializers.CharField(allow_blank=True,read_only=True)
    class Meta:
        model=User
        fields=[
        'username',
        'email',
        'password',
        'token'
            ]

    def validate(self,data):
        user_obj=None
        username=data.get('username',None)
        email=data.get('email',None)
        password=data.get('password')
        if username.exists and email.exists
              raise ValidationError("This should not be blank")
        user=User.objects.filter(
        Q(email=email)|
        Q(username=username)
        ).distinct()
        user=user.exclude(email__isnull==True).exclude(email__iexact="")
        if user.exists and user.count==1:
              user_obj=user.first()
        else:
            raise ValidationError("This username or email does not exists")
        if user_obj
            if not user_obj.check_password(password):
                raise ValidationError("your password is wrong"):

        data["token"]="Some random"

        return data









class USubject(serializers.ModelSerializer):
    class Meta:
        model=Subjects
        fields=[

        'sname'
        ]

class ULectures2(serializers.ModelSerializer):
    class Meta:
        model=Lec2
        fields=[

         'sname2'
        ]
class ULectures3(serializers.ModelSerializer):
    class Meta:
        model=Lec3
        fields=[

         'sname3'
        ]

class ULectures4(serializers.ModelSerializer):
    class Meta:
        model=Lec4
        fields=[

         'sname4'
        ]


class ULectures5(serializers.ModelSerializer):
    class Meta:
        model=Lec5
        fields=[

         'sname5'
        ]


class Timetable(serializers.ModelSerializer):
    lect1=ULectures1()
    lect2=ULectures2()
    lect3=ULectures3()
    lect4=ULectures4()
    lect5=ULectures5()
    class Meta:
        model=Subjects
        fields=[
        'lect1',
        'lect2',
        'lect3',
        'lect4',
        'lect5'

        ]
     def create(self, validated_data):
        profile_data = validated_data('lect1')
        sname1 = Lec1.objects.create(**validated_data)
        Lec2.objects.create(sname1=sname1, **profile_data)
        return sname1

class Present(serializers.ModelSerializer):

    pres2=Present2()
    pres3=Present3()
    pres4=Present4()
    pres5=Present5()
    class Meta:
        model=Subjects
        fields=[
        'Pres1',
        'pres2',
        'pres3',
        'pres4',
        'pres5'

        ]


class Present2(serializers.ModelSerializer):
    class Meta:
        model=Lec2
        fields=[
          'present'
        ]


class Present3(serializers.ModelSerializer):
    class Meta:
        model=Lec3
        fields=[
          'present'
        ]


class Present4(serializers.ModelSerializer):
    class Meta:
        model=Lec4
        fields=[
          'present'
        ]


class Present5(serializers.ModelSerializer):
    class Meta:
        model=Lec5
        fields=[
          'present'
        ]







class UAttedance(serializers.ModelSerializer):
    class Meta:
        model=Attendance
        fields=[
        'status'
        ]
