from django.contrib.auth.models import User
from django.shortcuts import render
from .forms import user_form, useridForm
from django.shortcuts import render, redirect
from django.conf import settings
from users.models import user_details

from django.http import HttpResponse
import os
#save_path1 = os.path.join(settings.MEDIA_ROOT, 'audio', uploaded_file.name)
#save_path1=os.path.join(settings.MEDIA_ROOT, 'audio')
def home_view(request,*args,**kwaregs):
    form = useridForm(request.POST,request.FILES)
    if form.is_valid():
        global pkval
        pkval= form.cleaned_data['idval']
        uploaded_file = form.cleaned_data['audio_file']
        if uploaded_file is not None:
        # Define the path to save the file
        # Make sure MEDIA_ROOT is configured in settings.py
            global save_path1
            save_path1 = os.path.join(settings.MEDIA_ROOT, 'audio', uploaded_file.name)

        # Create the directory if it doesn't exist
            os.makedirs(os.path.dirname(save_path1), exist_ok=True)

        # Save the file to the specified path
            with open(save_path1, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            obj = user_details.objects.get(id=pkval)
            obj.audio_file = save_path1
        else:
            form = useridForm()
            obj = user_details.objects.get(id=pkval)
    else:
        form=useridForm()
        obj = user_details.objects.get(id=1)
        #aval=form.cleaned_data['audio_file']
    obj.save()
    context={
        'form':form,
        'obj':obj,
        'pkval':pkval,}
    return render(request,"home.html",context)
    #return render(request,home.html,{})
#obj2 = user_details.objects.get(id=pkval)
