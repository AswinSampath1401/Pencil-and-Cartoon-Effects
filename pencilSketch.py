# Convert an Image to Pencil Sketch
import cv2
import os

folder = 'ENTER FOLDER PATH' # Sample -> 'Content\\Random_2'
output_folder = 'Content\Pencil Theme\Dodge' #Output Folder


def dodge(image,mask):
    return cv2.divide(image,255-mask,scale=256)

def burn(image,mask):
    return 255-cv2.divide(255-image,255-mask,scale=256)

def pencilSketch(imagefile):
    path = os.path.join(folder,imagefile)
    img = cv2.imread(path)
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    #Get the neagtive
    neg = 255-gray
    

    # Apply a Gaussian Blur
    blur = cv2.GaussianBlur(neg,ksize=(21,21),sigmaX=0,sigmaY=0)
    
    blend = dodge(gray,blur)
    
    return blend



def load_images_from_folder(folder):
    images=[]
    filenames=[]
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        filenames.append(filename)
        if img is not None:
            images.append(img)
    return images,filenames

images,filenames = load_images_from_folder(folder)


for imagefile in filenames:
    output_image = pencilSketch(imagefile)
    cv2.imwrite(os.path.join(output_folder,imagefile+'.jpg'),output_image)
