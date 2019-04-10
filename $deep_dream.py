from deepdreamer import model, load_image, recursive_optimize
import numpy as np
import PIL.Image

import cv2
import os

layer_tensor = model.layer_tensors[3]

dream_name = "test_dream"

# Testing
x_size = 800
y_size = 400
#

# 4k
# x_size = 4069
# y_size = 2008
#

created_count = 0
max_count = 50

for i in range(9999999):
    image_number = i

    path_to_next_dreamed_image = f"dreams/{dream_name}/img_{image_number + 1}.jpg"
    path_to_this_image = f"dreams/{dream_name}/img_{image_number}.jpg"

    if os.path.isfile(path_to_next_dreamed_image):
        print(f'{path_to_next_dreamed_image} already exists, checking next...')

    else:
        img_result = load_image(filename=path_to_this_image)

        x_trim = 2
        y_trim = 1

        img_result = img_result[0+x_trim:y_size-y_trim, 0+y_trim:x_size-x_trim]
        img_result = cv2.resize(img_result, (x_size, y_size))

        img_result[:, :, 0] += 3
        img_result[:, :, 1] += 3
        img_result[:, :, 2] += 3

        img_result = np.clip(img_result, 0.0, 255.0)
        img_result = img_result.astype(np.uint8)

        img_result = recursive_optimize(layer_tensor=layer_tensor,
                                        image=img_result,
                                        num_repeats=1,
                                        rescale_factor=0.3,
                                        blend=0.2,
                                        num_iterations=20,
                                        step_size=1,
                                        tile_size=5)

        img_result = np.clip(img_result, 0.0, 255.0)
        img_result = img_result.astype(np.uint8)
        result = PIL.Image.fromarray(img_result, mode='RGB')
        result.save(path_to_next_dreamed_image)

        created_count += 1

        if created_count >= max_count:
            print('\n')
            break
