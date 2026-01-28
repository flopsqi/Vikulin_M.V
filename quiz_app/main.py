import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import json
import random
from datetime import datetime


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("800x600")
        self.root.configure(bg="#f0f0f0")

        # Центрирование окна
        self.center_window(800, 600)

        # Загрузка данных
        self.questions_file = "questions.json"
        self.results_file = "results.json"
        self.questions = self.load_questions()

        # Переменные
        self.current_question_index = 0
        self.score = 0
        self.selected_answer = tk.StringVar()
        self.user_name = ""
        self.quiz_started = False
        self.current_quiz_questions = []

        # Стили
        self.setup_styles()

        # Создание интерфейса
        self.create_widgets()

        # Показать стартовый экран
        self.show_start_screen()

    def center_window(self, width, height):
        """Центрирует окно на экране"""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def setup_styles(self):
        """Настройка стилей для виджетов"""
        style = ttk.Style()
        style.theme_use('clam')

        # Настройка стилей для кнопок
        style.configure('Start.TButton',
                        font=('Arial', 14, 'bold'),
                        padding=10,
                        background='#4CAF50',
                        foreground='white')
        style.configure('Admin.TButton',
                        font=('Arial', 10),
                        padding=5,
                        background='#607D8B')
        style.configure('Answer.TRadiobutton',
                        font=('Arial', 12),
                        padding=10)

    def create_widgets(self):
        """Создание всех виджетов приложения"""
        # Основной фрейм
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Заголовок
        self.title_label = tk.Label(self.main_frame,
                                    text="📚 Quiz Application",
                                    font=('Arial', 24, 'bold'),
                                    bg="#f0f0f0",
                                    fg="#333")
        self.title_label.pack(pady=(0, 20))

        # Фрейм для контента (будет меняться)
        self.content_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        self.content_frame.pack(fill=tk.BOTH, expand=True)

        # Панель администратора (внизу)
        self.admin_frame = tk.Frame(self.root, bg="#e0e0e0", height=40)
        self.admin_frame.pack(side=tk.BOTTOM, fill=tk.X)

        admin_btn = ttk.Button(self.admin_frame,
                               text="🔧 Администратор",
                               style='Admin.TButton',
                               command=self.admin_login)
        admin_btn.pack(pady=5)

    def show_start_screen(self):
        """Отображение стартового экрана"""
        self.clear_content_frame()

        # Информация о тесте
        info_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        info_frame.pack(pady=20)

        tk.Label(info_frame,
                 text=f"Доступно вопросов: {len(self.questions)}",
                 font=('Arial', 14),
                 bg="#f0f0f0").pack()

        # Ввод имени
        name_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        name_frame.pack(pady=20)

        tk.Label(name_frame,
                 text="Введите ваше имя:",
                 font=('Arial', 12),
                 bg="#f0f0f0").pack()

        name_entry = tk.Entry(name_frame, font=('Arial', 12), width=30)
        name_entry.pack(pady=10)
        name_entry.focus()

        # Кнопка старта
        def start_quiz():
            self.user_name = name_entry.get().strip()
            if not self.user_name:
                messagebox.showwarning("Внимание", "Пожалуйста, введите ваше имя")
                return

            self.start_quiz_session()

        start_btn = ttk.Button(self.content_frame,
                               text="🚀 Начать тест",
                               style='Start.TButton',
                               command=start_quiz)
        start_btn.pack(pady=30)

    def start_quiz_session(self):
        """Начало новой сессии тестирования"""
        if not self.questions:
            messagebox.showerror("Ошибка", "Нет доступных вопросов")
            return

        # Выбор случайных вопросов (максимум 5)
        num_questions = min(5, len(self.questions))
        all_questions = list(self.questions.items())
        self.current_quiz_questions = random.sample(all_questions, num_questions)

        self.current_question_index = 0
        self.score = 0
        self.quiz_started = True

        self.show_question()

    def show_question(self):
        """Отображение текущего вопроса"""
        self.clear_content_frame()

        if self.current_question_index >= len(self.current_quiz_questions):
            self.finish_quiz()
            return

        # Получение текущего вопроса
        question, answers = self.current_quiz_questions[self.current_question_index]

        # Отображение прогресса
        progress_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        progress_frame.pack(fill=tk.X, pady=(0, 20))

        tk.Label(progress_frame,
                 text=f"Вопрос {self.current_question_index + 1} из {len(self.current_quiz_questions)}",
                 font=('Arial', 12, 'bold'),
                 bg="#f0f0f0",
                 fg="#666").pack()

        # Сам вопрос
        question_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        question_frame.pack(fill=tk.BOTH, expand=True)

        tk.Label(question_frame,
                 text=question,
                 font=('Arial', 16),
                 bg="#f0f0f0",
                 wraplength=700,
                 justify="left").pack(pady=20)

        # Варианты ответов
        self.selected_answer.set("")  # Сброс выбора

        answers_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        answers_frame.pack(fill=tk.BOTH, expand=True, pady=20)

        # Перемешиваем ответы, но запоминаем правильный (первый в исходном списке)
        correct_answer = answers[0]
        shuffled_answers = random.sample(answers, len(answers))

        for i, answer in enumerate(shuffled_answers):
            rb = tk.Radiobutton(answers_frame,
                                text=answer,
                                variable=self.selected_answer,
                                value=answer,
                                font=('Arial', 12),
                                bg="#f0f0f0",
                                activebackground="#e0e0e0",
                                indicatoron=1,
                                padx=20,
                                pady=8,
                                anchor="w")
            rb.pack(fill=tk.X, padx=50, pady=5)

        # Кнопка ответа
        def submit_answer():
            if not self.selected_answer.get():
                messagebox.showwarning("Внимание", "Пожалуйста, выберите ответ")
                return

            # Проверка ответа (правильный - первый в исходном списке)
            correct = answers[0]
            user_answer = self.selected_answer.get()

            if user_answer == correct:
                self.score += 1

            self.current_question_index += 1
            self.show_question()

        submit_btn = ttk.Button(self.content_frame,
                                text="✓ Ответить" if self.current_question_index < len(
                                    self.current_quiz_questions) - 1 else "🏁 Завершить",
                                style='Start.TButton',
                                command=submit_answer)
        submit_btn.pack(pady=20)

    def finish_quiz(self):
        """Завершение теста и сохранение результата"""
        self.clear_content_frame()

        # Отображение результата
        result_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        result_frame.pack(expand=True)

        # Смайлик в зависимости от результата
        percentage = (self.score / len(self.current_quiz_questions)) * 100
        if percentage >= 80:
            emoji = "🎉"
            color = "#4CAF50"
        elif percentage >= 60:
            emoji = "👍"
            color = "#FFC107"
        else:
            emoji = "📚"
            color = "#F44336"

        tk.Label(result_frame,
                 text=f"{emoji} Тест завершен! {emoji}",
                 font=('Arial', 24, 'bold'),
                 bg="#f0f0f0",
                 fg=color).pack(pady=20)

        tk.Label(result_frame,
                 text=f"Пользователь: {self.user_name}",
                 font=('Arial', 16),
                 bg="#f0f0f0").pack(pady=10)

        tk.Label(result_frame,
                 text=f"Правильных ответов: {self.score} из {len(self.current_quiz_questions)}",
                 font=('Arial', 18, 'bold'),
                 bg="#f0f0f0").pack(pady=10)

        tk.Label(result_frame,
                 text=f"Результат: {percentage:.1f}%",
                 font=('Arial', 20, 'bold'),
                 bg="#f0f0f0",
                 fg=color).pack(pady=20)

        # Сохранение результата
        self.save_result(percentage)

        # Кнопки
        buttons_frame = tk.Frame(self.content_frame, bg="#f0f0f0")
        buttons_frame.pack(pady=30)

        ttk.Button(buttons_frame,
                   text="🔄 Пройти еще раз",
                   style='Start.TButton',
                   command=self.show_start_screen).pack(side=tk.LEFT, padx=10)

        ttk.Button(buttons_frame,
                   text="📊 Посмотреть статистику",
                   style='Admin.TButton',
                   command=self.show_statistics).pack(side=tk.LEFT, padx=10)

    def load_questions(self):
        """Загрузка вопросов из JSON файла"""
        try:
            with open(self.questions_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            # Если файла нет, создаем пример вопросов
            default_questions = {
                "Пример вопроса 1": ["Правильный ответ", "Неправильный 1", "Неправильный 2"],
                "Пример вопроса 2": ["Верный ответ", "Ошибка 1", "Ошибка 2"]
            }
            self.save_questions(default_questions)
            return default_questions

    def save_questions(self, questions):
        """Сохранение вопросов в JSON файл"""
        with open(self.questions_file, 'w', encoding='utf-8') as f:
            json.dump(questions, f, ensure_ascii=False, indent=4)

    def save_result(self, percentage):
        """Сохранение результата теста"""
        try:
            with open(self.results_file, 'r', encoding='utf-8') as f:
                results = json.load(f)
        except FileNotFoundError:
            results = []

        result_entry = {
            "user": self.user_name,
            "score": self.score,
            "total": len(self.current_quiz_questions),
            "percentage": percentage,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        results.append(result_entry)

        with open(self.results_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)

    def show_statistics(self):
        """Показать статистику результатов"""
        try:
            with open(self.results_file, 'r', encoding='utf-8') as f:
                results = json.load(f)
        except FileNotFoundError:
            results = []

        if not results:
            messagebox.showinfo("Статистика", "Результаты тестов отсутствуют")
            return

        # Создание окна статистики
        stats_window = tk.Toplevel(self.root)
        stats_window.title("Статистика результатов")
        stats_window.geometry("600x400")
        stats_window.configure(bg="#f0f0f0")

        # Центрирование
        stats_window.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() - 600) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - 400) // 2
        stats_window.geometry(f"600x400+{x}+{y}")

        # Заголовок
        tk.Label(stats_window,
                 text="📊 Статистика результатов",
                 font=('Arial', 18, 'bold'),
                 bg="#f0f0f0").pack(pady=20)

        # Прокручиваемый фрейм для результатов
        canvas = tk.Canvas(stats_window, bg="#f0f0f0")
        scrollbar = ttk.Scrollbar(stats_window, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#f0f0f0")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Отображение каждого результата
        for i, result in enumerate(reversed(results[-20:])):  # Последние 20 результатов
            result_frame = tk.Frame(scrollable_frame, bg="#e8f5e9" if i % 2 == 0 else "#f1f8e9", padx=10, pady=5)
            result_frame.pack(fill=tk.X, padx=20, pady=2)

            tk.Label(result_frame,
                     text=f"{result['user']}: {result['score']}/{result['total']} ({result['percentage']:.1f}%)",
                     font=('Arial', 11),
                     bg=result_frame['bg']).pack(anchor="w")

            tk.Label(result_frame,
                     text=f"Дата: {result['date']}",
                     font=('Arial', 9),
                     fg="#666",
                     bg=result_frame['bg']).pack(anchor="w")

        canvas.pack(side="left", fill="both", expand=True, padx=20, pady=10)
        scrollbar.pack(side="right", fill="y")

        # Кнопка закрытия
        ttk.Button(stats_window,
                   text="Закрыть",
                   command=stats_window.destroy).pack(pady=10)

    def admin_login(self):
        """Вход в режим администратора"""
        password = simpledialog.askstring("Вход администратора",
                                          "Введите пароль:",
                                          show='*')

        # Простой пароль для демонстрации
        if password == "admin123":
            self.show_admin_panel()
        else:
            messagebox.showerror("Ошибка", "Неверный пароль")

    def show_admin_panel(self):
        """Панель администратора"""
        admin_window = tk.Toplevel(self.root)
        admin_window.title("Панель администратора")
        admin_window.geometry("700x500")
        admin_window.configure(bg="#f0f0f0")

        # Центрирование
        admin_window.update_idletasks()
        x = self.root.winfo_x() + (self.root.winfo_width() - 700) // 2
        y = self.root.winfo_y() + (self.root.winfo_height() - 500) // 2
        admin_window.geometry(f"700x500+{x}+{y}")

        # Заголовок
        tk.Label(admin_window,
                 text="🔧 Панель администратора",
                 font=('Arial', 20, 'bold'),
                 bg="#f0f0f0").pack(pady=20)

        # Вкладки
        tab_control = ttk.Notebook(admin_window)

        # Вкладка 1: Управление вопросами
        questions_tab = tk.Frame(tab_control, bg="#f0f0f0")
        tab_control.add(questions_tab, text="Вопросы")

        # Список вопросов
        questions_listbox = tk.Listbox(questions_tab, font=('Arial', 11), height=15)
        questions_scrollbar = tk.Scrollbar(questions_tab)
        questions_listbox.config(yscrollcommand=questions_scrollbar.set)
        questions_scrollbar.config(command=questions_listbox.yview)

        for question in self.questions:
            questions_listbox.insert(tk.END, question[:80] + "..." if len(question) > 80 else question)

        questions_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        questions_scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=10)

        # Кнопки управления вопросами
        buttons_frame = tk.Frame(questions_tab, bg="#f0f0f0")
        buttons_frame.pack(fill=tk.X, padx=10, pady=10)

        def add_question():
            add_window = tk.Toplevel(admin_window)
            add_window.title("Добавить вопрос")
            add_window.geometry("500x400")

            tk.Label(add_window, text="Текст вопроса:", font=('Arial', 12)).pack(pady=10)
            question_text = tk.Text(add_window, height=4, width=50, font=('Arial', 11))
            question_text.pack(pady=5, padx=20)

            tk.Label(add_window, text="Варианты ответов (первый - правильный):",
                     font=('Arial', 12)).pack(pady=10)

            answers_frame = tk.Frame(add_window)
            answers_frame.pack(pady=5)

            answer_entries = []
            for i in range(4):
                tk.Label(answers_frame, text=f"Ответ {i + 1}:").grid(row=i, column=0, sticky="w", pady=5)
                entry = tk.Entry(answers_frame, width=40, font=('Arial', 11))
                entry.grid(row=i, column=1, pady=5, padx=10)
                answer_entries.append(entry)

            def save_new_question():
                question = question_text.get("1.0", tk.END).strip()
                answers = [entry.get().strip() for entry in answer_entries if entry.get().strip()]

                if not question or len(answers) < 2:
                    messagebox.showwarning("Внимание", "Заполните вопрос и хотя бы 2 ответа")
                    return

                self.questions[question] = answers
                self.save_questions(self.questions)

                questions_listbox.insert(tk.END, question[:80] + "..." if len(question) > 80 else question)
                add_window.destroy()
                messagebox.showinfo("Успех", "Вопрос добавлен!")

            ttk.Button(add_window, text="Сохранить", command=save_new_question).pack(pady=20)

        ttk.Button(buttons_frame, text="Добавить вопрос",
                   command=add_question).pack(side=tk.LEFT, padx=5)

        def delete_question():
            selection = questions_listbox.curselection()
            if not selection:
                messagebox.showwarning("Внимание", "Выберите вопрос для удаления")
                return

            if messagebox.askyesno("Подтверждение", "Удалить выбранный вопрос?"):
                # Находим полный текст вопроса
                selected_index = selection[0]
                selected_text = questions_listbox.get(selected_index)

                # Ищем полное совпадение
                for question in list(self.questions.keys()):
                    if question.startswith(selected_text.replace("...", "")):
                        del self.questions[question]
                        break

                self.save_questions(self.questions)
                questions_listbox.delete(selected_index)

        ttk.Button(buttons_frame, text="Удалить вопрос",
                   command=delete_question).pack(side=tk.LEFT, padx=5)

        # Вкладка 2: Результаты
        results_tab = tk.Frame(tab_control, bg="#f0f0f0")
        tab_control.add(results_tab, text="Результаты")

        # Поиск результатов
        search_frame = tk.Frame(results_tab, bg="#f0f0f0")
        search_frame.pack(fill=tk.X, padx=20, pady=10)

        tk.Label(search_frame, text="Поиск по имени:",
                 font=('Arial', 11), bg="#f0f0f0").pack(side=tk.LEFT)

        search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=search_var, font=('Arial', 11), width=20)
        search_entry.pack(side=tk.LEFT, padx=10)

        results_text = tk.Text(results_tab, height=20, width=80, font=('Arial', 10))
        results_scrollbar = tk.Scrollbar(results_tab)
        results_text.config(yscrollcommand=results_scrollbar.set)
        results_scrollbar.config(command=results_text.yview)

        results_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        results_scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=10)

        def load_results(search_query=""):
            try:
                with open(self.results_file, 'r', encoding='utf-8') as f:
                    results = json.load(f)
            except FileNotFoundError:
                results = []

            results_text.delete(1.0, tk.END)

            if not results:
                results_text.insert(tk.END, "Нет результатов\n")
                return

            filtered_results = []
            if search_query:
                filtered_results = [r for r in results if search_query.lower() in r['user'].lower()]
            else:
                filtered_results = results[-50:]  # Последние 50 результатов

            for result in reversed(filtered_results):
                results_text.insert(tk.END, f"{'=' * 60}\n")
                results_text.insert(tk.END, f"Пользователь: {result['user']}\n")
                results_text.insert(tk.END,
                                    f"Результат: {result['score']}/{result['total']} ({result['percentage']:.1f}%)\n")
                results_text.insert(tk.END, f"Дата: {result['date']}\n")
                results_text.insert(tk.END, f"{'=' * 60}\n\n")

        def on_search(*args):
            load_results(search_var.get())

        search_var.trace("w", on_search)
        load_results()  # Загрузка всех результатов

        tab_control.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Кнопка закрытия
        ttk.Button(admin_window, text="Закрыть",
                   command=admin_window.destroy).pack(pady=10)

    def clear_content_frame(self):
        """Очистка content_frame"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()


def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()