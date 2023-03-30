import cv2
import numpy as np


def warped_image(image1, image2, h):
    rows1, columns1 = image1.shape[:2]
    rows2, columns2 = image2.shape[:2]

    list_of_points_one = np.float32([[0, 0], [0, rows1], [columns1, rows1], [columns1, 0]]).reshape(-1, 1,
                                                                                                    2)  # coordinates
    # of a reference image
    temporary_points = np.float32([[0, 0], [0, rows2], [columns2, rows2], [columns2, 0]]).reshape(-1, 1,
                                                                                                  2)  # coordinates
    # of second image

    # Warp perspective after establishing homography
    # Change field of view
    list_of_points_two = cv2.perspectiveTransform(temporary_points, h)  # calculate the transformation matrix

    list_of_points = np.concatenate((list_of_points_one, list_of_points_two), axis=0)

    [x_min, y_min] = np.int32(list_of_points.min(axis=0).ravel() - 0.5)
    [x_max, y_max] = np.int32(list_of_points.max(axis=0).ravel() + 0.5)

    translation_distance = [-x_min, -y_min]

    h_translation = np.array([[1, 0, translation_distance[0]], [0, 1, translation_distance[1]], [0, 0, 1]])

    output_image = cv2.warpPerspective(image2, h_translation.dot(h), (x_max - x_min, y_max - y_min))
    output_image[translation_distance[1]:rows1 + translation_distance[1],
    translation_distance[0]:columns1 + translation_distance[0]] = image1

    return output_image
