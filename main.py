import os

from PIL import Image


for i in range(5):
    file_path = f"photo_{i}"
    if not os.path.isdir(file_path):
        os.mkdir(file_path)
    photo = Image.open(f"Kartinky/photo_{i}.jpg")
    vk_photo = photo.resize((1400, 1000))
    vk_photo.save(f"{file_path}/photo_{i}_vk.png")
    instagram_photo = photo.resize((1080, 1080))
    instagram_photo.save(f"{file_path}/photo_{i}_instagram.png")
    facebook_photo = photo.resize((1200, 628))
    facebook_photo.save(f"{file_path}/photo_{i}_facebook.png")
    coordinates = (10, 0, photo.width - 10, photo.height)
    photo = photo.crop(coordinates)