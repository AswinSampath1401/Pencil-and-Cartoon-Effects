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
<li><i>Apply Median Blur to blur the Image</li>
<li><i>Apply Apaptive Treshold for a min_treshold which opencv adjusts automatically</li>
<li><i>Edges are finally obtained from Adaptive Treshold</li>
<br>

### <b><u>Final  Result</b></u>
<li><i>Bitwise And of the Image with Sharp edges and Blurred Color image will give us a nice Cartoonized Image</i></li>
<br>

### <a href='Markdown\demo.md'>Click here to see demo</a>

