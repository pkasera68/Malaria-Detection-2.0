from flask import render_template,url_for, redirect, request,flash
from Project import app
from Project.forms import ImageForm
#imports for machine learning
import pandas as pd
import numpy as np
#from sklearn.externals import joblib
import joblib
#imports for dataset generation
import cv2,os
import numpy as np
from PIL import Image

def transformImage(im):
    i = Image.open(im)
    num_im=np.array(i)
    im = cv2.GaussianBlur(num_im, (5, 5), 2)
    im_gray = cv2.cvtColor(num_im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(im_gray, 127, 255, 0)
    cc, _ = cv2.findContours(thresh, 1, 2)
    contours=np.array([])
    for i in range(5):
        try:
            area = cv2.contourArea(cc[i])
            contours=np.append(contours,area)
        except:
            contours=np.append(contours,"0")

    print(contours)
    return contours

def classify(contours):
    model = joblib.load("Project/Model/rf_malaria_100_5")

    ##Step4: Make predictions and get classification report

    # you can make predictions on a supplied data as:
    # a= np.array([[123.0,145.0,23.45,0,0],[7000,0,0,0,0]])
    # predictions = model.predict(a)
    # print(predictions)
    c=np.reshape(contours, (1, 5))
    predictions = model.predict(c)
    return predictions

@app.route("/",methods=['GET','POST'])
def home():
    form_obj = ImageForm()
    if form_obj.validate_on_submit():
        contours=transformImage(form_obj.cell_img.data)
        prediction=classify(contours)
        if prediction == 'Parasitized':
            flash(f'Infected! Please consult a doctor ASAP.','danger')
        else:
            flash(f'Uninfected! You are safe.', 'success')
        return redirect(url_for('Report'))
    return render_template("home.html", title="Upload Image", form=form_obj)

@app.route("/report")
def  Report():
    return render_template("Report.html",title="Test report")