from django import forms
from .models import Check_box, Radio, Post


class Check_boxForm(forms.ModelForm):
    class Meta:
        model = Check_box
        fields = ('name',)

    # Nesta parte vamos definir como vai ser os inputs la no html.
    name = forms.ModelMultipleChoiceField(queryset=Check_box.objects.all(), widget=forms.CheckboxSelectMultiple)


class RadioForm(forms.ModelForm):
    class Meta:
        model = Radio
        fields = ('name',)

    name = forms.ModelChoiceField(queryset=Radio.objects.all(), widget=forms.RadioSelect)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('name_post', 'category', 'tags')

    category = forms.ModelChoiceField(queryset=Radio.objects.all(), widget=forms.RadioSelect)
    tags = forms.ModelMultipleChoiceField(queryset=Check_box.objects.all(), widget=forms.CheckboxSelectMultiple)









# TOWN_CHOICES = (
#     ('Norwich', 'Norwich'),
#     ('Dereham', 'Dereham'),
#     )
    
#     name = forms.MultipleChoiceField(required=False, choices=TOWN_CHOICES, widget=forms.CheckboxSelectMultiple)