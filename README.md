# ner-annotator

# Introduction

ner-annotator is an tools which is used to help in labeling in faster than the traditional manual tagging.

# Process 
 In this we used ocr and flask for developing the tools
 
 OCR :- OCR is an recognizing text in images, such as scanned documents and photos
 
 Flask :- Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.
 
 # Installation process
 
 - For installing the libraries open the command and write the following command :- 
```
pip3 install -r required.txt
```

- Before installing the pytesseract, first install **tesseract** by using following command :-
```
sudo apt install tesseract-ocr
 
sudo apt install libtesseract-dev 
```

- Once the above installation is done, install pytessract via given command 
```
pip install pytesseract

# Directory Structure 

### Place the Files and Directories as bellow structure to avoid error

<pre>
.
├── Annotator
│   ├── app.py
│  
├── Annotator/static
│   ├── css
│   ├── js
│   ├── uploader
│   ├── uploads
│   
├── Annotator/templates
│   ├── index.html
│   ├── upload.html
│   ├── display.html
|
└── app/templates
    ├── index.html
    ├── predictions.html
    ├── scanner.html
    
 </pre>
 app.py :- In this file, it contains all the libraries and function which are used to upload image and run the pytesseract and save into the json format.
 
 ![Screenshot from 2022-06-21 16-06-37](https://user-images.githubusercontent.com/37176796/174780615-7dc53819-5bfc-4fa1-838b-1bf185f4b119.png)
 
![Screenshot from 2022-06-21 12-44-46](https://user-images.githubusercontent.com/37176796/174780638-80d220d2-b221-44a7-bc7f-dab5acba2193.png)


 
