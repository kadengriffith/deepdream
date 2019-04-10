import imageio
from os import walk

dream = 'test_dream'


GIFNAME = f'{dream}.gif'
PATH = f'dreams/{dream}/'

images = []
f_names = []

for (dirpath, dirnames, filenames) in walk(PATH):
    f_names.extend(filenames)
    break

for filename in f_names:
    images.append(imageio.imread(f'{PATH}{filename}'))


print(f'Gathered {len(f_names)} images for a gif!\n')
print('Attempting make...\n')

imageio.mimsave(GIFNAME, images, duration=0.01)

print(f'{GIFNAME} saved!\n')
