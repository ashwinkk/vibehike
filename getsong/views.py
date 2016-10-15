from django.shortcuts import render
import soundcloud
from .forms import Upload
from vibehike.settings import MEDIA_ROOT
from django.http import HttpResponseRedirect
from .models import Data
from django.views.decorators.csrf import csrf_exempt
from django.contrib.staticfiles.views import serve

# Create your views here.

def landing(request):
	form = Upload()
	if(request.method=='GET'):
		form = Upload()
	else:
		print request.FILES
		frm = Upload(request.POST,request.FILES)
		if(frm.is_valid()):
			ins = frm.save(commit=False)
		dat = Data.objects.filter(song_url=request.POST.get('song_url')).last()
		uid = str(dat.id)
		return HttpResponseRedirect('/player/'+uid+'/')
	return render(request,'landing.html',{'form' : form.as_p() })


def get_song(request):
	print request.path
	keys = request.path.split('/')
	key = 0
	print keys
	key = int(keys[-2])
	print key,type(key)
	dat = Data.objects.filter(id = int(key)).first()
	song_url = dat.song_url
	client = soundcloud.Client(client_id='YOUR_CLIENT_ID')
	embed = client.get('/oembed',url=song_url)
	player = {'player': embed.html,'link': str(key)}
	return render(request,'player.html',player)

@csrf_exempt
def download(request):
	keys = request.path.split('/')
	print keys
	key = int(keys[-2])
	dat = Data.objects.filter(id=key).first()
	if(dat.follow_user==True):
		fname = dat.file
		print "received"
		if(keys[-3]=='ajax'):
			return HttpResponseRedirect('/download/15/')
		return serve(request,fname.name)
	else:
		return render(request,"failed.html",{})