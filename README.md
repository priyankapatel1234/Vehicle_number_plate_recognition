<center><b><h1>Steps Involved In Vehicle Number Plate Recognition:</h1></b></center><br>
<b>1.Vehicle Number Plate Recognition:</b> The first step is to detect the number plate from the vehicle. We will use the contour option in OpenCV to detect for rectangular objects to find the number plate. The accuracy can be improved if we know the exact size, color and approximate location of the number plate. Normally the detection algorithm is trained based on the position of camera and type of number plate used in that particular country. This gets trickier if the image does not even have a car, in this case we will an additional step to detect the car and then the license plate.<br><br>
<b>2. Character Segmentation:</b> Once we have detected the Number  Plate we have to crop it out and save it as a new image. Again this can be done easily using OpenCV.<br><br>
<b>3. Character Recognition:</b> New image that we obtained in the previous step is sure to have some characters (Numbers/Alphabets) written on it. So, we can perform OCR (Optical Character Recognition) on it to detect the number.<br><br>
<h1>Output:</h1>

<img src="images/car2.jpg" alt="image not found" width="900"  height="500">

<br><br>
<img src="images/scr.png" alt="image not found" width="900" height="500">
