import glob
import ntpath
import os
import platform


_cur_dir = os.path.dirname(os.path.realpath(__file__))

ui_folders = [
    _cur_dir
]


def compile_ui():

    for ui_folder in ui_folders:
        for ui_file in glob.glob(os.path.join(ui_folder, '*.ui')):
            name = ntpath.basename(ui_file).split('.')[0]
            py_file = os.path.join(ui_folder, f'ui_{name}.py')
            os.system(f"pyside2-uic {ui_file} > {py_file}")
            # A bug in PySide2?
            if platform.system() == 'Linux':
                os.system(f"sed -i -- \"s/QString()/''/g\" {py_file}")


if __name__ == '__main__':

    compile_ui()
