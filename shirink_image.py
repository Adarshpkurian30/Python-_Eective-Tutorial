from images import Image

img_path = input("Enter the path to the GIF image:")
resize_factor = int(input("Enter the shrink factor:"))
original = Image(img_path)
orig_height = original.getHeight()
orig_width = original.getWidth()
resized = Image(orig_width // resize_factor, orig_height // resize_factor)

y_old = 0
new_y = 0
while y_old < orig_height - resize_factor:
    x_old = 0
    new_x = 0
    while x_old < orig_width - resize_factor:
        pixel_data = original.getPixel(x_old, y_old)
        resized.setPixel(new_x, new_y, pixel_data)
        x_old += resize_factor
        new_x += 1
    y_old += resize_factor
    new_y += 1

resized.draw()
