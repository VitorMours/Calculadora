import sys
import typing
import PySide6
from typing import Any, TypeVar, Optional
from PySide6.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QMainWindow, QApplication, QLayout


class MainWindow(QMainWindow):
    def __init__(self, parent: None | QWidget = None, title: str = "Application Main Window", *args: object, **kwargs: object) -> None:
        """
        MainWindow class constructor, need to specify some arguments that are used to build the Main window.

        Parameters
        ----------
        parent: QWidget | None
            Widget that's going to be used as the base of the main window of the application
        title: str
            The title of the main window applcation
        args:
            Any additional arguments
        kwargs:
            Any additional keyword arguments

        Returns
        -------
            None
        """

        # Setting the window standard configurations
        super().__init__(parent, *args, **kwargs)
        self.setWindowTitle(title)
        self.layout_list = []

    def add_layout(self, new_layout: QLayout):
        """
        Function designed to add a layout to the class layout's list, so we can have all the application layouts present
        in our list, facilitating to modify and make a reference to them.

        Parameters
        ----------
         new_layout: QLayout
            The new layout we're going to add to our list

        Returns
        -------
            None
        """
        self.layout_list.append(new_layout)

    def remove_layout(self, specific_layout: QLayout):
        """
        Function designed to remove a specific layout that exist in the layout list of the application, so is also going
        to be removed all the widgets from that specific layout.

        Parameters
        ----------
        specific_layout: QLayout
            The layout we want to remove from the application, and consequently, his layout list

        Returns
        -------
        None
        """
        self.layout_list.remove(specific_layout)

    def add_to_layout(self, layout: QLayout, widget: QWidget) -> None:
        """
        Function dedicated to add widget to a specific layout present inside the main window application

        Parameters
        ----------
        layout: QLayout
            The specific layout we want to add the widget too.
        widget: QWidget
            The specific Widget we want to add in the layout.

        Returns
        -------
            None
        """


if __name__ == "__main__":
    # Executando testes para verificar integridade dos elementos
    app = QApplication(sys.argv)

    window = MainWindow()

    window.show()
    app.exec()
