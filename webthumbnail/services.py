#-* coding:UTF-8 -*      
'''
Created on 2013年8月29日

@author: ezioruan
'''
from bottle import route, run,request,static_file
import uuid
import setting
import os
from task import capture_cmd
import time


@route('/webshot',method='POST')
def upload():
    template  = request.files.get('template')
    width = request.forms.get('width')
    height = request.forms.get('height')
    content = template.file.read()
    file_name = str(uuid.uuid1()) + ".png"
    file_path = os.path.join(setting.STATIC_DIR,file_name)
    capture_cmd(content, file_path, width, height)
    time.sleep(setting.TIME_OUT)
    return static_file(file_name,setting.STATIC_DIR)

@route('/webshot',method='GET')
def webthumb():
    return """
         <form action="/webshot" method="post" enctype="multipart/form-data">
          Width:      <input type="text" name="width" /></br>
          Height:      <input type="text" name="height" /></br>
          Select a file: <input type="file" name="template" />
          <input type="submit" value="Start upload" />
        </form>
    """



run(host=setting.HOST, port=setting.PORT)