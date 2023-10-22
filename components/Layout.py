from PySide6.QtWidgets import QGridLayout, QVBoxLayout, QLayout, QHBoxLayout, QFormLayout, QBoxLayout


class Grid(QGridLayout):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ["%", "+", "-", "*"],
            ["7", "8", "9", "**"],
            ["4", "5", "6", "/"],
            ["1", "2", "3", "//"],
            ["x", "0", ",", "="]
        ]
        self._make_grid()

    def _make_grid(self):
        for row_number, row_data in enumerate(self._grid_mask):
            for column_number, column_data in enumerate(self._grid_mask[row_number]):
                self.addWidget(button, row_number, column_number)

