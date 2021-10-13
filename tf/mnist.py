import tensorflow as tf

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test, y_test, verbose=2)

model.predict()

dataset = []
mapping = {"dogs": 0, "cats": 1}
count = 0
import tensorflow as tf

for file in os.listdir(directory):
    if file != '.DS_Store':
        path = os.path.join(directory, file)
        for im in os.listdir(path):
            if im != '_DS_Store':
                image = tf.keras.preprocessing.image.load_img(os.path.join(path, im), grayscale=False, color_mode='rgb',
                                                              target_size=(48, 48))
                image = tf.keras.preprocessing.image.img_to_array(image)
                image = image / 255.0
                dataset.append([image, count])
                count += 1
print(dataset)
