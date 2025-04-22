import sys

from PyQt5.QtWebEngineWidgets import QWebEngineView

from PyQt5.QtWidgets import (QApplication, QMainWindow, QToolBar, QPushButton, 

                           QVBoxLayout, QWidget, QLabel, QTextEdit, QLineEdit,

                           QHBoxLayout, QTreeView, QFileSystemModel, QListView,

                           QSplitter, QStatusBar, QAction, QComboBox, QMessageBox,

                           QInputDialog, QFileDialog, QScrollArea, QProgressBar, QFrame,

                           QSizePolicy, QPushButton, QGridLayout)

from PyQt5.QtGui import (QIcon, QPixmap, QTextCursor, QColor, QFont, 

                       QTextCharFormat, QPainter, QPen, QImage, QPalette)

from PyQt5.QtCore import (Qt, QSize, QDir, QTimer, QPoint, QRect, 

                         QProcess, QProcessEnvironment, QEvent, QObject, QUrl)


class main(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.setFixedSize(400, 300)

        self.setStyleSheet("background-color: #121212;")

        

        # Logo

        self.logo = QLabel(self)

        self.logo.setAlignment(Qt.AlignCenter)

        

        # Create simple logo

        pixmap = QPixmap(200, 200)

        pixmap.fill(Qt.transparent)

        painter = QPainter(pixmap)

        painter.setPen(QPen(QColor(0, 150, 255), 4))

        painter.drawEllipse(10, 10, 180, 180)

        painter.setFont(QFont("Fixedsys Excelsior 3.01", 24))

        painter.setPen(QColor(255, 255, 255))

        painter.drawText(QRect(10, 10, 180, 180), Qt.AlignCenter, "Delix")

        painter.end()

        

        self.logo.setPixmap(pixmap)

        

        # Progress bar

        self.progress = QProgressBar(self)

        self.progress.setRange(0, 100)

        self.progress.setTextVisible(False)

        self.progress.setStyleSheet("""

            QProgressBar {

                border: 2px solid #333;

                border-radius: 5px;

                background-color: #222;

                height: 10px;

            }

            QProgressBar::chunk {

                background-color: #0a84ff;

                border-radius: 3px;

            }

        """)

        

        # Version

        self.version = QLabel("Delix OS v0.1", self)

        self.version.setAlignment(Qt.AlignCenter)

        self.version.setStyleSheet("color: #666; font-size: 12px; font-family: Fixedsys Excelsior 3.01;")

        

        # Layout

        layout = QVBoxLayout()

        layout.addWidget(self.logo)

        layout.addWidget(self.progress)

        layout.addWidget(self.version)

        layout.setAlignment(self.logo, Qt.AlignCenter)

        layout.setAlignment(self.progress, Qt.AlignCenter)

        layout.setAlignment(self.version, Qt.AlignCenter)

        layout.setContentsMargins(40, 40, 40, 40)

        layout.setSpacing(20)

        self.setLayout(layout)

        

        # Center on screen

        screen = QApplication.primaryScreen().geometry()

        self.move(screen.center() - self.rect().center())

        

        # Timer for loading simulation

        self.timer = QTimer(self)

        self.timer.timeout.connect(self.update_progress)

        self.progress_value = 0

        self.timer.start(30)

    

    def update_progress(self):

        self.progress_value += 1

        self.progress.setValue(self.progress_value)

        

        if self.progress_value >= 100:

            self.timer.stop()



if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    mainapp = main()
    mainapp.showFullScreen()

    sys.exit(app.exec_())