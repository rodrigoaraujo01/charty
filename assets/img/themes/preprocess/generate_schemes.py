from PIL import Image
import os

def rgb2hex(r,g,b):
    return "{:02x}{:02x}{:02x}".format(r,g,b)



base_str = """<div class="col-sm-4 mb-4">
    <a href="$scheme">
        <p class="text-center"><strong>$theme_name</strong></p>
        <img src="assets/img/themes/$img_name" class="img-fluid rounded" alt="">
    </a>
</div>"""

all_img = os.listdir()
all_img.sort()
for img_name in all_img:
    if ".py" in img_name or img_name == ".DS_Store":
        continue
    theme_name = img_name[:-4]
    base_colors = 3
    if len(theme_name) > 6:
        base_colors = 4
    if theme_name == "mike_was_right" or theme_name == "OrderedPastel":
        base_colors = 0
    img = Image.open(img_name)
    pix = img.load()
    x = 45
    scheme = f"charty://add-theme?name={theme_name}&baseColors={base_colors}&colors="
    last_color = ""
    count = 0
    for i in range(10):
        color = pix[x,75]
        x += 90
        new_color = rgb2hex(color[0], color[1], color[2])
        if new_color != last_color:
            count += 1
            scheme += new_color
            if i != 9:
                scheme += ","
        last_color = new_color
    if scheme[-1] == ",":
        scheme = scheme[:-1]
    if count == 5:
        scheme = scheme.replace("baseColors=3", "baseColors=0")
        scheme = scheme.replace("baseColors=4", "baseColors=0")
    new_column = base_str.replace("$scheme", scheme)
    new_column = new_column.replace("$theme_name", theme_name)
    new_column = new_column.replace("$img_name", img_name)
    print(new_column)