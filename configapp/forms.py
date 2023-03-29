from django import forms
from .models import Category,News

class NewForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title','content','is_published','category']
        widgets = {
            'title':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'content':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            ),
            'category':forms.TextInput(
                attrs={
                    'class':'form-control'
                }
            )
        }

    # title = forms.CharField(max_length=150,label='Cars',widget=forms.TextInput(
    #     attrs=({'class':'form-control'})
    # ))
    # content = forms.CharField(label='Text',widget=(forms.Textarea(
    #     attrs=({'class':'form-control'})
    # )))
    # is_published = forms.CharField(label='Bool',initial=True)
    # category = forms.ModelChoiceField(queryset=Category.objects.all(),label='Categories',
    #                                   widget=forms.Select(
    #                                       attrs=({'class':'form-control'})
    #                                   ))
