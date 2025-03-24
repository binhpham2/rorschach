class PixelTransformation:
    def __init__(self):
        pass

    def help(self):
        print("PixelTransformation module:...")

    def make_light_pixel_transparent(self, pixel):
        # Light threshold
        threshold = 10
        
        # If all 3 R, G, B values are greater than the threshold, clear the pixel.
        # If not, keep the pixel as is.
        if (pixel[0] > threshold and pixel[1] > threshold and pixel[2] > threshold) or (pixel[0]+pixel[1]+pixel[2]>250 and pixel[1]>100):
            return (0, 0, 0, 0)
        else:
            return pixel
        
    def make_light_pixel_white(self, pixel):
        # Light threshold
        threshold = 600
        
        # If all 3 R, G, B values are greater than the threshold, clear the pixel.
        # If not, keep the pixel as is.
        if pixel[0] + pixel[1] + pixel[2] > threshold:
            return (100, 100, 100)
        else:
            return pixel
        
    def make_dark_pixel_white(self, pixel):
        # Light threshold
        threshold = 1
        
        # If all 3 R, G, B values are greater than the threshold, clear the pixel.
        # If not, keep the pixel as is.
        if pixel[3] >= threshold:
            return (255, 255, 255)
        else:
            return pixel
        
    def blur_pixel(self, pixel):
        # Alpha indicator (0-255)
        alpha = 50
        if pixel[3] == 0:
            return (0, 0, 0, 0)
        else:
            return (pixel[0], pixel[1], pixel[2], alpha)