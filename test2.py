import os

def list_file(abspath):
    files = set()
    subs = os.listdir(abspath)
    for sub in subs:
        f = os.path.join(abspath, sub)
        if os.path.isfile(f):
            files.add(f)
        elif os.path.isdir(f):
            files |= list_file(f)
    return files

def filter_type(files, types):
    types = set(types)
    return (file for file in files if file.split('.')[-1].lower() in types)
    
for file in  sorted(filter_type(list_file(r"m:/v/"), {'mp4'})):
    file_renamed = file.replace('mp3', 'mp4')
    os.rename(file, file_renamed)
    print('{} => {}'.format(file, os.path.basename(file_renamed)))