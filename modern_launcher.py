import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, 
                             QPushButton, QLabel, QFrame, QHBoxLayout, QGridLayout,
                             QSizePolicy, QGraphicsDropShadowEffect)
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QRect
from PyQt5.QtGui import QFont, QColor, QPalette, QIcon, QLinearGradient, QBrush, QPainter

class ModernButton(QPushButton):
    def __init__(self, text, color, icon_text, parent=None):
        super().__init__(text, parent)
        self.color = color
        self.icon_text = icon_text
        self.setCursor(Qt.PointingHandCursor)
        self.setFixedSize(280, 180)
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                border-radius: 15px;
                font-size: 18px;
                font-weight: bold;
                padding: 20px;
            }}
            QPushButton:hover {{
                background-color: {self._darken_color(color, 20)};
                transform: translateY(-5px);
            }}
            QPushButton:pressed {{
                background-color: {self._darken_color(color, 30)};
            }}
        """)
    
    def _darken_color(self, color, percent):
        """Darken a hex color by a percentage"""
        color = color.lstrip('#')
        r, g, b = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        r = int(max(0, r * (1 - percent / 100)))
        g = int(max(0, g * (1 - percent / 100)))
        b = int(max(0, b * (1 - percent / 100)))
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Draw rounded rectangle with gradient
        gradient = QLinearGradient(0, 0, self.width(), self.height())
        gradient.setColorAt(0, QColor(self.color))
        gradient.setColorAt(1, QColor(self._darken_color(self.color, 15)))
        painter.setBrush(QBrush(gradient))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.rect(), 15, 15)
        
        # Draw icon/text
        painter.setPen(QColor(255, 255, 255))
        font = QFont("Segoe UI", 48)
        font.setBold(True)
        painter.setFont(font)
        painter.drawText(self.rect(), Qt.AlignCenter, self.icon_text)
        
        # Draw label
        font = QFont("Segoe UI", 14)
        font.setBold(True)
        painter.setFont(font)
        painter.drawText(QRect(0, 120, self.width(), 40), Qt.AlignCenter, self.text())

class ModernDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IPTV Player Dashboard")
        self.setFixedSize(900, 600)
        
        # Apply modern dark theme
        self.apply_modern_theme()
        
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(40, 40, 40, 40)
        main_layout.setSpacing(30)
        
        # Header
        header = self.create_header()
        main_layout.addWidget(header)
        
        # Player cards
        cards_layout = QHBoxLayout()
        cards_layout.setSpacing(30)
        
        # Stalker Player Card
        stalker_card = self.create_player_card(
            "Stalker IPTV Player",
            "#2196F3",
            "📺",
            "MAC Address Authentication"
        )
        cards_layout.addWidget(stalker_card)
        
        # Xtream Player Card
        xtream_card = self.create_player_card(
            "Xtream IPTV Player",
            "#4CAF50",
            "🎬",
            "XTREAM Codes Authentication"
        )
        cards_layout.addWidget(xtream_card)
        
        main_layout.addLayout(cards_layout)
        
        # Footer
        footer = self.create_footer()
        main_layout.addWidget(footer)
        
        # Center the window
        self.center_window()
    
    def apply_modern_theme(self):
        """Apply modern dark theme to the application"""
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(45, 45, 48))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(35, 35, 38))
        palette.setColor(QPalette.AlternateBase, QColor(45, 45, 48))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(45, 45, 48))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        QApplication.setPalette(palette)
    
    def create_header(self):
        """Create modern header"""
        header = QFrame()
        header.setStyleSheet("""
            QFrame {
                background-color: #2C2C2E;
                border-radius: 15px;
                padding: 20px;
            }
        """)
        header.setFixedHeight(100)
        
        layout = QVBoxLayout(header)
        layout.setContentsMargins(25, 15, 25, 15)
        
        # Title
        title = QLabel("IPTV Player Dashboard")
        title.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                font-size: 28px;
                font-weight: bold;
                font-family: 'Segoe UI', Arial;
            }
        """)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Subtitle
        subtitle = QLabel("Select your preferred IPTV player")
        subtitle.setStyleSheet("""
            QLabel {
                color: #AAAAAA;
                font-size: 14px;
                font-family: 'Segoe UI', Arial;
            }
        """)
        subtitle.setAlignment(Qt.AlignCenter)
        layout.addWidget(subtitle)
        
        return header
    
    def create_player_card(self, title, color, icon, description):
        """Create a modern player card"""
        card = QFrame()
        card.setStyleSheet(f"""
            QFrame {{
                background-color: #2C2C2E;
                border-radius: 20px;
                border: 2px solid {color};
            }}
            QFrame:hover {{
                border: 3px solid {color};
            }}
        """)
        card.setFixedSize(350, 250)
        
        layout = QVBoxLayout(card)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Icon
        icon_label = QLabel(icon)
        icon_label.setStyleSheet(f"""
            QLabel {{
                color: {color};
                font-size: 60px;
                background: transparent;
            }}
        """)
        icon_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(icon_label)
        
        # Title
        title_label = QLabel(title)
        title_label.setStyleSheet("""
            QLabel {
                color: #FFFFFF;
                font-size: 20px;
                font-weight: bold;
                font-family: 'Segoe UI', Arial;
                background: transparent;
            }
        """)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        # Description
        desc_label = QLabel(description)
        desc_label.setStyleSheet("""
            QLabel {
                color: #AAAAAA;
                font-size: 12px;
                font-family: 'Segoe UI', Arial;
                background: transparent;
            }
        """)
        desc_label.setAlignment(Qt.AlignCenter)
        desc_label.setWordWrap(True)
        layout.addWidget(desc_label)
        
        # Launch button
        launch_btn = QPushButton("Launch Player")
        launch_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                border-radius: 10px;
                padding: 12px;
                font-size: 14px;
                font-weight: bold;
                font-family: 'Segoe UI', Arial;
            }}
            QPushButton:hover {{
                background-color: {self._darken_color(color, 20)};
            }}
            QPushButton:pressed {{
                background-color: {self._darken_color(color, 30)};
            }}
        """)
        launch_btn.setCursor(Qt.PointingHandCursor)
        
        # Connect to appropriate launch function
        if "Stalker" in title:
            launch_btn.clicked.connect(self.launch_stalker)
        else:
            launch_btn.clicked.connect(self.launch_xtream)
        
        layout.addWidget(launch_btn)
        
        # Add shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 100))
        shadow.setOffset(0, 5)
        card.setGraphicsEffect(shadow)
        
        return card
    
    def _darken_color(self, color, percent):
        """Darken a hex color by a percentage"""
        color = color.lstrip('#')
        r, g, b = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
        r = int(max(0, r * (1 - percent / 100)))
        g = int(max(0, g * (1 - percent / 100)))
        b = int(max(0, b * (1 - percent / 100)))
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def create_footer(self):
        """Create modern footer"""
        footer = QFrame()
        footer.setStyleSheet("""
            QFrame {
                background-color: transparent;
                border: none;
            }
        """)
        footer.setFixedHeight(50)
        
        layout = QHBoxLayout(footer)
        layout.setContentsMargins(0, 0, 0, 0)
        
        version_label = QLabel("Version 1.0.0")
        version_label.setStyleSheet("""
            QLabel {
                color: #666666;
                font-size: 12px;
                font-family: 'Segoe UI', Arial;
            }
        """)
        layout.addWidget(version_label)
        
        layout.addStretch()
        
        copyright_label = QLabel("© 2024 IPTV Player Dashboard")
        copyright_label.setStyleSheet("""
            QLabel {
                color: #666666;
                font-size: 12px;
                font-family: 'Segoe UI', Arial;
            }
        """)
        layout.addWidget(copyright_label)
        
        return footer
    
    def center_window(self):
        """Center the window on screen"""
        screen = QApplication.desktop().screenGeometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)
    
    def launch_stalker(self):
        """Launch Stalker IPTV Player"""
        try:
            import subprocess
            stalker_path = os.path.join(os.path.dirname(__file__), 'dist', 'Stalker_IPTV_Player.exe')
            if os.path.exists(stalker_path):
                subprocess.Popen([stalker_path])
                self.close()
            else:
                # Fallback to Python script
                stalker_script = os.path.join(os.path.dirname(__file__), 'STALKER PLAYER.py')
                subprocess.Popen([sys.executable, stalker_script])
                self.close()
        except Exception as e:
            print(f"Error launching Stalker Player: {e}")
    
    def launch_xtream(self):
        """Launch Xtream IPTV Player"""
        try:
            import subprocess
            xtream_path = os.path.join(os.path.dirname(__file__), 'dist', 'Xtream_IPTV_Player.exe')
            if os.path.exists(xtream_path):
                subprocess.Popen([xtream_path])
                self.close()
            else:
                # Fallback to Python script
                xtream_script = os.path.join(os.path.dirname(__file__), 'XTREME-IPTV-PLAYER', 'XTREME IPTV PLAYER BY MY-1 v4.0.py')
                subprocess.Popen([sys.executable, xtream_script])
                self.close()
        except Exception as e:
            print(f"Error launching Xtream Player: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    dashboard = ModernDashboard()
    dashboard.show()
    
    sys.exit(app.exec_())
