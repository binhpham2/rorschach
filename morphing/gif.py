from PIL import Image, ImageSequence

class GifTransformation:
    def __init__(self):
        pass
    
    def remove_white_background(input_path, output_path):
        # Open the original GIF
        gif = Image.open(input_path)
        
        # Prepare a list to hold frames with transparent backgrounds
        frames = []
        
        # Iterate through each frame in the GIF
        for frame in ImageSequence.Iterator(gif):
            # Conversion to RGBA
            fr = frame.convert("RGBA")

            # Extract pixel data
            datas = fr.getdata()
            new_data = []
            
            # Replace white with transparency
            for item in datas:   
                # If the pixel is white, make it transparent
                if item[0] > 50 and item[1] > 50 and item[2] > 50:  # Threshold for white
                    new_data.append((255, 255, 255, 0))  # Transparent pixel
                else:
                    new_data.append(item)

            # Apply the new data to the frame
            fr.putdata(new_data)
            
            # Append the processed frame to the frames list
            frames.append(fr)

        # Save the processed frames as a new GIF
        frames[0].save(output_path, save_all=True, append_images=frames[1:], loop=0)