import base64
import json
import shutil  
import os  

directory = "image_data/test_images/"

for filename in os.listdir(directory):
    file_dir = os.path.join(directory, filename)
    file_name, ext = os.path.splitext(filename)
    image = open(file_dir, 'rb')
    image_data = image.read()
    b64_encoded_string = open(file_name+".json", "w")
    data = {"image_data" : base64.b64encode(image_data).decode('utf-8')}
    json.dump(data, b64_encoded_string)
    b64_encoded_string.close()
    shutil.move(file_name + ".json",
                "image_data/b64string/"+file_name + ".json")



