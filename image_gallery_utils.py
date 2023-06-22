import os


def get_image_gallery():
  files = [
    f for f in os.listdir('./arquivos')
    if os.path.isfile(os.path.join('./arquivos', f))
    and os.path.splitext(f)[1].lower() in ['.jpg', '.jpeg', '.png']
  ]
  gallery = ''
  for f in files:
    url = f'/arquivos/{f}'
    gallery += f'<a href="{url}" target="_blank"><img src="{url}" alt="{f}" width="200"></a>'
  if gallery:
    gallery = '<hr><h2>Galeria de Imagens</h2>' + gallery
  return gallery
