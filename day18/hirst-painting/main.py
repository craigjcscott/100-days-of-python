import colorgram

extracted_colors = colorgram.extract('image.jpg', 100)
extracted_color_tuples = []

for color in extracted_colors:
    r = color.rgb.r
    b = color.rgb.b
    g = color.rgb.g
    temp_tuple = (r, b, g)
    extracted_color_tuples.append(temp_tuple)

print(extracted_color_tuples)