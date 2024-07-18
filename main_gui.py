import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QToolBar, QAction, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dark Themed GUI")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #2e2e2e;")

        # Create a toolbar
        toolbar = QToolBar()
        toolbar.setStyleSheet("background-color: #3e3e3e; border: none;")
        self.addToolBar(Qt.TopToolBarArea, toolbar)
        self.addToolBarBreak(Qt.TopToolBarArea)

        # Add actions to the toolbar
        action1 = QAction(QIcon(), "Action 1", self)
        action2 = QAction(QIcon(), "Action 2", self)
        toolbar.addAction(action1)
        toolbar.addAction(action2)

        # Create tabs
        tabs = QTabWidget()
        tabs.setStyleSheet("""
            QTabWidget::pane { border: 0; }
            QTabBar::tab { background: #3e3e3e; color: white; padding: 10px; border-radius: 10px 10px 0 0; min-width: 100px; margin-top: 5px; }
            QTabBar::tab:selected { background: #5e5e5e; }
            QTabBar { background: #252525; qproperty-drawBase: 0; border-radius: 15px; margin: 5px; padding: 5px; }
            QTabWidget>QWidget>QWidget { background: #2e2e2e; }
        """)

        # Create tab content
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        tab4 = QWidget()
        tab5 = QWidget()
        tabs.addTab(tab1, "Tab 1")
        tabs.addTab(tab2, "Tab 2")
        tabs.addTab(tab3, "Tab 3")
        tabs.addTab(tab4, "Tab 4")
        tabs.addTab(tab5, "Tab 5")

        # Layout for tab1
        layout1 = QVBoxLayout()
        tab1.setLayout(layout1)

        # Layout for tab2
        layout2 = QVBoxLayout()
        tab2.setLayout(layout2)

        # Layout for tab3
        layout3 = QVBoxLayout()
        tab3.setLayout(layout3)

        # Layout for tab4
        layout4 = QVBoxLayout()
        tab4.setLayout(layout4)

        # Layout for tab5
        layout5 = QVBoxLayout()
        tab5.setLayout(layout5)

        # Set central widget
        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_layout.addWidget(toolbar)
        central_layout.addWidget(tabs)
        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
