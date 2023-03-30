# We can use the function glob.glob() or glob.iglob() directly from glob module to retrieve paths recursively
# from inside the directories/files and subdirectories/subfiles.
import cv2
import glob


class ReceiveImages:
    def __init__(self, images_path):
        self.images_path = images_path

    def load_images(self):
        path = sorted(glob.glob(self.images_path + "/*.jpg"))
        image_list = []
        for Image in path:
            n = cv2.imread(Image)
            image_list.append(n)
        return image_list
