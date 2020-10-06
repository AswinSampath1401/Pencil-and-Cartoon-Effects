# An Open-Cv task and Tutorial to Convert the given image to Cartoon and Pencil Sketch

# Cartoon Effect 

## Aim <br>

To cartoonize an Image by lightenting the colors and detecting sharp edges

## Procedure
Blur the image thereby lightening the colors and apply suitable filters to detect sharp edges 

## Methodology<br>
<b><u>To Lighten the Imgae</i></u></b>
<li><i>Blur The Image using Bilateral Filter</i></li><br>

<b><u> To Detect Sharp Edges</u></b>
<li><i>Convert Image to grayscale</i></li>
<li><i>Apply Median Blur to blur the Image</i></li>
<li><i>Apply Apaptive Treshold for a min_treshold which opencv adjusts automatically</i></li>
<li><i>Edges are finally obtained from Adaptive Treshold</i></li>
<br>

### <b><u>Final  Result</b></u>
<li><i>Bitwise And of the Image with Sharp edges and Blurred Color image will give us a nice Cartoonized Image</i></li>
<br>

### <a href='Markdown\Demo.md'>Click here to see demo</a>
<br>

# Pencil Effect 

## Aim <br>

To create a pencil Sketch of an Image by using basic filters

## Procedure
Apply Image Blending Techniques such as Dodging and Burning and we are good to go.

## Methodology<br>
<li><i>Convert the given image into grayscale</i></li>
<li><i> Invert the grayscale to get negative image</i></li>
<li><i>Apply Gaussian Blur to the negative image</i></li>
<li><i>Blend the grayscale image(we got from rgb image in step 1) with the blurred negative image using a color dodge</i></li>
<br>

### <b><u>Final  Result</b></u>
<li><i>A nice Pencil Sketch is generated</i></li>
<br>

### <a href='Markdown\PencilDemo.md'>Click here to see demo</a>

Trying to make a verified commit
2nd attempt
