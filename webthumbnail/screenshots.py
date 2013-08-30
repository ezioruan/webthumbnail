#-* coding:UTF-8 -*      
'''
Created on 2013年8月29日

@author: ezioruan
'''
import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *

class ScreenShot(QWebView):
    def __init__(self):
        self.app = QApplication(sys.argv)
        QWebView.__init__(self)
        self._loaded = False
        self.loadFinished.connect(self._loadFinished)
        
    def capture(self, url, output_file,width=None, height=None):
        pass

    def _capture(self,output_file,width=None, height=None):
        self.wait_load()
        # set to webpage size
        frame = self.page().mainFrame()
        self.page().setViewportSize(frame.contentsSize())
        # render image
        image = QImage(self.page().viewportSize(), QImage.Format_ARGB32)
        painter = QPainter(image)
        frame.render(painter)
        painter.end()
        print 'saving', output_file
        image.save(output_file)

    def wait_load(self, delay=0):
        # process app events until page loaded
        while not self._loaded:
            self.app.processEvents()
            time.sleep(delay)
        self._loaded = False
        
    def scale(self, image, width=None, height=None):
        if width is None and height is None:
            scaled = image
        elif width is None:
            scaled = image.scaledToHeight(height, Qt.SmoothTransformation)
        elif height is None:
            scaled = image.scaledToWidth(width, Qt.SmoothTransformation)
        else:
            scaled = image.scaled(width, height,
                    Qt.KeepAspectRatioByExpanding,
                    Qt.SmoothTransformation)
            scaled = scaled.copy(0, 0, width, height)
        return scaled

    def _loadFinished(self, result):
        self._loaded = True


class ScreenShotURL(ScreenShot):
    def __init__(self):
        ScreenShot.__init__(self)

    def capture(self, url, output_file,width=None, height=None):
        self.load(QUrl(url))
        self._capture(output_file,width, height)
        


class ScreenShotContent(ScreenShot):
    def __init__(self):
        ScreenShot.__init__(self)

    def capture(self, content, output_file,width=None, height=None):
        self.setContent(content)
        self._capture(output_file,width, height)
        
        
scren_shot_content = ScreenShotContent()  











