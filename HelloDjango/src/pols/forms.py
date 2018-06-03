'''
Created on 2018. 5. 20.

@author: 1104-2
'''
from django.forms.models import ModelForm
from .import models  #.은 현재 파일

class QuestionForm(ModelForm):
    class Meta: #어떤 Modelclasss를 사용하는지 어떤 속성을 사용하는지
    #model : 내가 연결할 모델 클래스(필수 항목)
    #fields,exlude중 택 1
    #fields : 모댈 클래스의 속성중 사용자가 작성해야 하는것을 명시
    #exclude : 모델클래스의 속성중 명시한 속성을 제외한 속성들을 사용자가 작성
        model = models.Question #Question클래스를 사용하는 것을 명시
        fields = ['question_text','image',]#변수이름과 등록한 문자 작성
        #exclude=['pub_data','customuser',]
class ChoiceForm(ModelForm):
    class Meta:
        model = models.Choice
        fields = ['choice_text',]
        #exclude = ['votes','question',]
        
class CommentForm(ModelForm):
    class Meta:
        model = models.Comment
        fields=['text','image',]