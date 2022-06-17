# To convert the image into the data 
import pytesseract
from tqdm import tqdm
from glob import glob

all_data = pd.DataFrame(columns=['id','text','left','top','width','height'])

for files in  tqdm(filename,desc='invoice'):
    
    #files = filename[0]
    _, file_name = os.path.split(filename)
    # extract data and text 
    image = cv2.imread(file_name)
    data = pytesseract.image_to_data(image)
    dataList = list(map(lambda x: x.split('\t'),data.split('\n')))
    df = pd.DataFrame(dataList[1:],columns=dataList[0])
    df.dropna(inplace=True)
    df['conf'] = df['conf'].astype(int)

    useFulData = df.query('conf >= 30')

    # Dataframe
    invoice = pd.DataFrame()
    invoice['text'] = useFulData['text']
    invoice['id'] = filename
    invoice['left'] = useFulData['left']
    invoice['top'] = useFulData['top']
    invoice['width'] = useFulData['width']
    invoice['height'] = useFulData['height']
            
    # concatenation
    all_data = pd.concat((allinvoices,invoice))
    all_data.to_json('invoice.json',index=False)