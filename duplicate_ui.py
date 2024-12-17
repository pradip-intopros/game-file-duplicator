import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                           QFileDialog, QMessageBox)
from PyQt5.QtGui import QIcon
from duplicate import copy_and_rename_prefabs

class DuplicateUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Game File Duplicator")
        self.setGeometry(100, 100, 600, 200)
        
        # Set window icon
        if getattr(sys, 'frozen', False):
            # Running in PyInstaller bundle
            icon_path = os.path.join(sys._MEIPASS, 'logo.PNG')
        else:
            # Running in development
            icon_path = os.path.join(os.path.dirname(__file__), 'logo.PNG')
        self.setWindowIcon(QIcon(icon_path))
        
        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Source folder selection
        src_layout = QHBoxLayout()
        self.src_input = QLineEdit()
        src_button = QPushButton("Browse")
        src_button.clicked.connect(lambda: self.browse_folder(self.src_input))
        src_layout.addWidget(QLabel("Source Folder:"))
        src_layout.addWidget(self.src_input)
        src_layout.addWidget(src_button)
        layout.addLayout(src_layout)
        
        # Destination folder selection
        dst_layout = QHBoxLayout()
        self.dst_input = QLineEdit()
        dst_button = QPushButton("Browse")
        dst_button.clicked.connect(lambda: self.browse_folder(self.dst_input))
        dst_layout.addWidget(QLabel("Destination Folder:"))
        dst_layout.addWidget(self.dst_input)
        dst_layout.addWidget(dst_button)
        layout.addLayout(dst_layout)
        
        # Prefix inputs
        prefix_layout = QHBoxLayout()
        self.old_prefix = QLineEdit()
        self.new_prefix = QLineEdit()
        prefix_layout.addWidget(QLabel("Old Prefix:"))
        prefix_layout.addWidget(self.old_prefix)
        prefix_layout.addWidget(QLabel("New Prefix:"))
        prefix_layout.addWidget(self.new_prefix)
        layout.addLayout(prefix_layout)
        
        # Process button
        process_button = QPushButton("Process Files")
        process_button.clicked.connect(self.process_files)
        layout.addWidget(process_button)
    
    def browse_folder(self, line_edit):
        folder = QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder:
            line_edit.setText(folder)
    
    def process_files(self):
        src_folder = self.src_input.text()
        dst_folder = self.dst_input.text()
        old_prefix = self.old_prefix.text()
        new_prefix = self.new_prefix.text()
        
        if not all([src_folder, dst_folder, old_prefix, new_prefix]):
            QMessageBox.warning(self, "Error", "All fields must be filled!")
            return
        
        try:
            copy_and_rename_prefabs(src_folder, dst_folder, old_prefix, new_prefix)
            QMessageBox.information(self, "Success", "Files processed successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

def main():
    app = QApplication(sys.argv)
    window = DuplicateUI()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
