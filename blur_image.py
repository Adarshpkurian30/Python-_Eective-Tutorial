from images import Image

def smoothen(pixel_list):
    red = sum(p[0] for p in pixel_list) // 5
    green = sum(p[1] for p in pixel_list) // 5
    blue = sum(p[2] for p in pixel_list) // 5
    return (red, green, blue)

file_path = input("Enter the path to the GIF image:")
photo = Image(file_path)

for row in range(1, photo.getHeight() - 1):
    for col in range(1, photo.getWidth() - 1):
        center = photo.getPixel(col, row)
        left_px = photo.getPixel(col - 1, row)
        right_px = photo.getPixel(col + 1, row)
        top_px = photo.getPixel(col, row - 1)
        bottom_px = photo.getPixel(col, row + 1)
        blended_color = smoothen([center, left_px, right_px, top_px, bottom_px])
        photo.setPixel(col, row, blended_color)

photo.draw()
