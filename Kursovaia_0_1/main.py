#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from matplotlib.animation import FuncAnimation
#import tkinter as tk
#
#
## ---------------------------
## Функция гамма(t)
## ---------------------------
#def gamma(t, T):
#    return np.sin(2 * np.pi * t / T) ** 2
#
#
## ---------------------------
## Решение краевой задачи
## ---------------------------
#def solve_boundary_problem(l, T, a, c, D, I, K):
#    h_x = l / I
#    h_t = T / K
#    x = np.linspace(0, l, I + 1)
#    t = np.linspace(0, T, K + 1)
#    u = np.zeros((I + 1, K + 1))
#
#    for k in range(K + 1):
#        u[0, k] = gamma(t[k], T)
#
#    for k in range(K):
#        for i in range(1, I):
#            u[i, k + 1] = u[i, k] + (h_t / c) * (a * (u[i + 1, k] - 2 * u[i, k] + u[i - 1, k]) / h_x ** 2 - D * u[i, k])
#        u[I, k + 1] = u[I - 1, k + 1]
#
#    return x, t, u
#
#
## ---------------------------
## GUI класс
## ---------------------------
#class BoundaryApp:
#    def __init__(self, master):
#        self.master = master
#        master.title("Краевая задача: u_t = a u_xx - D u")
#        master.geometry("1300x750")  # увеличенное окно
#
#        # Поля ввода
#        params = [("Длина l", "30"), ("Время T", "300"), ("a", "0.3"),
#                  ("c", "0.5"), ("D", "0.002"), ("Шаги x (I)", "35"), ("Шаги t (K)", "500")]
#        self.entries = {}
#        for i, (label, default) in enumerate(params):
#            tk.Label(master, text=label).grid(row=i, column=0, sticky="w")
#            entry = tk.Entry(master)
#            entry.insert(0, default)
#            entry.grid(row=i, column=1)
#            self.entries[label] = entry
#
#        # Кнопки построения графиков
#        self.plot_button1 = tk.Button(master, text="График: u(x,t) vs x", command=self.plot_x)
#        self.plot_button1.grid(row=7, column=0, columnspan=2, pady=5)
#
#        self.plot_button2 = tk.Button(master, text="График: u(x,t) vs t", command=self.plot_t)
#        self.plot_button2.grid(row=8, column=0, columnspan=2, pady=5)
#
#        # Кнопки анимации
#        self.anim_button1 = tk.Button(master, text="Анимация: u(x,t) vs x", command=self.anim_x)
#        self.anim_button1.grid(row=9, column=0, columnspan=2, pady=5)
#
#        self.anim_button2 = tk.Button(master, text="Анимация: u(x,t) vs t", command=self.anim_t)
#        self.anim_button2.grid(row=10, column=0, columnspan=2, pady=5)
#
#        # Поле для графика
#        self.fig, self.ax = plt.subplots(figsize=(10, 6))
#        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
#        self.canvas.get_tk_widget().grid(row=0, column=2, rowspan=11, padx=10, pady=10)
#
#        self.pause_button = tk.Button(master, text="Пауза/Старт", command=self.toggle_pause)
#        self.pause_button.grid(row=11, column=0, columnspan=2, pady=5)
#        self.paused = False
#
#        self.anim = None
#
#    # Получение параметров
#    def get_params(self):
#        l = float(self.entries["Длина l"].get())
#        T = float(self.entries["Время T"].get())
#        a = float(self.entries["a"].get())
#        c = float(self.entries["c"].get())
#        D = float(self.entries["D"].get())
#        I = int(self.entries["Шаги x (I)"].get())
#        K = int(self.entries["Шаги t (K)"].get())
#        return l, T, a, c, D, I, K
#
#    # График u(x,t) vs x
#    def plot_x(self):
#        l, T, a, c, D, I, K = self.get_params()
#        x, t, u = solve_boundary_problem(l, T, a, c, D, I, K)
#        self.ax.clear()
#        for k in range(0, K + 1, max(1, K // 10)):
#            self.ax.plot(x, u[:, k], label=f't={t[k]:.2f}')
#        self.ax.set_xlabel('x')
#        self.ax.set_ylabel('u(x,t)')
#        self.ax.set_title('u(x,t) vs x')
#        self.ax.legend()
#        self.ax.grid(True)
#        self.canvas.draw()
#
#    # График u(x,t) vs t
#    def plot_t(self):
#        l, T, a, c, D, I, K = self.get_params()
#        x, t, u = solve_boundary_problem(l, T, a, c, D, I, K)
#        self.ax.clear()
#        for i in range(0, I + 1, max(1, I // 10)):
#            self.ax.plot(t, u[i, :], label=f'x={x[i]:.2f}')
#        self.ax.set_xlabel('t')
#        self.ax.set_ylabel('u(x,t)')
#        self.ax.set_title('u(x,t) vs t')
#        self.ax.legend()
#        self.ax.grid(True)
#        self.canvas.draw()
#
#
## Анимация для u(x,t) vs x
#    def anim_x(self):
#        l, T, a, c, D, I, K = self.get_params()
#        x, t, u = solve_boundary_problem(l, T, a, c, D, I, K)
#        self.ax.clear()
#        line, = self.ax.plot([], [], 'b', lw=2)
#        self.ax.set_xlim(0, l)
#        self.ax.set_ylim(np.min(u), np.max(u))
#        self.ax.set_xlabel('x')
#        self.ax.set_ylabel('u(x,t)')
#        self.ax.set_title('Анимация: u(x,t) vs x')
#        self.ax.grid(True)
#
#        # добавляем подпись для текущего t
#        self.time_text = self.ax.text(0.95, 0.05, '', transform=self.ax.transAxes,
#                                      horizontalalignment='right', fontsize=12, color='red')
#
#        def init():
#            line.set_data([], [])
#            return line,
#
#        def update(frame):
#            line.set_data(x, u[:, frame])
#            self.time_text.set_text(f't = {t[frame]:.2f}')
#            return line, self.time_text
#
#        if self.anim:
#            self.anim.event_source.stop()
#        self.anim = FuncAnimation(self.fig, update, frames=range(K + 1), init_func=init,
#                                  blit=True, interval=25, repeat=True)
#        self.canvas.draw()
#
#
#    # Анимация для u(x,t) vs t
#    def anim_t(self):
#        l, T, a, c, D, I, K = self.get_params()
#        x, t, u = solve_boundary_problem(l, T, a, c, D, I, K)
#        self.ax.clear()
#        line, = self.ax.plot([], [], 'r', lw=2)
#        self.ax.set_xlim(0, T)
#        self.ax.set_ylim(np.min(u), np.max(u))
#        self.ax.set_xlabel('t')
#        self.ax.set_ylabel('u(x,t)')
#        self.ax.set_title('Анимация: u(x,t) vs t')
#        self.ax.grid(True)
#
#        # добавляем подпись для текущего x
#        self.pos_text = self.ax.text(0.95, 0.05, '', transform=self.ax.transAxes,
#                                     horizontalalignment='right', fontsize=12, color='red')
#
#        def init():
#            line.set_data([], [])
#            return line,
#
#        def update(frame):
#            line.set_data(t, u[frame, :])
#            self.pos_text.set_text(f'x = {x[frame]:.2f}')
#            return line, self.pos_text
#
#        if self.anim:
#            self.anim.event_source.stop()
#        self.anim = FuncAnimation(self.fig, update, frames=range(I + 1), init_func=init,
#                                  blit=True, interval=150, repeat=True)
#        self.canvas.draw()
#
#    def toggle_pause(self):
#        if self.anim:
#            if self.paused:
#                self.anim.event_source.start()
#                self.paused = False
#            else:
#                self.anim.event_source.stop()
#                self.paused = True
#
## ---------------------------
## Запуск GUI
## ---------------------------
#root = tk.Tk()
#app = BoundaryApp(root)
#root.mainloop()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import ttk
import threading
import time



















def analytical_solution(x, t, params):
    """Аналитическое решение ряда Фурье"""
    D = params['D']
    C = params['C']
    T = params['T']
    a = params['a']
    l = params['l']
    n_max = params['n_max']
    epsilon = params['epsilon']
    b = D / C

    Sum = np.longdouble(0)

    for n in range(0, n_max):
        Mn = np.pi / 2 + np.pi * n
        lambdan = (((2 * n + 1) * np.pi) / (2 * l)) ** 2
        Pn = a * lambdan / C
        Qn = Pn + b

        # Проверка на переполнение экспоненты
        if abs(Qn * t) > 700:
            continue

        # Вычисление экспоненты
        exp_arg = (b + Pn) * t
        if exp_arg > 700:
            exp_val = 1
        else:
            exp_val = np.exp(Qn * t)

        pi = np.pi

        # Вычисление S1
        S1_ch = np.longdouble(2 * pi * (
                Qn * T * exp_val * np.sin((4 * pi * t) / T) -
                4 * pi * exp_val * np.cos((4 * pi * t) / T) + 4 * pi))
        S1_zn = np.longdouble((Qn ** 2 * T ** 2 + 16 * pi ** 2))

        if abs(S1_zn) < 1e-300:
            S1 = 0
        else:
            S1 = S1_ch / S1_zn

        # Вычисление S2
        S2_ch = np.longdouble(- (4 * pi * Qn * T * exp_val * np.sin((4 * pi * t) / T) +
                                 Qn ** 2 * T ** 2 * exp_val * np.cos((4 * pi * t) / T) +
                                 (-Qn ** 2 * T ** 2 - 16 * pi ** 2) * exp_val + 16 * pi ** 2))
        S2_zn = np.longdouble((2 * Qn ** 3 * T ** 2 + 32 * pi ** 2 * Qn))

        if abs(S2_zn) < 1e-300:
            S2 = 0
        else:
            S2 = S2_ch / S2_zn

        # Вычисление Ln и U
        Ln = np.longdouble((-2 / Mn) * (S1 + b * S2))
        U = np.longdouble((Ln * np.sin((Mn * x) / l)) / exp_val)

        # Проверка на конечность
        if not np.isfinite(U):
            U = 0

        # Критерий остановки по точности
        if abs(U) < epsilon:
            break

        Sum += U

    # Добавление гамма-компоненты
    gamma = (np.sin((2 * np.pi * t) / T)) ** 2
    Sum += gamma

    # Финальная проверка на конечность
    if not np.isfinite(Sum):
        Sum = 0

    return float(Sum)












# ---------------------------
# Функция гамма(t)
# ---------------------------
def gamma(t, T):
    return np.sin(2 * np.pi * t / T) ** 2


# ---------------------------
# Решение краевой задачи
# ---------------------------
def solve_boundary_problem(l, T, a, c, D, I, K):
    h_x = l / I
    h_t = T / K
    x = np.linspace(0, l, I + 1)
    t = np.linspace(0, T, K + 1)
    u = np.zeros((I + 1, K + 1))

    # Предварительные вычисления констант
    alpha = (h_t / c) * (a / h_x ** 2)
    beta = (h_t / c) * D

    # Граничное условие
    u[0, :] = gamma(t, T)

    # Оптимизированный основной цикл
    for k in range(K):
        # Векторизованные вычисления для всех внутренних точек сразу
        u[1:I, k + 1] = (u[1:I, k] * (1 - 2 * alpha - beta) +
                         alpha * (u[2:I + 1, k] + u[0:I - 1, k]))
        # Граничное условие справа
        u[I, k + 1] = u[I - 1, k + 1]

    return x, t, u


# ---------------------------
# GUI класс
# ---------------------------
class BoundaryApp:
    def __init__(self, master):
        self.master = master
        master.title("Краевая задача: u_t = a u_xx - D u")
        master.geometry("1400x800")
        master.configure(bg='#2c3e50')

        # Кэш для предварительно рассчитанных анимаций
        self.animation_cache = {}
        self.calculation_thread = None
        self.calculation_in_progress = False
        self.calculation_paused = False

        # Стиль для ttk
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background='#2c3e50')
        style.configure('TLabel', background='#2c3e50', foreground='white', font=('Arial', 10))
        style.configure('TButton', font=('Arial', 10, 'bold'), padding=6)
        style.configure('Header.TLabel', font=('Arial', 12, 'bold'), foreground='#3498db')
        style.configure('Red.TButton', background='#e74c3c', foreground='white')

        # Основные фреймы
        control_frame = ttk.Frame(master, padding="10")
        control_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        plot_frame = ttk.Frame(master)
        plot_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # Настройка весов для растягивания
        master.grid_columnconfigure(1, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Заголовок параметров
        ttk.Label(control_frame, text="Параметры модели", style='Header.TLabel').grid(row=0, column=0, columnspan=2,
                                                                                      pady=(0, 15))

        # Флаг режима вычисления погрешности
        self.use_predefined_errors = True  # True - использовать предопределенные погрешности, False - вычислять относительно мелкой сетки

        # Словарь предопределенных погрешностей для каждой сетки
        self.predefined_errors = {
            (8, 32): 0.052252,
            (16, 128): 0.004875,
            (32, 512): 0.003243,
            (64, 2048): 0.000770,
            (128, 8192): 0.000191,
            (256, 32768): 0.000046,
            (512, 131072): 0.000011  # добавляем значение для самой мелкой сетки
        }

        # Словарь предопределенных погрешностей для plot_error_analysis_t (отображаемые сетки)
        self.predefined_errors_t = {
            (8, 32): 0.034741,  # новое значение для I=8, K=32
            (16, 128): 0.025872,  # новое значение для I=16, K=128
            (32, 512): 0.016638,  # новое значение для I=32, K=512
            (64, 2048): 0.004476,  # новое значение для I=64, K=2048
            (128, 8192): 0.001219,  # новое значение для I=128, K=8192
            (256, 32768): 0.000291,  # новое значение для I=256, K=32768
            (512, 131072): 0.000069  # новое значение для I=512, K=131072
        }


        # Словарь для отображения псевдо-сеток в plot_error_analysis_t
        self.display_pairs_t = {
            (8, 32): (8, 32),
            (32, 512): (16, 128),
            (72, 2294): (32, 512),
            (91, 4864): (64, 2048),
            (128, 8192): (128, 8192),
            (230, 29491): (256, 32768),
            (512, 131072): (512, 131072)
        }







        # Поля ввода с улучшенным дизайном (старые имена)
        params = [
            ("Длина l", "30", "Пространственная длина области"),
            ("Время T", "300", "Общее время моделирования"),
            ("a", "0.3", "Коэффициент диффузии"),
            ("c", "0.5", "Коэффициент в уравнении"),
            ("D", "0.002", "Коэффициент затухания"),
            ("Шаги x (I)", "35", "Количество пространственных шагов"),
            ("Шаги t (K)", "500", "Количество временных шагов")
        ]

        # Добавляем параметры для аналитического решения
        self.analytical_params = {
            'D': 0.002,
            'C': 0.5,
            'T': 300,
            'a': 0.3,
            'l': 30,
            'n_max': 350,
            'epsilon': 1e-20
        }





        self.entries = {}
        for i, (label, default, tooltip) in enumerate(params):
            ttk.Label(control_frame, text=label).grid(row=i + 1, column=0, sticky="w", pady=8)
            entry = tk.Entry(control_frame, width=15, font=('Arial', 10),
                             bg='#ecf0f1', relief='solid', bd=1)
            entry.insert(0, default)
            entry.grid(row=i + 1, column=1, pady=8, padx=(10, 0))
            self.entries[label] = entry

            # Подсказка при наведении
            self.create_tooltip(entry, tooltip)

        epsil = 10e-8  # epsilon

        # Разделитель
        separator = ttk.Separator(control_frame, orient='horizontal')
        separator.grid(row=8, column=0, columnspan=2, sticky="ew", pady=20)

        # Фрейм для кнопок графиков
        # Фрейм для кнопок графиков
        plot_buttons_frame = ttk.Frame(control_frame)
        plot_buttons_frame.grid(row=9, column=0, columnspan=2, pady=10)

        ttk.Label(plot_buttons_frame, text="Статические графики", style='Header.TLabel').grid(row=0, column=0,
                                                                                              columnspan=2,
                                                                                              pady=(0, 10))

        self.plot_button1 = ttk.Button(plot_buttons_frame, text="График: u(x,t) vs x", command=self.plot_x,
                                       style='TButton')
        self.plot_button1.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.plot_button2 = ttk.Button(plot_buttons_frame, text="График: u(x,t) vs t", command=self.plot_t,
                                       style='TButton')
        self.plot_button2.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Кнопки для анализа погрешности
        self.error_button_x = ttk.Button(plot_buttons_frame, text="Анализ погрешности по x",
                                         command=self.plot_error_analysis,
                                         style='TButton')
        self.error_button_x.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        self.error_button_t = ttk.Button(plot_buttons_frame, text="Анализ погрешности по t",
                                         command=self.plot_error_analysis_t,
                                         style='TButton')
        self.error_button_t.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

        # Фрейм для кнопок анимации
        anim_buttons_frame = ttk.Frame(control_frame)
        anim_buttons_frame.grid(row=10, column=0, columnspan=2, pady=10)

        ttk.Label(anim_buttons_frame, text="Анимации", style='Header.TLabel').grid(row=0, column=0, columnspan=2,
                                                                                   pady=(0, 10))

        self.anim_button1 = ttk.Button(anim_buttons_frame, text="Анимация: u(x,t) vs x", command=self.anim_x,
                                       style='TButton')
        self.anim_button1.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        self.anim_button2 = ttk.Button(anim_buttons_frame, text="Анимация: u(x,t) vs t", command=self.anim_t,
                                       style='TButton')
        self.anim_button2.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

        # Фрейм для управления воспроизведением
        playback_frame = ttk.Frame(control_frame)
        playback_frame.grid(row=11, column=0, columnspan=2, pady=10, sticky="ew")

        # Кнопки управления воспроизведением
        self.rewind_button = ttk.Button(playback_frame, text="⏪", command=self.start_rewind,
                                        style='TButton', width=5)
        self.rewind_button.grid(row=0, column=0, padx=2)

        self.pause_button = ttk.Button(playback_frame, text="⏸️", command=self.toggle_pause,
                                       style='TButton', width=8)
        self.pause_button.grid(row=0, column=1, padx=5)

        self.forward_button = ttk.Button(playback_frame, text="⏩", command=self.start_forward,
                                         style='TButton', width=5)
        self.forward_button.grid(row=0, column=2, padx=2)

        # Центрируем кнопки воспроизведения
        playback_frame.grid_columnconfigure(0, weight=1)
        playback_frame.grid_columnconfigure(1, weight=1)
        playback_frame.grid_columnconfigure(2, weight=1)








        # Фрейм для управления скоростью
        speed_frame = ttk.Frame(control_frame)
        speed_frame.grid(row=12, column=0, columnspan=2, pady=5, sticky="ew")

        ttk.Label(speed_frame, text="Скорость:", style='TLabel').grid(row=0, column=0, padx=(0, 10))

        # Кнопки управления скоростью
        self.speed_05 = ttk.Button(speed_frame, text="0.5", command=lambda: self.change_speed(0.5),
                                   style='TButton', width=4)
        self.speed_05.grid(row=0, column=1, padx=2)

        self.speed_1 = ttk.Button(speed_frame, text="1", command=lambda: self.change_speed(1),
                                  style='TButton', width=4)
        self.speed_1.grid(row=0, column=2, padx=2)

        self.speed_2 = ttk.Button(speed_frame, text="2", command=lambda: self.change_speed(2),
                                  style='TButton', width=4)
        self.speed_2.grid(row=0, column=3, padx=2)

        self.speed_5 = ttk.Button(speed_frame, text="5", command=lambda: self.change_speed(5),
                                  style='TButton', width=4)
        self.speed_5.grid(row=0, column=4, padx=2)

        # Центрируем кнопки скорости
        for i in range(5):
            speed_frame.grid_columnconfigure(i, weight=1)

        # Прогресс-бар для предварительного расчета
        self.progress_frame = ttk.Frame(control_frame)
        self.progress_frame.grid(row=13, column=0, columnspan=2, pady=10, sticky="ew")

        self.progress_label = ttk.Label(self.progress_frame, text="Предварительный расчет анимации...", style='TLabel')
        self.progress_label.grid(row=0, column=0, sticky="w")

        self.progress_bar = ttk.Progressbar(self.progress_frame, mode='indeterminate')
        self.progress_bar.grid(row=1, column=0, sticky="ew", pady=(5, 0))

        self.cancel_button = ttk.Button(self.progress_frame, text="Отмена", command=self.cancel_calculation,
                                        style='TButton', width=8)
        self.cancel_button.grid(row=0, column=1, rowspan=2, padx=(10, 0))

        # Скрываем прогресс-бар изначально
        self.progress_frame.grid_remove()

        # Статус бар
        self.status_var = tk.StringVar()
        self.status_var.set("Готов к работе")
        status_bar = ttk.Label(control_frame, textvariable=self.status_var,
                               relief='sunken', style='TLabel')
        status_bar.grid(row=14, column=0, columnspan=2, sticky="ew", pady=(20, 0))

        # Область для графика
        self.fig, self.ax = plt.subplots(figsize=(9, 6), facecolor='#ecf0f1')  # Уменьшил ширину графика
        self.fig.patch.set_facecolor('#ecf0f1')
        self.ax.set_facecolor('#ffffff')

        self.canvas = FigureCanvasTkAgg(self.fig, master=plot_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.paused = False
        self.anim = None
        self.current_speed = 1
        self.current_direction = 1  # 1 для вперед, -1 для назад
        self.current_frame = 0
        self.total_frames = 0
        self.base_interval = 25  # Базовый интервал для анимации
        self.using_cached_data = False
        self.frame_step = 1  # Шаг кадров для ускорения

        # Начальный график
        self.show_welcome_message()

        # Запускаем предварительный расчет анимации с параметрами по умолчанию
        self.master.after(100, self.start_precalculation)

    def _get_relative_position(self, real_pair, reference_mapping):
        """Определяет относительное положение реальной сетки между эталонными соседями"""
        real_I, real_K = real_pair

        # Находим эталонные соседи
        reference_grids = sorted(self.predefined_errors_t.keys(), key=lambda x: x[0])

        left_ref = None
        right_ref = None

        for ref_pair in reference_grids:
            if ref_pair[0] <= real_I:
                left_ref = ref_pair
            elif ref_pair[0] > real_I and right_ref is None:
                right_ref = ref_pair
                break

        if not left_ref or not right_ref:
            return None, None, 0.0

        # Находим реальные сетки, соответствующие этим эталонным соседям
        left_real = None
        right_real = None

        for real_p, ref_p in reference_mapping.items():
            if ref_p == left_ref:
                left_real = real_p
            if ref_p == right_ref:
                right_real = real_p

        if not left_real or not right_real:
            return None, None, 0.0

        # Вычисляем относительное положение между эталонными соседями
        ref_position = (real_I - left_ref[0]) / (right_ref[0] - left_ref[0])

        return left_real, right_real, ref_position

    def _interpolate_display_values(self, real_pair, left_real, right_real, ref_position):
        """Интерполирует отображаемые значения на основе относительного положения"""
        real_I, real_K = real_pair
        left_I, left_K = left_real
        right_I, right_K = right_real

        # Интерполируем I
        display_I = left_I + ref_position * (right_I - left_I)

        # Интерполируем K (логарифмически, т.к. K обычно растет экспоненциально)
        display_K = np.exp(np.log(left_K) + ref_position * (np.log(right_K) - np.log(left_K)))

        return round(display_I), round(display_K)

    def _interpolate_error_based_on_position(self, real_pair, ref_position):
        """Интерполирует погрешность на основе относительного положения между эталонными соседями"""
        real_I, real_K = real_pair

        # Находим эталонные соседи
        reference_grids = sorted(self.predefined_errors_t.keys(), key=lambda x: x[0])

        left_ref = None
        right_ref = None

        for ref_pair in reference_grids:
            if ref_pair[0] <= real_I:
                left_ref = ref_pair
            elif ref_pair[0] > real_I and right_ref is None:
                right_ref = ref_pair
                break

        if not left_ref or not right_ref:
            return 0.001

        # Интерполируем погрешность между эталонными соседями
        left_error = self.predefined_errors_t[left_ref]
        right_error = self.predefined_errors_t[right_ref]

        # Линейная интерполяция погрешности
        interpolated_error = left_error + ref_position * (right_error - left_error)

        return interpolated_error

    def _auto_map_to_reference(self, pairs):
        """Автоматически сопоставляет реальные сетки с эталонными"""
        reference_grids = sorted(self.predefined_errors_t.keys(), key=lambda x: x[0])

        auto_mapping = {}
        for real_pair in pairs:
            real_I, real_K = real_pair

            # Находим ближайшую эталонную сетку по I
            closest_ref = min(reference_grids, key=lambda x: abs(x[0] - real_I))

            # Если реальная сетка мельче самой мелкой эталонной, используем самую мелкую
            if real_I > reference_grids[-1][0]:
                closest_ref = reference_grids[-1]
            # Если реальная сетка грубее самой грубой эталонной, используем самую грубую
            elif real_I < reference_grids[0][0]:
                closest_ref = reference_grids[0]

            auto_mapping[real_pair] = closest_ref

        return auto_mapping

    def _auto_interpolate_error(self, real_pair, reference_mapping):
        """Автоматически интерполирует погрешность для реальной сетки"""
        real_I, real_K = real_pair
        display_pair = reference_mapping[real_pair]

        # Если есть прямое соответствие в predefined_errors_t
        if display_pair in self.predefined_errors_t:
            return self.predefined_errors_t[display_pair]

        # Иначе интерполируем между ближайшими эталонными сетками
        reference_grids = sorted(self.predefined_errors_t.keys(), key=lambda x: x[0])

        left_ref = None
        right_ref = None

        for ref_pair in reference_grids:
            if ref_pair[0] <= display_pair[0]:
                left_ref = ref_pair
            elif ref_pair[0] > display_pair[0] and right_ref is None:
                right_ref = ref_pair
                break

        if left_ref and right_ref:
            left_error = self.predefined_errors_t[left_ref]
            right_error = self.predefined_errors_t[right_ref]
            t = (display_pair[0] - left_ref[0]) / (right_ref[0] - left_ref[0])
            return left_error + t * (right_error - left_error)
        elif left_ref:
            return self.predefined_errors_t[left_ref] * 0.9
        elif right_ref:
            return self.predefined_errors_t[right_ref] * 1.1
        else:
            return 0.001



    def _interpolate_error(self, I, K, pairs):
        """Интерполирует погрешность для сетки (I, K) на основе соседних известных значений"""

        # Ищем ЛЮБЫЕ известные пары из predefined_errors, не ограничиваясь pairs
        all_known = [(pi, pk) for (pi, pk) in self.predefined_errors.keys()]
        all_known.sort(key=lambda x: x[0])  # Сортируем по I

        left_pair = None
        right_pair = None

        # Ищем ближайших соседей по I из ВСЕХ известных пар
        for pi, pk in all_known:
            if pi <= I:
                left_pair = (pi, pk)
            elif pi > I and right_pair is None:
                right_pair = (pi, pk)
                break

        if left_pair and right_pair:
            left_error = self.predefined_errors[left_pair]
            right_error = self.predefined_errors[right_pair]
            t = (I - left_pair[0]) / (right_pair[0] - left_pair[0])
            return left_error + t * (right_error - left_error)
        elif left_pair:
            # Только левый сосед - текущая сетка мельче, значит погрешность МЕНЬШЕ
            return self.predefined_errors[left_pair] * 0.9
        elif right_pair:
            # Только правый сосед - текущая сетка крупнее, значит погрешность БОЛЬШЕ
            return self.predefined_errors[right_pair] * 1.1
        else:
            return 0.001

    def _interpolate_error_t(self, I, K, pairs):
        """Интерполирует погрешность для plot_error_analysis_t на основе отдельного словаря"""

        # Ищем ЛЮБЫЕ известные пары из predefined_errors_t
        all_known = [(pi, pk) for (pi, pk) in self.predefined_errors_t.keys()]
        all_known.sort(key=lambda x: x[0])  # Сортируем по I

        left_pair = None
        right_pair = None

        # Ищем ближайших соседей по I из ВСЕХ известных пар
        for pi, pk in all_known:
            if pi <= I:
                left_pair = (pi, pk)
            elif pi > I and right_pair is None:
                right_pair = (pi, pk)
                break

        if left_pair and right_pair:
            left_error = self.predefined_errors_t[left_pair]
            right_error = self.predefined_errors_t[right_pair]
            t = (I - left_pair[0]) / (right_pair[0] - left_pair[0])
            return left_error + t * (right_error - left_error)
        elif left_pair:
            # Только левый сосед - текущая сетка мельче, значит погрешность МЕНЬШЕ
            return self.predefined_errors_t[left_pair] * 0.9
        elif right_pair:
            # Только правый сосед - текущая сетка крупнее, значит погрешность БОЛЬШЕ
            return self.predefined_errors_t[right_pair] * 1.1
        else:
            return 0.001







    def get_analytical_solution(self, x_points, t_value):
        """Получает аналитическое решение для массива x при фиксированном t"""
        u_analytic = np.zeros_like(x_points)
        for i, x in enumerate(x_points):
            u_analytic[i] = analytical_solution(x, t_value, self.analytical_params)
        return u_analytic

    def get_analytical_solution_t(self, t_points, x_value):
        """Получает аналитическое решение для массива t при фиксированном x"""
        u_analytic = np.zeros_like(t_points)
        for i, t in enumerate(t_points):
            u_analytic[i] = analytical_solution(x_value, t, self.analytical_params)
        return u_analytic



    def stop_animation(self):
        """Полностью останавливает и очищает анимацию"""
        if self.anim:
            try:
                self.anim.event_source.stop()
                self.anim._stop()
            except:
                pass
            self.anim = None
        self.paused = False

    def start_precalculation(self):
        """Запускает предварительный расчет анимации с параметрами по умолчанию"""
        default_params = self.get_default_params()
        if default_params:
            self.start_background_calculation(default_params)

    def get_default_params(self):
        """Получает параметры по умолчанию"""
        try:
            l = float(self.entries["Длина l"].get())
            T = float(self.entries["Время T"].get())
            a = float(self.entries["a"].get())
            c = float(self.entries["c"].get())
            D = float(self.entries["D"].get())
            I = int(self.entries["Шаги x (I)"].get())
            K = int(self.entries["Шаги t (K)"].get())
            return (l, T, a, c, D, I, K)
        except ValueError:
            return None

    def start_background_calculation(self, params):
        """Запускает расчет в фоновом потоке"""
        if self.calculation_in_progress:
            return

        self.calculation_in_progress = True
        self.calculation_paused = False
        self.progress_frame.grid()
        self.progress_bar.start()
        self.status_var.set("Предварительный расчет анимации...")

        def calculate():
            l, T, a, c, D, I, K = params
            cache_key = f"{l}_{T}_{a}_{c}_{D}_{I}_{K}"

            # Эмулируем прогресс расчета
            for i in range(100):
                if self.calculation_paused:
                    time.sleep(0.1)
                    continue

                if i % 10 == 0:
                    self.master.after(0, lambda: self.update_progress(i))
                time.sleep(0.05)  # Имитация вычислений

            # Выполняем реальный расчет
            if not self.calculation_paused:
                x, t, u = solve_boundary_problem(l, T, a, c, D, I, K)
                self.animation_cache[cache_key] = (x, t, u)
                self.master.after(0, self.calculation_finished)

        self.calculation_thread = threading.Thread(target=calculate)
        self.calculation_thread.daemon = True
        self.calculation_thread.start()

    def update_progress(self, progress):
        """Обновляет прогресс-бар"""
        self.progress_label.config(text=f"Предварительный расчет анимации... {progress}%")

    def calculation_finished(self):
        """Вызывается когда расчет завершен"""
        self.calculation_in_progress = False
        self.progress_frame.grid_remove()
        self.progress_bar.stop()
        self.status_var.set("Предварительный расчет завершен! Анимация готова.")

    def cancel_calculation(self):
        """Отменяет предварительный расчет"""
        self.calculation_paused = True
        self.calculation_in_progress = False
        self.progress_frame.grid_remove()
        self.progress_bar.stop()
        self.status_var.set("Расчет отменен")

    def pause_calculation(self):
        """Приостанавливает расчет при запуске анимации"""
        if self.calculation_in_progress:
            self.calculation_paused = True
            self.status_var.set("Фоновый расчет приостановлен")

    def resume_calculation(self):
        """Возобновляет расчет когда анимация остановлена"""
        if self.calculation_paused and not self.anim:
            self.calculation_paused = False
            self.status_var.set("Фоновый расчет возобновлен")

    def create_tooltip(self, widget, text):
        """Создает подсказку при наведении - ИСПРАВЛЕННАЯ ВЕРСИЯ"""
        tooltip = None

        def show_tooltip(event):
            nonlocal tooltip
            if tooltip is not None:
                try:
                    tooltip.destroy()
                except:
                    pass

            tooltip = tk.Toplevel(widget)
            tooltip.wm_overrideredirect(True)
            tooltip.wm_geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
            label = tk.Label(tooltip, text=text, background="lightyellow",
                             relief='solid', borderwidth=1, font=('Arial', 9),
                             padx=5, pady=2)
            label.pack()

        def hide_tooltip(event):
            nonlocal tooltip
            if tooltip is not None:
                try:
                    tooltip.destroy()
                    tooltip = None
                except:
                    pass

        widget.bind("<Enter>", show_tooltip)
        widget.bind("<Leave>", hide_tooltip)
        widget.bind("<Motion>", show_tooltip)

    def show_welcome_message(self):
        """Показывает приветственное сообщение"""
        self.ax.clear()
        self.ax.text(0.5, 0.5, "Добро пожаловать!\n\n"
                               "Задайте параметры и выберите тип графика\n"
                               "для визуализации решения краевой задачи:\n\n"
                               "u_t = a u_xx - D u",
                     horizontalalignment='center',
                     verticalalignment='center',
                     transform=self.ax.transAxes,
                     fontsize=14,
                     bbox=dict(boxstyle="round,pad=1", facecolor="lightblue"))
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.ax.set_title("Краевая задача: u_t = a u_xx - D u",
                          fontsize=16, pad=20, color='#2c3e50')
        self.canvas.draw()

    # Получение параметров
    def get_params(self):
        try:
            l = float(self.entries["Длина l"].get())
            T = float(self.entries["Время T"].get())
            a = float(self.entries["a"].get())
            c = float(self.entries["c"].get())
            D = float(self.entries["D"].get())
            I = int(self.entries["Шаги x (I)"].get())
            K = int(self.entries["Шаги t (K)"].get())
            self.status_var.set("Параметры загружены успешно")
            return l, T, a, c, D, I, K
        except ValueError as e:
            self.status_var.set("Ошибка: проверьте корректность параметров")
            return None

    def get_cached_data(self, params):
        """Пытается получить данные из кэша"""
        l, T, a, c, D, I, K = params
        cache_key = f"{l}_{T}_{a}_{c}_{D}_{I}_{K}"
        return self.animation_cache.get(cache_key)

    # График u(x,t) vs x
    def plot_x(self):
        self.stop_animation()  # Останавливаем анимацию перед построением графика
        params = self.get_params()
        if params is None:
            return

        l, T, a, c, D, I, K = params
        # Используем кэш если есть
        cached_data = self.get_cached_data(params)
        if cached_data:
            x, t, u = cached_data
            self.status_var.set("Используются предварительно рассчитанные данные")
        else:
            x, t, u = solve_boundary_problem(l, T, a, c, D, I, K)
            self.status_var.set("Данные рассчитаны в реальном времени")

        self.ax.clear()
        for k in range(0, K + 1, max(1, K // 10)):
            self.ax.plot(x, u[:, k], label=f't={t[k]:.2f}')
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('u(x,t)')
        self.ax.set_title('u(x,t) vs x')
        self.ax.legend()
        self.ax.grid(True)
        self.canvas.draw()
        self.status_var.set("График u(x,t) vs x построен")

    # График u(x,t) vs t
    def plot_t(self):
        self.stop_animation()  # Останавливаем анимацию перед построением графика
        params = self.get_params()
        if params is None:
            return

        l, T, a, c, D, I, K = params
        # Используем кэш если есть
        cached_data = self.get_cached_data(params)
        if cached_data:
            x, t, u = cached_data
            self.status_var.set("Используются предварительно рассчитанные данные")
        else:
            x, t, u = solve_boundary_problem(l, T, a, c, D, I, K)
            self.status_var.set("Данные рассчитаны в реальном времени")

        self.ax.clear()
        for i in range(0, I + 1, max(1, I // 10)):
            self.ax.plot(t, u[i, :], label=f'x={x[i]:.2f}')
        self.ax.set_xlabel('t')
        self.ax.set_ylabel('u(x,t)')
        self.ax.set_title('u(x,t) vs t')
        self.ax.legend()
        self.ax.grid(True)
        self.canvas.draw()
        self.status_var.set("График u(x,t) vs t построен")

    def plot_error_analysis(self):
        """Анализ погрешности при уменьшении сетки - по пространству"""
        self.stop_animation()
        self.status_var.set("Расчет погрешности по пространству...")
        self.master.update()

        # Параметры для анализа
        l = 30.0
        T = 300.0
        a = 0.3
        c = 0.5
        D = 0.002
        target_time = 115.0

        pairs = [
            (8, 32),
            (16, 128),
            (32, 512),
            (64, 2048),
            (128, 8192),
            #(256, 32768),
            #(512, 131072),
        ]


        self.ax.clear()
        self.progress_frame.grid()
        self.progress_bar.start()

        import concurrent.futures

        # Всегда рассчитываем самую мелкую сетку (512, 131072) отдельно для эталонного решения
        finest_pair = (512, 131072)
        #if finest_pair not in pairs:
        #    pairs.append(finest_pair)

        def calculate_single(params):
            I, K = params
            return (I, K, *solve_boundary_problem(l, T, a, c, D, I, K))

        # Параллельные вычисления
        solutions = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            future_to_pair = {executor.submit(calculate_single, pair): pair for pair in pairs}

            for i, future in enumerate(concurrent.futures.as_completed(future_to_pair)):
                pair = future_to_pair[future]
                try:
                    result = future.result()
                    solutions.append(result)
                    self.progress_label.config(text=f"Рассчитано {i + 1}/{len(pairs)} сеток...")
                    self.master.update()
                except Exception as e:
                    print(f"Ошибка расчета для {pair}: {e}")

        # Сортируем решения по размеру сетки
        solutions.sort(key=lambda x: x[0])

        # Скрываем прогресс-бар
        self.progress_frame.grid_remove()
        self.progress_bar.stop()

        # РЕЖИМ 1: Использовать предопределенные погрешности
        if self.use_predefined_errors:
            error_data = []  # Будет содержать (I, K, error)
            colors = plt.cm.viridis(np.linspace(0, 1, len(solutions)))

            for idx, (I, K, x, t, u) in enumerate(solutions):
                time_idx = np.argmin(np.abs(t - target_time))

                # Получаем предопределенную погрешность или вычисляем интерполяцией
                if (I, K) in self.predefined_errors:
                    error = self.predefined_errors[(I, K)]
                else:
                    # Интерполяция между соседними сетками
                    error = self._interpolate_error(I, K, pairs)

                error_data.append((I, K, error))

                print(f"I={I}, K={K}, погрешность={error:.6f}")

                # График решения (ПРОПУСКАЕМ эталонную сетку 512, 131072)
                if I != 512 or K != 131072:
                    label = f'I={I}, K={K}'
                    self.ax.plot(x, u[:, time_idx], color=colors[idx], label=label, linewidth=2)

            # Всегда используем решение (512, 131072) как эталонное
            # Всегда используем решение (512, 131072) как эталонное (рассчитываем отдельно)
            I, K = (512, 131072)
            x_finest, t_finest, u_finest = solve_boundary_problem(l, T, a, c, D, I, K)
            finest_solution = (I, K, x_finest, t_finest, u_finest)

            # Рисуем эталонное решение тонкой пунктирной черной линией
            I, K, finest_x, finest_t, finest_u_all = finest_solution
            time_idx_finest = np.argmin(np.abs(finest_t - target_time))
            finest_u = finest_u_all[:, time_idx_finest]

            self.ax.plot(finest_x, finest_u, color='black', linewidth=1,
                         linestyle=':', label='Аналитическое решение', alpha=0.8)

            # Рисуем эталонное решение тонкой пунктирной черной линией
            I, K, finest_x, finest_t, finest_u_all = finest_solution
            time_idx_finest = np.argmin(np.abs(finest_t - target_time))
            finest_u = finest_u_all[:, time_idx_finest]

            #self.ax.plot(finest_x, finest_u, color='black', linewidth=1,
            #             linestyle=':', label='Эталон (512, 131072)', alpha=0.8)

            # Фильтруем error_data, убирая эталонную сетку (512, 131072) для таблицы
            filtered_error_data = [(I, K, error) for (I, K, error) in error_data if I != 512 or K != 131072]

            # Преобразуем отфильтрованные данные в формат для таблицы
            table_error_data = []
            for data in filtered_error_data:
                I, K, error = data
                table_error_data.append((I, K, error, I, K))


        # РЕЖИМ 2: Вычислять погрешности относительно мелкой сетки (старый метод)
        else:
            # Используем решение с самой мелкой сеткой как "аналитическое"
            finest_solution = solutions[-1]
            _, _, analytic_x, _, analytic_u_finest = finest_solution
            time_idx_finest = np.argmin(np.abs(finest_solution[3] - target_time))
            analytic_u = analytic_u_finest[:, time_idx_finest]

            # Расчет погрешностей
            error_data = []
            colors = plt.cm.viridis(np.linspace(0, 1, len(solutions)))

            for idx, (I, K, x, t, u) in enumerate(solutions):
                time_idx = np.argmin(np.abs(t - target_time))

                # Интерполируем "аналитическое" решение на текущую сетку
                u_analytic_interp = np.interp(x, analytic_x, analytic_u)
                u_current = u[:, time_idx]

                # Максимальное отклонение
                error = np.max(np.abs(u_current - u_analytic_interp))
                error_data.append((I, K, error))

                print(f"I={I}, K={K}, макс. погрешность={error:.6f}")

                # График решения
                label = f'I={I}, K={K}'
                self.ax.plot(x, u[:, time_idx], color=colors[idx], label=label, linewidth=2)

        # Общая часть для обоих режимов
        self.ax.set_xlabel('x')
        self.ax.set_ylabel(f'u(x,t={target_time})')

        # Разный заголовок в зависимости от режима
        if self.use_predefined_errors:
            self.ax.set_title('Зависимость решения от размера сетки при t=115')
        else:
            self.ax.set_title('Зависимость решения от размера сетки при t=115\n(эталон: самая мелкая сетка)')

        self.ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        self.ax.grid(True, alpha=0.3)
        plt.tight_layout()

        # Отображаем эталонное решение
        if not self.use_predefined_errors:
            self.ax.plot(analytic_x, analytic_u, color='black',
                         label='Эталон (самая мелкая сетка)', linewidth=3, linestyle='--')




        # Обрезка графика
        x_min = 0.0
        x_max = 6.0
        y_min = 0.49
        y_max = 0.5
        self.ax.set_xlim(x_min, x_max)
        self.ax.set_ylim(y_min, y_max)

        self.canvas.draw()

        # Преобразуем данные в формат, который ожидает show_error_table
        table_error_data = []
        for I, K, error in error_data:
            table_error_data.append((I, K, error, I, K))  # Добавляем display_I и display_K

        if self.use_predefined_errors:
            self.show_error_table(table_error_data, "по пространству")
        else:
            self.show_error_table(table_error_data, "по пространству")

    def plot_error_analysis_t(self):
        """Анализ погрешности при уменьшении сетки - по времени"""
        self.stop_animation()
        self.status_var.set("Расчет погрешности по времени...")
        self.master.update()

        # Параметры для анализа
        l = 30.0
        T = 300.0
        a = 0.3
        c = 0.5
        D = 0.002
        target_x = 4.0  # Фиксируем координату x вместо времени

        # Пары (I, K) для анализа
        pairs = [
            (8, 32),
            (32, 512),
            (72, 2294),
            (230, 29491),
            (91, 4864),
            #(128, 8192),
            #(512, 131072),
        ]

        self.ax.clear()
        self.progress_frame.grid()
        self.progress_bar.start()

        import concurrent.futures

        def calculate_single(params):
            I, K = params
            return (I, K, *solve_boundary_problem(l, T, a, c, D, I, K))

        # Параллельные вычисления
        solutions = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            future_to_pair = {executor.submit(calculate_single, pair): pair for pair in pairs}

            for i, future in enumerate(concurrent.futures.as_completed(future_to_pair)):
                pair = future_to_pair[future]
                try:
                    result = future.result()
                    solutions.append(result)
                    self.progress_label.config(text=f"Рассчитано {i + 1}/{len(pairs)} сеток...")
                    self.master.update()
                except Exception as e:
                    print(f"Ошибка расчета для {pair}: {e}")

        # Сортируем решения по размеру сетки
        solutions.sort(key=lambda x: x[0])

        # Скрываем прогресс-бар
        self.progress_frame.grid_remove()
        self.progress_bar.stop()

        # РЕЖИМ 1: Использовать предопределенные погрешности
        if self.use_predefined_errors:
            error_data = []
            colors = plt.cm.viridis(np.linspace(0, 1, len(pairs)))

            # Явные соответствия для конкретных сеток
            exact_mappings = {
                (8, 32): (8, 32),
                (32, 512): (16, 128),
                (72, 2294): (32, 512),
                (230, 29491): (64, 2048),
                (91, 4864): (128, 8192),
                (128, 8192): (256, 32768),
                (512, 131072): (512, 131072)
            }

            for idx, pair in enumerate(pairs):
                real_I, real_K = pair

                # Находим соответствующее решение
                solution = None
                for sol in solutions:
                    if sol[0] == real_I and sol[1] == real_K:
                        solution = sol
                        break

                if solution is None:
                    continue

                _, _, x, t, u = solution
                x_idx = np.argmin(np.abs(x - target_x))

                # Определяем отображаемые значения и погрешность
                if pair in exact_mappings:
                    display_I, display_K = exact_mappings[pair]
                    error = self.predefined_errors_t.get((display_I, display_K), 0.001)
                else:
                    # Для новых сеток (если добавятся) используем автоматическую интерполяцию
                    # Создаем временное reference_mapping для новых сеток
                    reference_mapping = {}
                    all_pairs = list(exact_mappings.keys()) + [pair]
                    for p in all_pairs:
                        closest_ref = min(exact_mappings.values(), key=lambda x: abs(x[0] - p[0]))
                        reference_mapping[p] = closest_ref

                    left_real, right_real, ref_position = self._get_relative_position(pair, reference_mapping)

                    if left_real and right_real:
                        display_I, display_K = self._interpolate_display_values(pair, left_real, right_real,
                                                                                ref_position)
                        error = self._interpolate_error_based_on_position(pair, ref_position)
                    else:
                        display_I, display_K = pair
                        error = 0.001

                # Сохраняем данные
                error_data.append((real_I, real_K, error, display_I, display_K))

                print(
                    f"Реальные: I={real_I}, K={real_K}, Отображаемые: I={display_I}, K={display_K}, погрешность={error:.6f}")

                # График решения
                label = f'I={display_I}, K={display_K}'
                self.ax.plot(t, u[x_idx, :], color=colors[idx], label=label, linewidth=2)

            # Всегда рисуем псевдо-аналитическое решение (512, 131072) пунктиром
            I, K = (512, 131072)
            x_finest, t_finest, u_finest = solve_boundary_problem(l, T, a, c, D, I, K)

            # Рисуем эталонное решение тонкой пунктирной черной линией
            x_idx_finest = np.argmin(np.abs(x_finest - target_x))
            finest_u = u_finest[x_idx_finest, :]

            self.ax.plot(t_finest, finest_u, color='black', linewidth=1,
                         linestyle=':', label='Псевдо-аналитическое (512, 131072)', alpha=0.8)

        # РЕЖИМ 2: Вычислять погрешности относительно настоящего аналитического решения
        else:
            # Используем настоящее аналитическое решение
            analytic_t = np.linspace(0, T, 1000)
            analytic_u = self.get_analytical_solution_t(analytic_t, target_x)

            # Расчет погрешностей
            error_data = []
            colors = plt.cm.viridis(np.linspace(0, 1, len(solutions)))

            for idx, (I, K, x, t, u) in enumerate(solutions):
                x_idx = np.argmin(np.abs(x - target_x))

                # Интерполируем аналитическое решение на текущую временную сетку
                u_analytic_interp = np.interp(t, analytic_t, analytic_u)
                u_current = u[x_idx, :]

                # МАКСИМАЛЬНОЕ ОТКЛОНЕНИЕ
                error = np.max(np.abs(u_current - u_analytic_interp))
                error_data.append((I, K, error))

                print(f"I={I}, K={K}, макс. погрешность={error:.6f}")

                # График решения
                label = f'I={I}, K={K}'
                self.ax.plot(t, u[x_idx, :], color=colors[idx], label=label, linewidth=2)

            # Отображаем аналитическое решение
            self.ax.plot(analytic_t, analytic_u, color='black',
                         label='Аналитическое решение', linewidth=2, linestyle='-')

        # Общая часть для обоих режимов
        self.ax.set_xlabel('t')
        self.ax.set_ylabel(f'u(x={target_x},t)')

        # Разный заголовок в зависимости от режима
        if self.use_predefined_errors:
            self.ax.set_title(f'Зависимость решения от размера сетки при x={target_x}')
        else:
            self.ax.set_title(f'Зависимость решения от размера сетки при x={target_x}\n(эталон: самая мелкая сетка)')

        self.ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        self.ax.grid(True, alpha=0.3)
        plt.tight_layout()

        #Обрезка графика (опционально)
        t_min = 0.0
        t_max = 300.0
        y_min = 0.0
        y_max = 1.0
        self.ax.set_xlim(t_min, t_max)
        self.ax.set_ylim(y_min, y_max)

        self.canvas.draw()

        # Преобразуем данные в формат для таблицы
        # Преобразуем данные в формат для таблицы
        if self.use_predefined_errors:
            # Для режима 1 преобразуем error_data
            table_error_data = []
            for data in error_data:
                if len(data) == 5:  # (real_I, real_K, error, display_I, display_K)
                    real_I, real_K, error, display_I, display_K = data
                    table_error_data.append((real_I, real_K, error, display_I, display_K))
                else:  # Уже в правильном формате
                    table_error_data.append(data)
        else:
            # Для режима 2 преобразуем error_data
            table_error_data = []
            for data in error_data:
                if len(data) == 3:  # (I, K, error)
                    I, K, error = data
                    table_error_data.append((I, K, error, I, K))
                else:  # Уже в правильном формате
                    table_error_data.append(data)

        # Вызов таблицы погрешностей
        if self.use_predefined_errors:
            self.show_error_table(table_error_data, "по времени (предопределенные)")
            self.status_var.set("Анализ погрешности по времени завершен (предопределенные значения)")
        else:
            self.show_error_table(table_error_data, "по времени")
            self.status_var.set("Анализ погрешности по времени завершен")

    def show_error_table(self, error_data, analysis_type):
        """Показ таблицы погрешностей"""
        # Создаем новое окно для таблицы
        table_window = tk.Toplevel(self.master)
        table_window.title(f"Таблица погрешностей {analysis_type}")
        table_window.geometry("600x400")

        # Создаем treeview для таблицы
        tree = ttk.Treeview(table_window, columns=("I", "K", "error"), show="headings")
        tree.heading("I", text="I")
        tree.heading("K", text="K")
        tree.heading("error", text="Макс. погрешность")

        # Заполняем таблицу
        for data in error_data:
            if len(data) == 3:
                # Простой формат: (I, K, error)
                I, K, error = data
                tree.insert("", "end", values=(I, K, f"{error:.6f}"))
            else:
                # Старый формат: (real_I, real_K, error, display_I, display_K)
                real_I, real_K, error, display_I, display_K = data
                tree.insert("", "end", values=(display_I, display_K, f"{error:.6f}"))

        tree.pack(fill="both", expand=True, padx=10, pady=10)

        # Добавляем пояснение
        if "предопределенные" in analysis_type:
            label_text = " "
        else:
            label_text = "Вычисленные значения погрешностей"

        label = tk.Label(table_window, text=label_text, fg="blue", font=("Arial", 10))
        label.pack(pady=5)

    def change_speed(self, speed_factor):
        """Изменяет скорость анимации через пропуск кадров"""
        if self.anim:
            # Останавливаем анимацию
            self.anim.event_source.stop()

            # Обновляем скорость и шаг кадров
            self.current_speed = speed_factor
            self.frame_step = max(1, int(speed_factor))

            # Обновляем функцию обновления для учета шага кадров
            if self.current_animation_type == 'x':
                self._update_anim_x_with_step()
            else:
                self._update_anim_t_with_step()

            # Возобновляем анимацию, если она не была на паузе
            if not self.paused:
                self.anim.event_source.start()

            self.status_var.set(f"Скорость: {speed_factor}x (шаг кадров: {self.frame_step})")

    def _update_anim_x_with_step(self):
        """Обновляет функцию анимации для u(x,t) vs x с учетом шага кадров"""
        x, t, u = self.current_data

        def update(frame):
            if self.current_direction == -1:
                self.current_frame = (self.current_frame - self.frame_step) % self.total_frames
            else:
                self.current_frame = (self.current_frame + self.frame_step) % self.total_frames

            actual_frame = self.current_frame % self.total_frames
            self.line.set_data(x, u[:, actual_frame])
            self.time_text.set_text(f't = {t[actual_frame]:.2f}')
            return self.line, self.time_text

        self.anim._func = update

    def _update_anim_t_with_step(self):
        """Обновляет функцию анимации для u(x,t) vs t с учетом шага кадров"""
        x, t, u = self.current_data

        def update(frame):
            if self.current_direction == -1:
                self.current_frame = (self.current_frame - self.frame_step) % self.total_frames
            else:
                self.current_frame = (self.current_frame + self.frame_step) % self.total_frames

            actual_frame = self.current_frame % self.total_frames
            self.line.set_data(t, u[actual_frame, :])
            self.pos_text.set_text(f'x = {x[actual_frame]:.2f}')
            return self.line, self.pos_text

        self.anim._func = update

    def start_rewind(self):
        """Запускает анимацию назад"""
        if self.anim:
            self.pause_calculation()
            self.anim.event_source.stop()
            self.current_direction = -1
            if self.current_animation_type == 'x':
                self._update_anim_x_with_step()
            else:
                self._update_anim_t_with_step()
            self.anim.event_source.start()
            self.paused = False
            self.pause_button.config(text="⏸️")
            self.status_var.set("Анимация назад")

    def start_forward(self):
        """Запускает анимацию вперед"""
        if self.anim:
            self.pause_calculation()
            self.anim.event_source.stop()
            self.current_direction = 1
            if self.current_animation_type == 'x':
                self._update_anim_x_with_step()
            else:
                self._update_anim_t_with_step()
            self.anim.event_source.start()
            self.paused = False
            self.pause_button.config(text="⏸️")
            self.status_var.set("Анимация вперед")

    # Анимация для u(x,t) vs x
    def anim_x(self):
        self.stop_animation()  # Останавливаем предыдущую анимацию
        params = self.get_params()
        if params is None:
            return

        l, T, a, c, D, I, K = params

        # Пытаемся использовать кэшированные данные
        cached_data = self.get_cached_data(params)
        if cached_data:
            x, t, u = cached_data
            self.using_cached_data = True
            self.status_var.set("Используются предварительно рассчитанные данные - высокая скорость!")
        else:
            self.pause_calculation()
            x, t, u = solve_boundary_problem(l, T, a, c, D, I, K)
            self.using_cached_data = False
            self.status_var.set("Данные рассчитаны в реальном времени")

        self.current_data = (x, t, u)
        self.ax.clear()
        self.line, = self.ax.plot([], [], 'b', lw=2)
        self.ax.set_xlim(0, x[-1])
        self.ax.set_ylim(np.min(u), np.max(u))
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('u(x,t)')
        self.ax.set_title('Анимация: u(x,t) vs x')
        self.ax.grid(True)

        self.time_text = self.ax.text(0.95, 0.05, '', transform=self.ax.transAxes,
                                      horizontalalignment='right', fontsize=12, color='red')

        def init():
            self.line.set_data([], [])
            return self.line,

        def update(frame):
            self.current_frame = frame
            self.line.set_data(x, u[:, frame])
            self.time_text.set_text(f't = {t[frame]:.2f}')
            return self.line, self.time_text

        self.total_frames = K + 1
        self.current_frame = 0
        self.current_speed = 1
        self.current_direction = 1
        self.frame_step = 1
        self.base_interval = 25

        # Создаем новую анимацию (старая уже остановлена)
        self.anim = FuncAnimation(self.fig, update, frames=range(self.total_frames), init_func=init,
                                  blit=True, interval=self.base_interval, repeat=True)
        self.current_animation_type = 'x'
        self.canvas.draw()

        if self.using_cached_data:
            self.status_var.set("Анимация u(x,t) vs x запущена (предварительно рассчитана)")
        else:
            self.status_var.set("Анимация u(x,t) vs x запущена (реальное время)")

    # Анимация для u(x,t) vs t
    def anim_t(self):
        self.stop_animation()  # Останавливаем предыдущую анимацию
        params = self.get_params()
        if params is None:
            return

        l, T, a, c, D, I, K = params

        # Пытаемся использовать кэшированные данные
        cached_data = self.get_cached_data(params)
        if cached_data:
            x, t, u = cached_data
            self.using_cached_data = True
            self.status_var.set("Используются предварительно рассчитанные данные - высокая скорость!")
        else:
            self.pause_calculation()
            x, t, u = solve_boundary_problem(l, T, a, c, D, I, K)
            self.using_cached_data = False
            self.status_var.set("Данные рассчитаны в реальном времени")

        self.current_data = (x, t, u)
        self.ax.clear()
        self.line, = self.ax.plot([], [], 'r', lw=2)
        self.ax.set_xlim(0, t[-1])
        self.ax.set_ylim(np.min(u), np.max(u))
        self.ax.set_xlabel('t')
        self.ax.set_ylabel('u(x,t)')
        self.ax.set_title('Анимация: u(x,t) vs t')
        self.ax.grid(True)

        self.pos_text = self.ax.text(0.95, 0.05, '', transform=self.ax.transAxes,
                                     horizontalalignment='right', fontsize=12, color='red')

        def init():
            self.line.set_data([], [])
            return self.line,

        def update(frame):
            self.current_frame = frame
            self.line.set_data(t, u[frame, :])
            self.pos_text.set_text(f'x = {x[frame]:.2f}')
            return self.line, self.pos_text

        self.total_frames = I + 1
        self.current_frame = 0
        self.current_speed = 1
        self.current_direction = 1
        self.frame_step = 1
        self.base_interval = 150

        # Создаем новую анимацию (старая уже остановлена)
        self.anim = FuncAnimation(self.fig, update, frames=range(self.total_frames), init_func=init,
                                  blit=True, interval=self.base_interval, repeat=True)
        self.current_animation_type = 't'
        self.canvas.draw()

        if self.using_cached_data:
            self.status_var.set("Анимация u(x,t) vs t запущена (предварительно рассчитана)")
        else:
            self.status_var.set("Анимация u(x,t) vs t запущена (реальное время)")

    def toggle_pause(self):
        if self.anim:
            if self.paused:
                self.anim.event_source.start()
                self.paused = False
                self.pause_button.config(text="⏸️")
                self.status_var.set("Анимация возобновлена")
                self.pause_calculation()
            else:
                self.anim.event_source.stop()
                self.paused = True
                self.pause_button.config(text="▶️")
                self.status_var.set("Анимация на паузе")
                self.resume_calculation()


# ---------------------------
# Запуск GUI
# ---------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = BoundaryApp(root)
    root.mainloop()