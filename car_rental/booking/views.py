from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import CarImageForm
from .models import Car, Customer, Booking, Category
from django.urls import reverse

"""
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']    # remember request.FILES is a dictionary so it needs a key value
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'booking/upload.html', {'uploaded_file_url': uploaded_file_url})

    return render(request, 'booking/upload.html')
"""
"""
def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
"""


def model_form_upload(request):
    if request.method == 'POST':
        form = CarImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = CarImageForm()
    return render(request, 'booking/upload.html', {'form': form})


"""the upload_to can also be a string callable that returns a string
def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)
"""








