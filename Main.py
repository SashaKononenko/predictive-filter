import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt
 
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication, QInputDialog, QLabel,QTextEdit,QComboBox)
from PyQt5.QtGui import QFont

import numpy 


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        central_widget = QWidget(self)
        #self.setCentralWidget(central_widget)
        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)
        central_widget.move(0,20)
        central_widget.resize(800,500)
        
        btn = QPushButton('Прогнозуватися', self)
        btn.setToolTip('')
        btn.resize(btn.sizeHint())
        btn.move(0, 0)
        btn.clicked.connect(self.prog)
        self.setGeometry(50, 50, 800, 600)
        self.setWindowTitle('Курсова')    
        self.show()
    def prog(self):
        print('asdasd')
        data = [10,15,13,19,14,18,17,11]
        print('дані:',data)
        print('Складаємо систему умовних рівнянь Гауса.')
        i = 0
        while i < len(data):
            if i>=2:
                print(data[i],'=a0 + a1*',data[i-2],'+a2*',data[i-1],'+a3*',data[i-2],'*',data[i-1],',')
            i = i +1 
        i = 0
        res = [0,0,0,0]
        r1 = [1,1,1,1,1]
        s = [0,0,0,0,0]
        while i < len(data):
            if i>=2:
                r1[0] = r1[0]*data[i]
                r1[2] = r1[2]*data[i-2]
                r1[3] =r1[3]*data[i-1]
                r1[4] =  r1[4]*data[i-1]*data[i-2]
                s[0] = s[0] + r1[0]
                s[1] = s[1] + r1[1]
                s[2] = s[2] + r1[2]
                s[3] = s[3] + r1[3]
                s[4] = s[4] + r1[4] 
                r1 = [1,1,1,1,1]
            i = i +1 
        print(s)
        res[0] = s
        
        r1 = [1,1,1,1,1]
        s = [0,0,0,0,0]
        i = 0
        while i < len(data):
            if i>=2:
                r1[0] = r1[0]*data[i]*data[i-2]
                r1[1] = r1[1]*data[i-2]
                r1[2] = r1[2]*data[i-2]*data[i-2]
                r1[3] = r1[3]*data[i-1]*data[i-2]
                r1[4] = r1[4]*data[i-1]*data[i-2]*data[i-2]
                print('--:',r1)
                s[0] = s[0] + r1[0]
                s[1] = s[1] + r1[1]
                s[2] = s[2] + r1[2]
                s[3] = s[3] + r1[3]
                s[4] = s[4] + r1[4] 
                r1 = [1,1,1,1,1]
            i = i +1 
        print(s)
        res[1] = s

        r1 = [1,1,1,1,1]
        s = [0,0,0,0,0]
        i = 0
        while i < len(data):
            if i>=2:
                r1[0] = r1[0]*data[i]*data[i-1]
                r1[1] = r1[1]*data[i-1]
                r1[2] = r1[2]*data[i-2]*data[i-1]
                r1[3] = r1[3]*data[i-1]*data[i-1]
                r1[4] = r1[4]*data[i-1]*data[i-2]*data[i-1]
                print('--:',r1)
                s[0] = s[0] + r1[0]
                s[1] = s[1] + r1[1]
                s[2] = s[2] + r1[2]
                s[3] = s[3] + r1[3]
                s[4] = s[4] + r1[4] 
                r1 = [1,1,1,1,1]
            i = i +1 
        print(s)
        res[2] = s

        r1 = [1,1,1,1,1]
        s = [0,0,0,0,0]
        i = 0
        while i < len(data):
            if i>=2:
                r1[0] = r1[0]*data[i]*data[i-1]*data[i-2]
                r1[1] = r1[1]*data[i-1]*data[i-2]
                r1[2] = r1[2]*data[i-2]*data[i-1]*data[i-2]
                r1[3] = r1[3]*data[i-1]*data[i-1]*data[i-2]
                r1[4] = r1[4]*data[i-1]*data[i-2]*data[i-1]*data[i-2]
                print('--:',r1)
                s[0] = s[0] + r1[0]
                s[1] = s[1] + r1[1]
                s[2] = s[2] + r1[2]
                s[3] = s[3] + r1[3]
                s[4] = s[4] + r1[4] 
                r1 = [1,1,1,1,1]
            i = i +1 
        print(s)
        res[3] = s
        m = numpy.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        v= numpy.array([0,0,0,0])
        i = 0
        print(res)
        while i < len(res):
            j = 0
            while j < len(res[i]):
                if j == 0:
                    v[i] = res[i][j]
                else:
                    m[i][j-1] = res[i][j]
                j = j + 1
            i = i + 1
        print(v)
        print(m)
        print('-------')
        r = numpy.linalg.solve(m, v)
        print(r)

        print(6*r[0]+89*r[1]+96*r[2]+1416*r[3])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
