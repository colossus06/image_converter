from PIL import Image
import glob

print(glob.glob("*.png"))
for file in glob.glob("*png"):
    im = Image.open(file)
    jpg_im = im.convert("RGB")
    jpg_im.save(file.replace("png", "jpg"), quality = 95)


