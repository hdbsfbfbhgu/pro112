import sys
import time
import random

import os
import shutil

from_dir = "C:\Users\chala\Downloads"              # Add the path of you "Downloads" folder.
to_dir = "C:\Users\chala\OneDrive\Desktop\downloads" #Create "Document_Files" folder in your Desktop and update the path accordingly.


dir_tree = {
 "extension":['.doc','.docx','.jpg','.pdf','.pdf']
   
}

# Event Hanlder Class

class FileMovementHandler:

    def on_created(self, event):

        name, extension = os.path.splitext(event.src_path)
       
        time.sleep(1)

        for key, value in dir_tree.items():
            time.sleep(1)

            if extension in value:

                file_name = os.path.basename(event.src_path)
               
                print("Downloaded " + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                if os.path.exists(path2):

                    print("Directory Exists...")
                    print("Moving " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

                else:
                    print("Making Directory...")
                    os.makedirs(path2)
                    print("Moving " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)



    

