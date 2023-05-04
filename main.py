import random
import tkinter as tk
from GameRules import GameRules
from Game import Game


class Board:
    # Размер доски
    size = 5

    # Метод для создания доски
    @staticmethod
    def create_board(size):
        return [[random.choice([True, False]) for i in range(size)] for j in range(size)]

    # Метод для изменения состояния клетки и всех соседних клеток

    def __init__(self, window_size, cell_color, bg_color):
        # Определение размеров окна
        self.window_size = window_size

        # Создание доски
        self.board = Board.create_board(Board.size)

        # Определение цветов клеток и фона
        self.cell_color = cell_color
        self.bg_color = bg_color

    @staticmethod
    def toggle_cell(board, i, j):
        Game.toggle(board, i, j)
    # Метод для отрисовки доски на экране
    def draw_board(self, canvas):
        for i in range(Board.size):
            for j in range(Board.size):
                x = j * self.cell_size
                y = i * self.cell_size
                color = self.cell_color if self.board[i][j] else self.bg_color
                canvas.create_rectangle(x, y, x + self.cell_size, y + self.cell_size, fill=color, outline="black")

    # Метод для проверки победы
    def check_win(self):
        for i in range(Board.size):
            for j in range(Board.size):
                if not self.board[i][j]:
                    return False
        return True

    # Метод для обработки нажатия на клетку
    def handle_click(self, event, canvas):
        x, y = event.x, event.y
        i = y // self.cell_size
        j = x // self.cell_size
        Board.toggle_cell(self.board, i, j)
        self.draw_board(canvas)
        if self.check_win():
            # Поздравление с победой
            canvas.create_rectangle(0,0,self.window_size[0],self.window_size[1],fill=self.bg_color)
            canvas.create_text(self.window_size[0]/2, self.window_size[1]/2, text="Вы выиграли!", font=("Arial", 36))

    # Метод для запуска игры
    def run(self):
        # Создание окна
        root = tk.Tk()
        root.title("Выключи свет")
        root.geometry(f"{self.window_size[0]}x{self.window_size[1]}")

        # Создание меню
        menu = tk.Menu(root)
        root.config(menu=menu)

        # Создание окна настроек
        def open_settings():
            settings_window = tk.Toplevel(root)
            settings_window.title("Настройки")
            settings_window.geometry("300x200")

            # Создание ползунков для настройки размера поля
            size_label = tk.Label(settings_window, text="Размер поля:")
            size_label.pack()

            size_slider = tk.Scale(settings_window, from_=3, to=10, orient=tk.HORIZONTAL, length=200, tickinterval=1)
            size_slider.set(Board.size)
            size_slider.pack()

            # Создание полей для настройки цвета
            cell_color_label = tk.Label(settings_window, text="Цвет клеток:")
            cell_color_label.pack()

            cell_color_entry = tk.Entry(settings_window, width=7)
            cell_color_entry.insert(0, self.cell_color)
            cell_color_entry.pack()

            bg_color_label = tk.Label(settings_window, text="Цвет фона:")
            bg_color_label.pack()

            bg_color_entry = tk.Entry(settings_window, width=7)
            bg_color_entry.insert(0, self.bg_color)
            bg_color_entry.pack()

            # Обработка изменений настроек и закрытие окна
            def save_settings():
                Board.size = size_slider.get()
                self.cell_color = cell_color_entry.get()
                self.bg_color = bg_color_entry.get()
                self.board = Board.create_board(Board.size)
                self.window_size = (self.cell_size * Board.size, self.cell_size * Board.size)
                root.geometry(f"{self.window_size[0]}x{self.window_size[1]}")
                self.draw_board(canvas)
                settings_window.destroy()

            save_button = tk.Button(settings_window, text="Сохранить", command=save_settings)
            save_button.pack()

        settings_menu = tk.Menu(menu)
        menu.add_cascade(label="Настройки", menu=settings_menu)
        settings_menu.add_command(label="Открыть настройки", command=open_settings)

        # Создание игровой доски
        canvas = tk.Canvas(root, width=self.window_size[0], height=self.window_size[1])
        canvas.pack(fill=tk.BOTH, expand=True)

        def open_rules():
            rules_window = tk.Toplevel(root)
            rules_window.title("Правила игры")
            rules_window.geometry("400x300")

            # Получение текста правил игры
            rules_text = GameRules.get_rules()

            # Отображение текста на экране
            rules_label = tk.Label(rules_window, text=rules_text, font=("Arial", 12))
            rules_label.pack()

        menu.add_command(label="Правила игры", command=open_rules)
        # Определение размера клетки
        self.cell_size = self.window_size[0] // Board.size

        # Отрисовка начального состояния доски
        self.draw_board(canvas)

        # Обработка нажатий на клавиши
        canvas.bind("<Button-1>", lambda event: self.handle_click(event, canvas))

        # Запуск игры
        root.mainloop()



# Создание доски и запуск игры
board = Board((400, 400), "#ffff99", "#ffffff")
board.run()