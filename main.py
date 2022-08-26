import sys

from PySide2.QtWidgets import QApplication, QMainWindow

from ui.ui_main import Ui_MultiLangTestApp


class MultiLangTestApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MultiLangTestApp()
        self.ui.setupUi(self)
        self.ui.comboLanguage.currentIndexChanged.connect(lambda index: self._on_language_changed())

    def _on_language_changed(self):
        print(f"Language changed to {self.ui.comboLanguage.currentText()}")
        # TODO: Update ALL widget texts with the new language here.


if __name__ == '__main__':

    app = QApplication(sys.argv)

    mt_app = MultiLangTestApp()
    mt_app.show()
    sys.exit(app.exec_())
