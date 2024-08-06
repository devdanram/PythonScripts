import sys
from PySide2 import QtCore, QtGui, QtWidgets
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui
import maya.cmds as cmds

def maya_main_window():
    """
    Return the Maya main window widget as a Python object
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)

class OpenImportDialog(QtWidgets.QDialog):

    def __init__(self, parent=maya_main_window()):
        super(OpenImportDialog, self).__init__(parent)

        self.setWindowTitle("Save Data")
        self.setMinimumSize(250, 80)
        self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowContextHelpButtonHint)

        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self):
        self.save_btn = QtWidgets.QPushButton("SAVE")
        self.load_btn = QtWidgets.QPushButton("LOAD")
        self.both_rb = QtWidgets.QRadioButton("BOTH")
        self.both_rb.setChecked(True)
        self.translate_rb = QtWidgets.QRadioButton("TRANSLATE")
        self.rotate_rb = QtWidgets.QRadioButton("ROTATE")
        self.close_btn = QtWidgets.QPushButton("Close")

    def create_layout(self):
        saveload_layout = QtWidgets.QHBoxLayout()
        saveload_layout.addStretch()
        saveload_layout.addWidget(self.save_btn)
        saveload_layout.addWidget(self.load_btn)

        radio_btn_layout = QtWidgets.QHBoxLayout()
        radio_btn_layout.addWidget(self.both_rb)
        radio_btn_layout.addWidget(self.translate_rb)
        radio_btn_layout.addWidget(self.rotate_rb)

        form_layout = QtWidgets.QFormLayout()
        form_layout.addRow("", radio_btn_layout)
        form_layout.addRow(saveload_layout)
        
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.close_btn)

        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

    def create_connections(self):
        self.save_btn.clicked.connect(self.save_Data)
        self.load_btn.clicked.connect(self.load_file)
        self.close_btn.clicked.connect(self.close)

    def get_path(self):
        return r"C:\Users\moebi\Desktop\transform_data.txt"

    def load_file(self):
        selected_objects = cmds.ls(selection=True)

        if not selected_objects:
            cmds.error("No object selected.")
            return
        
        obj = selected_objects[0]
        file_path = self.get_path()

        try:
            with open(file_path, "r") as file:
                lines = file.readlines()

            if self.translate_rb.isChecked():
                translation_line = lines[1].strip()
                translation_values = translation_line.split(':')[1].split(',')
                translation = [float(val.split('=')[1]) for val in translation_values]
                cmds.setAttr(f"{obj}.translate", translation[0], translation[1], translation[2])
                cmds.confirmDialog(title='Success', message='Translation values applied successfully.', button=['OK'])

            elif self.rotate_rb.isChecked():
                rotation_line = lines[2].strip()
                rotation_values = rotation_line.split(':')[1].split(',')
                rotation = [float(val.split('=')[1]) for val in rotation_values]
                cmds.setAttr(f"{obj}.rotate", rotation[0], rotation[1], rotation[2])
                cmds.confirmDialog(title='Success', message='Rotation values applied successfully.', button=['OK'])

            else:
                translation_line = lines[1].strip()
                translation_values = translation_line.split(':')[1].split(',')
                translation = [float(val.split('=')[1]) for val in translation_values]
                cmds.setAttr(f"{obj}.translate", translation[0], translation[1], translation[2])

                rotation_line = lines[2].strip()
                rotation_values = rotation_line.split(':')[1].split(',')
                rotation = [float(val.split('=')[1]) for val in rotation_values]
                cmds.setAttr(f"{obj}.rotate", rotation[0], rotation[1], rotation[2])
                cmds.confirmDialog(title='Success', message='Translation and rotation values applied successfully.', button=['OK'])

        except Exception as e:
            cmds.error(f"An error occurred: {e}")

    def save_Data(self):
        selected_objects = cmds.ls(selection=True)
        
        if not selected_objects:
            cmds.error("No object selected.")
            return
        
        obj = selected_objects[0]
        translation = cmds.getAttr(f"{obj}.translate")[0]
        rotation = cmds.getAttr(f"{obj}.rotate")[0]

        data = f"Object: {obj}\n"
        data += f"Translation: X={translation[0]}, Y={translation[1]}, Z={translation[2]}\n"
        data += f"Rotation: X={rotation[0]}, Y={rotation[1]}, Z={rotation[2]}\n"

        file_path = self.get_path()

        try:
            with open(file_path, "w") as file:
                file.write(data)
            cmds.confirmDialog(title='Success', message=f'Translation and rotation values saved to {file_path}', button=['OK'])
        except Exception as e:
            cmds.error(f"An error occurred: {e}")

if __name__ == "__main__":

    try:
        open_import_dialog.close()
        open_import_dialog.deleteLater()
    except:
        pass

    open_import_dialog = OpenImportDialog()
    open_import_dialog.show()
