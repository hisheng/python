import tensorflow as tf
import os
import matplotlib.pyplot as plt


# num_skipped = 0
# for folder_name in ("Cat", "Dog"):
#     print(folder_name)
#     folder_path = os.path.join("PetImages", folder_name)
#     print(folder_path)
#     for fname in os.listdir(folder_path):
#         print(fname)
#         fpath = os.path.join(folder_path, fname)
#         print(fpath)
#         try:
#             fobj = open(fpath, "rb")
#             is_jfif = tf.compat.as_bytes("JFIF") in fobj.peek(10)
#         finally:
#             fobj.close()
#
#         if not is_jfif:
#             num_skipped += 1
#             os.remove(fpath)
#
# print("Deleted %d images" % num_skipped)

image_size = (180, 180)
batch_size = 32

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "PetImages", validation_split=0.2, subset="training", seed=1337, image_size=image_size, batch_size=batch_size,
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "PetImages", validation_split=0.2, subset="validation", seed=1337, image_size=image_size, batch_size=batch_size,
)

for item in train_ds:
    print(item)

plt.figure(figsize=(10, 10))
for images, labels in train_ds.take(1):
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(int(labels[i]))
        plt.axis("off")



