This directory stores script to convert Image data to b64encoded string 

Steps to generate the b64encoded string

    Put all the Images into the /image_data/test_images directory
    Run the script imgtostring.py

This will generate a __b64string__ as a json with same filename and place it
in **/image_data/b64stringjson** directory

These json file will be used in hitting the API.

For testing purpose, a test string **phototest.json** is already placed inside the **/image_data/b64stringjson** directory








