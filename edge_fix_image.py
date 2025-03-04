from images import Image

def compute_intensity(rgb_values):
    return sum(rgb_values) // 3

file_path = input("Enter the path to the GIF image:")
sensitivity = int(input("Enter the threshold amount:"))
black = (0, 0, 0)
white = (255, 255, 255)
image = Image(file_path)

for row in range(1, image.getHeight() - 1):
    for col in range(1, image.getWidth() - 1):
        current_pixel = image.getPixel(col, row)
        adjacent_left = image.getPixel(col - 1, row)
        adjacent_down = image.getPixel(col, row + 1)
        curr_intensity = compute_intensity(current_pixel)
        left_intensity = compute_intensity(adjacent_left)
        down_intensity = compute_intensity(adjacent_down)
        
        if abs(curr_intensity - left_intensity) > sensitivity or abs(curr_intensity - down_intensity) > sensitivity:
            image.setPixel(col, row, black)
        else:
            image.setPixel(col, row, white)

image.draw()
