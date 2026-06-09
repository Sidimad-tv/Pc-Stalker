import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QStyle
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class LauncherWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IPTV Player Launcher")
        self.setFixedSize(500, 300)
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Title
        title_label = QLabel("Select IPTV Player")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # Stalker Player Button
        stalker_btn = QPushButton("Stalker IPTV Player")
        stalker_btn.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                padding: 15px;
                background-color: #2196F3;
                color: white;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        stalker_btn.clicked.connect(self.launch_stalker)
        layout.addWidget(stalker_btn)
        
        # Xtream Player Button
        xtream_btn = QPushButton("Xtream IPTV Player")
        xtream_btn.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                padding: 15px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #388E3C;
            }
        """)
        xtream_btn.clicked.connect(self.launch_xtream)
        layout.addWidget(xtream_btn)
        
        layout.addStretch()
        
        # Center the window
        self.center_window()
    
    def center_window(self):
        screen = QApplication.desktop().screenGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)
    
    def launch_stalker(self):
        self.hide()
        try:
            # Launch Stalker Player as subprocess
            import subprocess
            stalker_path = os.path.join(os.path.dirname(__file__), 'STALKER PLAYER.py')
            subprocess.Popen([sys.executable, stalker_path])
            self.close()
        except Exception as e:
            print(f"Error launching Stalker Player: {e}")
            import traceback
            traceback.print_exc()
            self.show()
    
    def launch_xtream(self):
        self.hide()
        try:
            # Launch Xtream Player as subprocess
            import subprocess
            xtream_path = os.path.join(os.path.dirname(__file__), 'XTREME-IPTV-PLAYER', 'XTREME IPTV PLAYER BY MY-1 v4.0.py')
            subprocess.Popen([sys.executable, xtream_path])
            self.close()
        except Exception as e:
            print(f"Error launching Xtream Player: {e}")
            import traceback
            traceback.print_exc()
            self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    launcher = LauncherWindow()
    launcher.show()
    
    sys.exit(app.exec_())
