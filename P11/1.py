import requests
import json
import tkinter as tk
from tkinter import messagebox

def get_repo_info():
    repo_name = entry.get()  # Получаем введённое имя репозитория
    try:
        owner, repo = repo_name.split('/')
    except ValueError:
        messagebox.showerror("Ошибка", "Введите имя репозитория в формате 'owner/repo'")
        return

    # Запрос к API GitHub для организации/пользователя
    url = f"https://api.github.com/users/{owner}"
    response = requests.get(url)

    if response.status_code != 200:
        messagebox.showerror("Ошибка", f"Ошибка API: {response.status_code}")
        return

    user_data = response.json()

    # Извлекаем нужные поля
    required_fields = {
        'company': user_data.get('company'),
        'created_at': user_data.get('created_at'),
        'email': user_data.get('email'),
        'id': user_data.get('id'),
        'name': user_data.get('name'),
        'url': user_data.get('url')
    }

    # Сохраняем в JSON-файл
    with open('vscode_info.json', 'w', encoding='utf-8') as f:
        json.dump(required_fields, f, indent=4, ensure_ascii=False)

    messagebox.showinfo("Успех", "Данные сохранены в файл 'vscode_info.json'")

# Создаём GUI
root = tk.Tk()
root.title("GitHub Repo Info")

label = tk.Label(root, text="Введите имя репозитория (например, Microsoft/vscode):")
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

button = tk.Button(root, text="Получить данные", command=get_repo_info)
button.pack()

root.mainloop()