class PixelTransformation:
    def __init__(self):
        pass

    def help(self):
        print("PixelTransformation module:...")

    def make_light_pixel_transparent(self, pixel):
        # Light threshold
        threshold = 200
        
        # If all 3 R, G, B values are greater than the threshold, clear the pixel.
        # If not, keep the pixel as is.
        if (pixel[0] > threshold and pixel[1] > threshold and pixel[2] > threshold) or (pixel[0]+pixel[1]+pixel[2]>250 and pixel[1]>100):
            return (0, 0, 0, 0)
        else:
            return pixel
        
    def make_dark_pixel_transparent(self, pixel):
        # Light threshold
        threshold = 300
        
        # If all 3 R, G, B values are greater than the threshold, clear the pixel.
        # If not, keep the pixel as is.
        if pixel[0] + pixel[1] + pixel[2] < threshold:
            return (0, 0, 0, 0)
        else:
            return pixel
        
    def make_light_pixel_white(self, pixel):
        # Light threshold
        threshold = 50
        
        # If all 3 R, G, B values are greater than the threshold, clear the pixel.
        # If not, keep the pixel as is.
        if pixel[0] + pixel[1] + pixel[2] > threshold:
            return (255, 255, 255, pixel[3])
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
        
    def make_all_pixel_white(self, pixel):
        # Color sum threshold
        threshold = 100
        
        # If all 3 R, G, B values are greater than the threshold, make it white.
        # If not, keep the pixel as is.
        if pixel[3] > threshold:
            return (255, 255, 255, 255)
        else:
            return pixel
        
    def blur_pixel(self, pixel):
        # Alpha indicator (0-255)
        alpha = 50
        if pixel[3] == 0:
            return (0, 0, 0, 0)
        else:
            return (pixel[0], pixel[1], pixel[2], alpha)