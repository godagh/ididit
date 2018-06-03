'''
Created on 2018. 6. 3.

@author: 1104-2
'''
from django.forms.models import ModelForm
from .models import Post,Image
from Blog.models import Posttype

class PostForm(ModelForm):
    class Meta:
        model = Posttype
        exclude = ('pub_date','author',)
    def __init__(self,*args,**kwargs):
        super(PostForm,self).__init__(self,*args,**kwargs)
        self.fields['type'].empty_label=None
class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ('post','image',)
        
        