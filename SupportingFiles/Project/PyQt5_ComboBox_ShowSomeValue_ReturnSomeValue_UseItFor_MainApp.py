from PyQt5 import QtWidgets, QtCore
import pandas as pd


class Widget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)

        self.combo = QtWidgets.QComboBox(self)

        # some data
        self.df = pd.DataFrame({'TERM': ['apple', 'banana', 'cherry', 'date', 'grape'],
                                'UID': [1, 2, 3, 4, 5]})

        print(self.df)
        # for each row in dataframe, add item with value in 'TERM' column as text and value in 'UID' column as data
        for row in self.df.itertuples():
            self.combo.addItem(row.TERM, row.UID)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.combo)

        self.combo.currentIndexChanged.connect(self.combo_index_changed)

    def combo_index_changed(self, index):
        # retrieve user data of an item in combo box via QComboBox.itemData()
        print(f'index {index}, text {self.combo.itemText(index)}, uid {self.combo.itemData(index)}')


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = Widget()
    w.show()
    app.exec()