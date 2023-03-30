from desktop import Utils
from desktop import Image_Enhancement
import matplotlib.pyplot as plt
from desktop import Extract_Keypoints


class ImageCollation:
    def __init__(self, images_path):
        self.imagesPath = images_path

    def stitching(self):
        # getting Images
        image_loading_object = Utils.ReceiveImages(self.imagesPath)
        image_list = image_loading_object.load_images()
        # Plotting Final Stitched Image
        plt.figure(figsize=(10, 10))
        plt.title('Image After Collation')
        plt.imshow(Extract_Keypoints.extract_keypoints(image_list))
        plt.show()

    def image_enhancement(self):
        image_enhancement_object = Image_Enhancement.Enhancement(self.imagesPath)
        image_enhancement_object.enhance_image()