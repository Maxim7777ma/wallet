import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QMainWindow, QDesktopWidget, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QTimer

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Мое окно')

        screen = QDesktopWidget().screenGeometry()
        self.setGeometry(screen)  # Устанавливаем размеры окна как максимальное

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)  # Выравниваем содержимое по центру y

        # Создаем кнопку закрытия и располагаем в верхнем правом углу
        close_button = QPushButton(self)
        close_icon = QPixmap("pngwing 1.png")  
        close_button.setIcon(QIcon(close_icon))
        close_button.setIconSize(close_icon.size())
        close_button.setStyleSheet("background-color: transparent; border: none;")
        close_button.clicked.connect(self.close)

        # Добавляем компоновку кнопки закрытия в правый верхний угол
        close_layout = QHBoxLayout()
        close_layout.addStretch(1)
        close_layout.addWidget(close_button)

        layout.addLayout(close_layout)

        # Создаем вложенную компоновку для изображения
        image_layout = QVBoxLayout()
        image_layout.setAlignment(Qt.AlignCenter)

        spacer_top = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        image_layout.addItem(spacer_top)

        image_label = QLabel(self)
        pixmap = QPixmap("tether-usdt-logo 2.png")  
        image_label.setPixmap(pixmap)
        image_label.setAlignment(Qt.AlignCenter)
        image_layout.addWidget(image_label)

        layout.addLayout(image_layout)

        # Создаем вложенную компоновку для текста
        text_layout = QVBoxLayout()
        text_layout.setAlignment(Qt.AlignCenter)
        text_layout.setContentsMargins(0, 0, 0, 0)

        text_label_1 = QLabel('Tether USDT', self)
        text_label_1.setAlignment(Qt.AlignCenter)
        text_label_1.setStyleSheet("font-size: 30px; color: black;")
        text_layout.addWidget(text_label_1)

        text_label_2 = QLabel('0 USDT', self)
        text_label_2.setAlignment(Qt.AlignCenter)
        text_label_2.setStyleSheet("font-size: 30px; color: black;")
        text_layout.addWidget(text_label_2)

        text_label_3 = QLabel('0.00 USD', self)
        text_label_3.setAlignment(Qt.AlignCenter)
        text_label_3.setStyleSheet("font-size: 20px; color: gray;")
        text_layout.addWidget(text_label_3)

        layout.addLayout(text_layout)

        # Создаем компоновку для кнопок
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignCenter)
        button_layout.setContentsMargins(0, 0, 0, 300)

        
        # Создаем кнопоки
        button1 = QPushButton('Receive', self)
        button1.setStyleSheet("QPushButton { font-size: 30px; background-color: #3E3E3E; width: 200px; height: 57px; border-radius: 25px; }")
        button2 = QPushButton('Send', self)
        button2.setStyleSheet("QPushButton { font-size: 30px; background-color: #3E3E3E; width: 200px; height: 57px; border-radius: 25px; }")

        button_layout.addWidget(button1)
        button_layout.addSpacing(47)  # растояние между Receive и Send
        button_layout.addWidget(button2)

        layout.addLayout(button_layout)

        central_widget.setLayout(layout)

        # Настройка анимации для кнопок
        self.connect_animated_button(button1, "red")
        self.connect_animated_button(button2, "green")

    def animate_button(self, button, color):
        original_style = button.styleSheet()

        button.setStyleSheet(f"QPushButton {{ font-size: 30px; background-color: {color}; width: 200px; height: 57px; border-radius: 20px; }}")
        timer = QTimer(self)
        timer.setSingleShot(True)
        timer.timeout.connect(lambda: button.setStyleSheet(original_style))
        timer.start(200)
        if button.text() == 'Receive':
            print('Button "Receive" был нажат!')
        elif button.text() == 'Send':
            print('Button "Send" был нажат!')

    def connect_animated_button(self, button, color):
        button.clicked.connect(lambda: self.animate_button(button, color))

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.setStyleSheet("background-color: #D9D9E2;")
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
