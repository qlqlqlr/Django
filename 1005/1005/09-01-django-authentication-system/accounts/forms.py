from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
# Django 가 제공하는 CreateionForm 을 상속받아서
# 우리가 정의한 User  모델을 사용하도록 새로 생성

class CustomCreationForm(UserCreationForm):
    nickname = forms.CharField(max_length=30, required=False, help_text="필요시 닉네임 지정하세요")
    class Meta(UserCreationForm.Meta):
        # get_user_model() : 현재 프로젝트에 세팅된 User모델을 가져오는 역할
        model = get_user_model()
        # 앞으로 사용할 field는
        # 기존 것 + 위에서 정의한 nickname 필드 이다.
        fields = UserCreationForm.Meta.fields + ('nickname', )