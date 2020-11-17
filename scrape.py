import time
import requests as rq
import os

if not os.path.isdir('poke_images'):
    os.mkdir('poke_images')


def convert_int_to_triple_0(num):
    return str(num).zfill(3)


# downloads images from https://www.pokemon.com/us/pokedex/
def write_images(image_count):
    image_hyperlink = 'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/{}.png'
    for i in range(1, image_count + 1):
        img_link = image_hyperlink.format(convert_int_to_triple_0(i))
        image = rq.get(img_link).content
        with open('poke_images/' + convert_int_to_triple_0(i) + '.jpg', 'wb+') as f:
            f.write(image)
        time.sleep(.1)


write_images(151)
