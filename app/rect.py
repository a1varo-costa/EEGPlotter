from PyQt5 import QtWidgets, QtGui, QtCore


class BlinkRect(QtWidgets.QLabel):
    def __init__(self, parent=None, label=None, w=128, h=128, sqsz=16, freq=1):
        super().__init__(parent=parent)
        
        self.pixmapWidth = w
        self.pixmapHeight = h
        self.sqsz = sqsz
        self.rects = []
        self.txtLabel = label
        
        self.pixmap1 = QtGui.QPixmap(self.pixmapWidth+1, self.pixmapHeight+40)
        self.pixmap1.fill()
        self.pixmap2 = QtGui.QPixmap(self.pixmapWidth+1, self.pixmapHeight+40)
        self.pixmap2.fill()
        self.__prevColor = 1  # 1 = black   -1 = white
        self.__pmActive = 1   # 1 = pixmap1  2 = pixmap2

        self._setupPixmaps()

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self._blink)
        self.timer.start(int(1000 * 1/freq))


    def _setupPixmaps(self):
        self._createRects(self.pixmapWidth, self.pixmapHeight, self.sqsz)
        
        self._drawRects(self.sqsz, self.pixmap1)
        self.__prevColor = -self.__prevColor
        self._drawRects(self.sqsz, self.pixmap2)


    def _blink(self):
        if self.__pmActive == 1:
            self.setPixmap(self.pixmap2)
            self.__pmActive = 2
        else:
            self.setPixmap(self.pixmap1)
            self.__pmActive = 1


    def _drawRects(self, h_, pixmap):
        painter = QtGui.QPainter(pixmap)
        painter.setPen(QtCore.Qt.black)
        
        brushWhite = QtGui.QBrush(QtCore.Qt.white)
        brushBlack = QtGui.QBrush(QtCore.Qt.black)

        for row in self.rects:
            self.__prevColor = -self.__prevColor

            for rect in row:
                if self.__prevColor == 1:
                    painter.setBrush(brushWhite)
                    self.__prevColor = -1
                else:
                    painter.setBrush(brushBlack)
                    self.__prevColor = 1
                painter.drawRect(rect)

        letterRect = QtCore.QRectF(0, self.pixmapHeight, self.pixmapWidth-1, 40)
        painter.drawText(letterRect, QtCore.Qt.AlignCenter, self.txtLabel)
        painter.end()
      

    def _createRects(self, w, h, sqsz):
        self.rects = [
                [QtCore.QRectF(i, j, sqsz, sqsz) for i in range(0, w, sqsz)] \
                    for j in range(0, h, sqsz)
            ]
