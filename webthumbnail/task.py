# -* coding:UTF-8 -*      
'''
Created on 2013年8月30日

@author: ezioruan
'''
import subprocess
import base64
import time    
import setting
import os
import signal

def capture_cmd(content, file_path, width, height):
    cmd = "exec python webthumbnail.py --content %s --out %s --width %s --height %s"  % (base64.b64encode(content), file_path, width, height)
    print cmd
    p = subprocess.Popen(cmd,shell=True)
    time.sleep(setting.TIME_OUT)
    try:
        p.kill()
    except Exception, e:
        print e
        print 'pid',p.pid
        pass

    



