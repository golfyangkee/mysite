from django.shortcuts import render
from .forms import UploadFileForm
from django.shortcuts import redirect, reverse

# Create your views here.




def image_search(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request,'image_upload/results.html')

    else:
        form = UploadFileForm()

    return render(request, 'image_upload/search.html', {'form' : form })

#def image_upload(request):

 #   return render(request, 'image_upload/yes.html')

