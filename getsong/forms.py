from django.forms import ModelForm,FileInput
from .models import Data

class Upload(ModelForm):
	class Meta:
		model = Data
		fields = ['file','song_url','user_url','follow_user']
		widgets = {
			'file': FileInput({'accept':'.mp3'})
		}

		def cleaned_file(self):
			file = self.cleaned_data.get('file')
			if file==None:
				raise forms.ValidationError("please enter a file name")
			return file

		def cleaned_song_url(self):
			song_url = self.cleaned_data.get('song_url')
			if song_url==None:
				raise forms.ValidationError("please enter a file name")
			return song_url