
import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = '/home/satvshr/Desktop/amfoss-tasks-2/pq19/catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

os.makedirs('withLogo', exist_ok=True)
# Loop over all files in the working directory.
for filename in os.listdir('/home/satvshr/Desktop/amfoss-tasks-2/pq19'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg') or filename.lower().endswith('.gif') or filename.lower().endswith('bmp')):
        continue # skip non-image files and the logo file itself

    im = Image.open('/home/satvshr/Desktop/amfoss-tasks-2/pq19/' + filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        im = im.resize((width, height))
        imWidth, imHeight = im.size

    if imWidth < logoWidth * 2 and imHeight < logoHeight * 2:
        print("Logo taking up too much space")
    
    else:
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes.
    im.save(os.path.join('withLogo', filename))