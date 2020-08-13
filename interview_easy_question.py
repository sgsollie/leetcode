
# left_images: [(timestamp: int, image: bytes), ...]
# right_images: [(timestamp: int, image: bytes), ...]

# output images: [(timstamp: int, image_left: bytes, image_right: bytes), ...]

def merge_images(left_images,right_imgaes):
    output_images = []
    for i in range(len(left_images)):
        triple = (,)
        triple.append(left_images[i][0])
        triple.append(left_images[i][1])
        triple.append(right_images[i][1])
        output_images.append(triple)
    return output_images