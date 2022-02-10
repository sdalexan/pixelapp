from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from PIL import Image
import pandas as pd
  
#converts RGB to HEX
def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b) 

#create to data file from image
def getfile(request):  
    im = Image.open(request)  
    pix = im.load()
    imageWidth = im.size[0]
    imageHeight = im.size[1]
    df_size = pd.DataFrame([['Width', imageWidth], ['Height', imageHeight]], columns = ['Width', 'Height'])
    pixalsHEX = []
    ID = 1
    for width in range(imageWidth):
        for height in range(imageHeight):
            pixalRGB = pix[width, height]
            pixalHEX = rgb2hex(pixalRGB[0], pixalRGB[1], pixalRGB[2])
            row = (ID, pixalHEX, height, width)
            pixalsHEX.append(row)
            ID = ID + 1
            df_pixalsHEX = pd.DataFrame(pixalsHEX, columns = ['ID', 'HEX', 'Y', 'X'])
            Hex_Size = df_pixalsHEX.groupby('HEX').size().reset_index(name='COUNT')
            df_Hex_Size = pd.DataFrame(Hex_Size, columns = ['HEX','COUNT'])
            df_data = df_pixalsHEX.merge(df_Hex_Size, on='HEX', how='left')
            df_data = pd.DataFrame(df_data, columns = ['ID', 'HEX', 'Y', 'X', 'COUNT'])
            df_sorted = df_data.sort_values(by=['COUNT', 'HEX'], ascending=True)
            df_data = pd.merge(df_sorted, df_data, left_index=True, right_index=True)
    df_data.to_csv('media/data/data.csv')
    df_size.to_csv('media/data/size.csv')
    return redirect('image_upload')
    


# Create your views here.
def hotel_image_view(request):
  
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
  
        if form.is_valid():
            getfile(request.FILES['file'])
    else:
        form = UploadFileForm()
    return render(request, 'image_form.html', {'form' : form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')


# Python program to view 
# for displaying images
def display_hotel_images(request):
    if request.method == 'GET':
  
        # getting all the objects of hotel.
        # Hotels = Hotel.objects.all() 
        return render((request, 'display_hotel_images.html', {'hotel_images' : "test"}))






