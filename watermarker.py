from moviepy.editor import ImageClip, TextClip, CompositeVideoClip
import os

watermark = "watermarker by azsry"

textclips = []

img_path = str(input("Drag the image you want to be watermarked into this window: "))
save_folder = os.path.dirname(img_path)
filename = os.path.splitext(os.path.basename(img_path))[0]
image = ImageClip(img_path)

ypos = -image.h

while ypos <= image.h:
    xpos = -image.w
    while xpos <= image.w:
        text = TextClip(watermark, fontsize=36, color='white')  
        text_masked = text.add_mask().rotate(30).set_opacity(0.1).set_position((xpos,ypos))

        textclips.append(text_masked)

        xpos = xpos + text.w
    ypos = ypos + (text.h * 2)

result = CompositeVideoClip([image, *textclips])
result.save_frame(f"{save_folder}\\{filename}_watermarked.png")