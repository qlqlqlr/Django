# form : 사용자로부터 데이터를 받기위해 활용하는 방법

from django import forms
from .models import Article

# form 과 modelForm 의 차이 -> DB
# form : DB에 저장 X
# ModelForm : DB에 저장 o


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget = forms.Textarea)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # 모델에 있는 모든 필드를 이 폼에서 사용하겠다.
        fields = '__all__'