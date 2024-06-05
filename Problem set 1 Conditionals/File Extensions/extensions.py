
filee = input("File name: ").strip().lower()

extension = ""

#check if "." is present in file or not. If present, extract extension from file. If not present, let extension be "octet-stream"
dot_index = filee.find('.')
if dot_index != -1:
    extension = filee[dot_index+1:]
    #check if extensions again contains "." i.e. dual extension. In this case, we have to consider last extension as main extension of a file...
    if extension.find('.') != -1:
        extension = extension[extension.find('.')+1:]

#if extensions are belongs to type "image"
if extension == "gif" or extension == "jpeg" or extension == "png":
    print(f"image/{extension}")
elif extension == "jpg":
    extension = "jpeg"
    print(f"image/{extension}")

#if extensions are belongs to type "document"
elif extension == "pdf" or extension == "zip":
    print(f"application/{extension}")

#if extensions are belongs to type "text"
elif extension == "txt":
    print(f"text/{filee[:dot_index]}")

#if extensions are not belongs to given extensions...
else:
    extension = "octet-stream"
    print(f"application/{extension}")
