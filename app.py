from flask import Flask, request, render_template, redirect, url_for
import os
from numpy import True_
from werkzeug.utils import secure_filename
import pytesseract
import data_gen

app = Flask(__name__)


@app.route('/')
def index():
    path = 'static/uploads/'
    uploads = sorted(os.listdir(path), key=lambda x: os.path.getctime(
        path+x))        # Sorting as per image upload date and time
    print(uploads)

    uploads = ['uploads/' + file for file in uploads]
    uploads.reverse()

    # Pass filenames to front end for display in 'uploads' variable
    return render_template('upload.html', uploads=uploads)


app.config['UPLOAD_FOLDER'] = 'static/uploads'             # Storage path


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def home():
    return render_template('upload.html')


@app.route('/display')
def display():
    return render_template('display.html')


@app.route("/upload", methods=['POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        print(f.filename)

        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # Redirect to route '/' for displaying images on front end
        return redirect("/display")
    
# @app.route("/json",methods = ['GET','POST'])
# def upload_json():
#     all_data = pd.DataFrame(columns=['id','text','left','top','width','height'])

#     for files in  tqdm(filename,desc='invoice'):
    
#         #files = filename[0]
#         _, file_name = os.path.split(filename)
#         # extract data and text 
#         image = cv2.imread(file_name)
#         data = pytesseract.image_to_data(image)
#         dataList = list(map(lambda x: x.split('\t'),data.split('\n')))
#         df = pd.DataFrame(dataList[1:],columns=dataList[0])
#         df.dropna(inplace=True)
#         df['conf'] = df['conf'].astype(int)

#         useFulData = df.query('conf >= 30')

#         # Dataframe
#         invoice = pd.DataFrame()
#         invoice['text'] = useFulData['text']
#         invoice['id'] = filename
#         invoice['left'] = useFulData['left']
#         invoice['top'] = useFulData['top']
#         invoice['width'] = useFulData['width']
#         invoice['height'] = useFulData['height']
        
#         # concatenation
#         all_data = pd.concat((allinvoices,invoice))
#         all_data.to_json('invoice.json',index=False)
#         return render_template("display.html")



if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
