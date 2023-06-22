import os


def get_file_list():
  files = [
    f for f in os.listdir('./arquivos')
    if os.path.isfile(os.path.join('./arquivos', f))
  ]
  file_groups = {}
  for f in files:
    ext = os.path.splitext(f)[1]
    if ext.lower() == '.pdf':
      file_groups.setdefault('PDF', []).append(f'/arquivos/{f}')
    elif ext.lower() == '.txt':
      file_groups.setdefault('TXT', []).append(f'/arquivos/{f}')
    elif ext.lower() in ['.jpg', '.jpeg']:
      file_groups.setdefault('JPG', []).append(f'/arquivos/{f}')
  file_list = ''
  for ext, urls in file_groups.items():
    if ext == 'PDF' or ext == 'TXT':
      file_list += f'<h3>{ext}</h3><ul>'
      for url in urls:
        filename = os.path.basename(url)
        file_list += f'<li><a href="{url}">{filename}</a></li>'
      file_list += '</ul>'
  return file_list
