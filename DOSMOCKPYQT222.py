import sys

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QTextEdit,
    QMainWindow,
    QListWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLineEdit,
)

from PyQt6.QtWidgets import QToolBar, QLineEdit

from PyQt6.QtGui import QAction
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QColorDialog
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QLabel,
    QTextEdit,
    QMainWindow,
    QListWidget,
    QHBoxLayout,
    QVBoxLayout,
    QLineEdit,
    QSlider,
)
from PyQt6.QtWidgets import QTabWidget


class DOS(QMainWindow):

    def __init__(self):
        super().__init__()

        self.dark_mode = False

        self.setWindowTitle("DOS")
        self.setGeometry(100, 100, 1000, 600)

        # =====================
        # DESKTOP
        # =====================

        self.desktop = QWidget()
        self.desktop.setStyleSheet("background-color: #f47321;")

        self.setCentralWidget(self.desktop)
        
        # Notepad Icon

        self.notepad_icon = QPushButton("📝\nNotepad", self.desktop)

        self.notepad_icon.setGeometry(20, 20, 80, 80)

        self.notepad_icon.clicked.connect(self.open_app)

        # Files Icon

        self.files_icon = QPushButton("📁\nFiles", self.desktop)

        self.files_icon.setGeometry(20, 120, 80, 80)

        self.files_icon.clicked.connect(self.open_files)

        # Browser Icon

        self.browser_icon = QPushButton("🌐\nBrowser", self.desktop)

        self.browser_icon.setGeometry(20, 220, 80, 80)

        self.browser_icon.clicked.connect(self.open_browser)

        # Settings Icon

        self.settings_icon = QPushButton("⚙️\nSettings", self.desktop)

        self.settings_icon.setGeometry(20, 320, 80, 80)

        self.settings_icon.clicked.connect(self.open_settings)

        # Calculator Icon

        self.calc_icon = QPushButton("🧮\nCalculator", self.desktop)

        self.calc_icon.setGeometry(20, 420, 80, 80)

        # Music Icon

        self.music_icon = QPushButton("🎵\nMusic", self.desktop)

        self.music_icon.setGeometry(120, 20, 80, 80)

        icon_style = """
        QPushButton {
            background: transparent;
            border: none;
            color: white;
            font-size: 14px;
        }

        QPushButton:hover {
            background-color: #005030;
        }
        """

        for button in [
            self.notepad_icon,
            self.files_icon,
            self.browser_icon,
            self.settings_icon,
            self.calc_icon,
            self.music_icon,
        ]:
            button.setStyleSheet(icon_style)

        # =====================
        # TASKBAR
        # =====================

        self.taskbar = QWidget(self)

        self.taskbar.setGeometry(0, 560, 1000, 40)

        self.taskbar.setStyleSheet("background-color: #005030;")

        self.start_button = QPushButton("🔑 Start", self.taskbar)

        self.start_button.setGeometry(10, 5, 80, 30)

        self.start_button.setStyleSheet("""
            QPushButton {
                background-color: #005030;
                color: white;
            }

            QPushButton:hover {
                background-color: white;
                color: black;
            }
        """)

        self.clock_label = QLabel("🕒", self.taskbar)

        self.clock_label.setGeometry(950, 5, 30, 30)

        self.clock_label.setStyleSheet("color: white;")
        self.apply_light_theme()

    # =====================
    # NOTEPAD
    # =====================

    def open_app(self):

        window = QWidget()

        window.setWindowTitle("Notepad")

        window.resize(500, 350)

        label = QLabel("Notepad", window)

        label.move(20, 10)

        editor = QTextEdit(window)

        editor.setGeometry(20, 40, 450, 250)

        window.show()

        self.notepad_window = window

    # =====================
    # FILE EXPLORER
    # =====================

    def open_files(self):

        self.files_window = QWidget()

        self.files_window.setWindowTitle("Files")

        self.files_window.resize(900, 600)

        self.files_window.setStyleSheet("""
            QWidget {
                background-color: #242424;
                color: white;
            }

            QListWidget {
                background-color: #2e2e2e;
                border: 1px solid #444;
            }

            QLineEdit {
                background-color: #333333;
                border: 1px solid #555;
                padding: 5px;
                color: white;
            }
        """)

        main_layout = QVBoxLayout()

        # Address Bar

        address_bar = QLineEdit()

        address_bar.setText("/home/user")

        main_layout.addWidget(address_bar)

        content_layout = QHBoxLayout()

        # Sidebar

        sidebar = QListWidget()

        sidebar.addItem("🏠 Home")
        sidebar.addItem("📄 Documents")
        sidebar.addItem("⬇ Downloads")
        sidebar.addItem("🖼 Pictures")
        sidebar.addItem("🎵 Music")
        sidebar.addItem("🎥 Videos")
        sidebar.addItem("🗑 Trash")

        sidebar.setFixedWidth(180)

        # Main File Area

        file_list = QListWidget()

        file_list.addItem("📁 Projects")
        file_list.addItem("📁 Python")
        file_list.addItem("📁 Downloads")
        file_list.addItem("📁 Pictures")
        file_list.addItem("📁 Games")
        file_list.addItem("📄 notes.txt")
        file_list.addItem("📄 report.pdf")
        file_list.addItem("🐍 app.py")

        content_layout.addWidget(sidebar)

        content_layout.addWidget(file_list)

        main_layout.addLayout(content_layout)

        def open_item(item):

            text = item.text()

            if text.startswith("📁"):

                folder = text.replace("📁 ", "")

                address_bar.setText(address_bar.text() + "/" + folder)

                file_list.clear()

                file_list.addItem("📁 Subfolder")

                file_list.addItem("📄 readme.txt")

                file_list.addItem("🐍 main.py")

                file_list.addItem("📄 config.json")

        file_list.itemDoubleClicked.connect(open_item)

        self.files_window.setLayout(main_layout)

        self.files_window.show()

    # =====================
    # BROWSER
    # =====================

    def open_browser(self):

        self.browser_window = QMainWindow()
        self.browser_window.resize(1200, 800)
        self.browser_window.setWindowTitle("Browser")

        # Tabs
        self.tabs = QTabWidget()
        self.browser_window.setCentralWidget(self.tabs)

        # First tab
        browser = QWebEngineView()
        browser.setUrl(QUrl("https://www.google.com"))
        self.tabs.addTab(browser, "New Tab")

        # Toolbar
        toolbar = QToolBar()
        self.browser_window.addToolBar(toolbar)

        back_btn = QAction("←", self)
        back_btn.triggered.connect(browser.back)
        toolbar.addAction(back_btn)

        forward_btn = QAction("→", self)
        forward_btn.triggered.connect(browser.forward)
        toolbar.addAction(forward_btn)

        refresh_btn = QAction("⟳", self)
        refresh_btn.triggered.connect(browser.reload)
        toolbar.addAction(refresh_btn)

        home_btn = QAction("🏠", self)
        home_btn.triggered.connect(lambda: browser.setUrl(QUrl("https://www.google.com")))
        toolbar.addAction(home_btn)

        address_bar = QLineEdit()
        toolbar.addWidget(address_bar)

        status = QLabel("Ready")
        toolbar.addWidget(status)

        browser.loadStarted.connect(lambda: status.setText("Loading..."))
        browser.loadFinished.connect(lambda: status.setText("Done"))

        def navigate():
            url = address_bar.text()
            if not url.startswith(("http://", "https://")):url = "https://" + url 
            browser.setUrl(QUrl(url))

        address_bar.returnPressed.connect(navigate)
        browser.urlChanged.connect(lambda q: address_bar.setText(q.toString()))
        browser.titleChanged.connect(self.browser_window.setWindowTitle)

        self.browser_window.show()

    # =====================
    # SETTINGS
    # =====================

    def open_settings(self):

        self.settings_window = QWidget()

        self.settings_window.setWindowTitle("Settings")

        self.settings_window.resize(400, 300)

        layout = QVBoxLayout()

        title = QLabel("System Settings")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")

        layout.addWidget(title)
        theme_button = QPushButton("Toggle Dark / Light Mode")

        theme_button.clicked.connect(self.toggle_theme)

        layout.addWidget(theme_button)

        cycle_button = QPushButton("Change Taskbar Color")
        cycle_button.clicked.connect(self.change_taskbar_color)
        layout.addWidget(cycle_button)

        color_picker_button = QPushButton("Choose Taskbar Color")
        color_picker_button.clicked.connect(self.choose_taskbar_color)
        layout.addWidget(color_picker_button)

        size_label = QLabel("Desktop Icon Size")
        layout.addWidget(size_label)

        size_slider = QSlider(Qt.Orientation.Horizontal)

        size_slider.setMinimum(60)
        size_slider.setMaximum(140)
        size_slider.setValue(80)

        size_slider.valueChanged.connect(self.set_icon_size)

        layout.addWidget(size_slider)

        self.settings_window.setLayout(layout)

        self.settings_window.show()

    def apply_light_theme(self):

        self.setStyleSheet("""
        QMainWindow, QWidget {
            background-color: #f47321;
            color: white;
        }

        QPushButton {
            color: white;
        }
    """)

        self.desktop.setStyleSheet("background-color: #f47321;")

    def apply_dark_theme(self):

        self.setStyleSheet("""
            QMainWindow, QWidget {
            background-color: #1e1e1e;
            color: white;
        }

            QPushButton {
            color: white;
        }
    """)

        self.desktop.setStyleSheet("background-color: #1e1e1e;")

    def toggle_theme(self):

        self.dark_mode = not self.dark_mode

        if self.dark_mode:
            self.apply_dark_theme()

        else:
            self.apply_light_theme()

    def change_taskbar_color(self):

        colors = [
            "#005030",  # Green
            "#1e3a8a",  # Blue
            "#7c2d12",  # Brown
            "#4c1d95",  # Purple
            "#7f1d1d",  # Red
        ]

        current = self.taskbar.styleSheet()

        for i, color in enumerate(colors):

            if color in current:
                next_color = colors[(i + 1) % len(colors)]
                break
        else:
            next_color = colors[0]

        self.taskbar.setStyleSheet(f"background-color: {next_color};")

    def choose_taskbar_color(self):

        color = QColorDialog.getColor()

        if color.isValid():

            self.taskbar.setStyleSheet(f"background-color: {color.name()};")

    def set_icon_size(self, size):

        icons = [
            self.notepad_icon,
            self.files_icon,
            self.browser_icon,
            self.settings_icon,
            self.calc_icon,
            self.music_icon,
        ]

        for icon in icons:

            icon.setFixedSize(size, size)

            font_size = max(10, size // 6)

            icon.setStyleSheet(f"""
                QPushButton {{
                    background: transparent;
                    border: none;
                    color: white;
                    font-size: {font_size}px;
                }}

                QPushButton:hover {{
                    background-color: #005030;
                }}
            """)


# =====================
# MAIN
# =====================

app = QApplication(sys.argv)

window = DOS()
window.show()

sys.exit(app.exec())
