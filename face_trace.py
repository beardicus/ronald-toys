#!/usr/bin/python
from chiplotle import *
from subprocess import call
from opencv.cv import *
from opencv.highgui import *

cvNamedWindow("PlottyDraw", 1)
capture = cvCreateCameraCapture(0)

orig = cvQueryFrame(capture)
grey = cvCreateImage(cvGetSize(orig), IPL_DEPTH_8U, 1)
canny = cvCreateImage(cvGetSize(grey), IPL_DEPTH_8U, 1)

def ploutput():
    # capture current frame and send it to plotter
    print "ploutputting!"
    cvSaveImage("input.png", canny)
    call(["convert", "input.png", "-negate", "inverted.png"])
    call(["autotrace", "inverted.png", "--centerline", "--output-file", "input.eps"])
    call(["pstoedit", "-f", "hpgl", "input.eps", "out.hpgl"])
#    call(["plot_hpgl_file_max_size.py", "out.hpgl"])

while True:
    orig = cvQueryFrame(capture)
    cvCvtColor(orig, grey, CV_RGB2GRAY)
    cvCanny(grey, canny, 50, 150, 3)
    cvShowImage("PlottyDraw", canny)
    key = cvWaitKey(10)
    if key == 'q':
        break
    elif key == 'p':
        ploutput()
