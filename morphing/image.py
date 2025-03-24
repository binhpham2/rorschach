from PIL import Image # type: ignore

class ImageTransformation:
    def __init__(self):
        pass

    def help(self):
        print("ImageTransformation module:...")
    
    def load(self, path):
        image = Image.open(path).convert("RGBA")
        return (image, image.getdata())
    
    def save(self, image, data, path):
        image.putdata(data)
        image.save(f"{path}", "PNG")
        return None

    def transform(self, input_path, output_path, transform_pixel):
        # Load current image and decode it into list of pixels
        image, image_data = self.load(input_path)

        # Transform the image pixel by pixel and save the results
        new_image_data = []
        for pixel in image_data:
            new_pixel = transform_pixel(pixel)
            new_image_data.append(new_pixel)

        # Save the transformed image
        self.save(image, new_image_data, output_path)
        return None