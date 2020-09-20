import cv2
import matplotlib
import matplotlib.pyplot as plt
import os


folder="Content\Resource"
output_folder = "Content\Cartoon Theme" 
def cartoonify(imgagefile):
    path = os.path.join(folder,imagefile)
    img=cv2.imread(path)
    #Apply Bilateral Filter
    col_img = cv2.bilateralFilter(img,5,255,255)
    #Convert Image from bgr to gray
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #Apply Median Blur
    gray = cv2.medianBlur(gray,3)

    #get the edges
    edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,5)

    #Bitwise And of bilateral filter and mask is edges
    cartoon = cv2.bitwise_and(col_img,col_img,mask=edges)
    return cartoon



def load_images_from_folder(folder):
    images = []
    filenames=[]
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        filenames.append(filename)
        if img is not None:
            images.append(img)
    return images,filenames



images,filenames = load_images_from_folder(folder)

#print(filenames)
count=0
for imagefile in filenames:
    output_image = cartoonify(imagefile)
    cv2.imwrite(os.path.join(output_folder,imagefile+'.jpg'),output_image)
    

