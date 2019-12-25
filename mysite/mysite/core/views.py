import io
import matplotlib.pyplot as plt
import tensorflow as tf
import cv2
import os

### If you are using tensorflow-2, then uncomment the following lines ###
# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()

from django.http import HttpResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

class Home(TemplateView):
    template_name = 'home.html'

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

def view_plot(request):

	#if request.POST.get('Display Image'):
	#form = PostForm(request.POST)
	form = request.POST.get('Display Image')
	template = 'my_upload.html' 
	context = {'form': form}
	return render(request, template, context)

def plot(request):
    # Make figure
    f = plt.figure()

    # Search for image in Media folder
    locc = []
    for root, dirs, files in os.walk(os.getcwd(), 'media'):
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
                loc = os.path.join(root, file)
                print(loc)
                locc.append(loc)                    #Append adds element

    IMG_SIZE = 50  # 50 in txt-based
    img_array = cv2.imread(locc[0], cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    prepare = new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
	
    model = tf.keras.models.load_model(os.path.join(os.getcwd(), 'mysite\\core\\cat-dog-CNN.model'))
	
    prediction = model.predict([prepare])
    pred = int(prediction)

    # Original Image
    imorg = cv2.imread(locc[0])
    imo = cv2.cvtColor(imorg, cv2.COLOR_BGR2RGB)
    axes1 = f.add_subplot(121)
    axes1.imshow(imo)
    axes1.axis("off")
    axes1.set_title("Original")

    # Predicted Image
    axes2 = f.add_subplot(122)

    if pred == 0:
        dog_dir = os.path.join(os.getcwd(), 'mysite\\core\\dog.jpg')
        r1 = cv2.imread(dog_dir, -1)
        r2 = cv2.cvtColor(r1, cv2.COLOR_BGR2RGB)
        axes2.imshow(r2)
        axes2.axis("off")
        axes2.set_title("Prediction")

    else:
        cat_dir = os.path.join(os.getcwd(), 'mysite\\core\\cat.jpg')
        r1 = cv2.imread(r'mysite\core\cat.jpg', -1)
        r2 = cv2.cvtColor(r1, cv2.COLOR_BGR2RGB)
        axes2.imshow(r2)
        axes2.axis("off")
        axes2.set_title("Prediction")

        # Image sent in bytes and kept in a buffer
    buf = io.BytesIO()
    canvas = FigureCanvasAgg(f)
    canvas.print_png(buf)

    # Set output image type --> png
    response = HttpResponse(buf.getvalue(), content_type='image/png')

    # Clean figure
    f.clear()

    # Add file length header
    response['Content-Length'] = str(len(response.content))

    # Return the response
    return response


	

