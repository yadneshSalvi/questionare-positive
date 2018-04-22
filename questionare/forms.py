from django import forms
from .models import Response


class ResponseForm(forms.ModelForm):
	experience = forms.CharField(
		widget=forms.Textarea(
			attrs={'rows': 4, 'placeholder': 'Write about your best gift here...'}
		),
		max_length=4000,
		help_text='The max length of the text is 4000.'
	)
	ans_1 = forms.CharField(
		widget=forms.Textarea(
			attrs={'rows': 1, 'placeholder': 'Type A or B'}
		),
		max_length=30
	)
	ans_4 = forms.CharField(
		widget=forms.Textarea(
			attrs={'rows': 1, 'placeholder': 'Measure of angle A in degrees.'}
		),
		max_length=30
	)
	class Meta:
		model = Response
		fields = ['name','gender','age','experience','emotion_scale','ans_1','ans_2','ans_3','ans_4']