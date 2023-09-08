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
    elif ext.lower() == '.mp3':
      file_groups.setdefault('MP3', []).append(f'/arquivos/{f}')
    elif ext.lower() == '.mp4':
      file_groups.setdefault('MP4', []).append(f'/arquivos/{f}')
    elif ext.lower() == '.doc' or ext.lower() == '.docx':
      file_groups.setdefault('Word', []).append(f'/arquivos/{f}')
    elif ext.lower() == '.xls' or ext.lower() == '.xlsx':
      file_groups.setdefault('Excel', []).append(f'/arquivos/{f}')
    elif ext.lower() == '.ppt' or ext.lower() == '.pptx':
      file_groups.setdefault('PowerPoint', []).append(f'/arquivos/{f}')
    elif ext.lower() in ['.png', '.gif', '.bmp', '.tif', '.tiff']:
      file_groups.setdefault('Imagem', []).append(f'/arquivos/{f}')
    elif ext.lower() in ['.avi', '.mpg', '.mpeg', '.mov', '.wmv']:
      file_groups.setdefault('Vídeo', []).append(f'/arquivos/{f}')
    elif ext.lower() in ['.mp3', '.wav', '.wma']:
      file_groups.setdefault('Áudio', []).append(f'/arquivos/{f}')
    elif ext.lower() == '.exe':
      file_groups.setdefault('Executável', []).append(f'/arquivos/{f}')
    elif ext.lower() == '.zip':
      file_groups.setdefault('ZIP', []).append(f'/arquivos/{f}')
    else:
      file_groups.setdefault('Outros', []).append(f'/arquivos/{f}')
  file_list = ''
  for ext, urls in file_groups.items():
    if ext in ['PDF', 'TXT', 'Word', 'Excel', 'PowerPoint', 'Imagem', 'Vídeo', 'MP3', 'MP4', 'Áudio', 'Executável', 'ZIP']:
      file_list += f'<h3>{ext}</h3><ul>'
      for url in urls:
        filename = os.path.basename(url)
        file_list += f'<li><a href="{url}">{filename}</a></li>'
      file_list += '</ul>'
  return file_list
