import json
import os
from collections import Counter

DATA_FILE = "books.json"


def load_books():
    """Загружает список книг из JSON-файла."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("⚠️ Ошибка чтения файла. Возвращаю пустой список.")
        return []


def save_books(books):
    """Сохраняет список книг в JSON-файл."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)


def add_book(books):
    """Добавляет новую книгу с валидацией и проверкой дубликатов."""
    print("\n📚 Добавление книги")
    
    author = input("Автор: ").strip()
    title = input("Название: ").strip()
    
    # Проверка на дубликаты (автор + название)
    for book in books:
        if book["author"].lower() == author.lower() and book["title"].lower() == title.lower():
            print("⚠️ Эта книга уже есть в списке!")
            return books
    
    # Валидация оценки (1-5)
    while True:
        try:
            rating = int(input("Оценка (1-5): "))
            if 1 <= rating <= 5:
                break
            print("❌ Оценка должна быть от 1 до 5.")
        except ValueError:
            print("❌ Введите целое число.")
    
    date = input("Дата прочтения (например, 2024-01-15): ").strip()
    
    # Добавляем книгу в список
    new_book = {
        "author": author,
        "title": title,
        "rating": rating,
        "date_read": date
    }
    books.append(new_book)
    save_books(books)
    print(f"✅ Книга '{title}' добавлена!")
    return books


def show_books(books):
    """Выводит все книги в красивом формате."""
    print("\n📖 Ваши книги:")
    print("-" * 60)
    
    if not books:
        print("📭 Список пуст. Добавьте первую книгу!")
        return
    
    for idx, book in enumerate(books, start=1):
        # Звёздочки для визуализации оценки
        stars = "⭐" * book["rating"]
        print(f"{idx}. {book['title']}")
        print(f"   👤 {book['author']} | {stars} ({book['rating']}/5) | 📅 {book['date_read']}")
        print("-" * 60)


def show_avg_rating(books):
    """Вычисляет и выводит среднюю оценку."""
    print("\n📊 Средняя оценка")
    print("-" * 60)
    
    if not books:
        print("📭 Нет книг для расчёта.")
        return
    
    total = sum(book["rating"] for book in books)
    average = total / len(books)
    
    # Визуализация средней оценки
    stars = "⭐" * round(average)
    print(f"Всего книг: {len(books)}")
    print(f"Средняя оценка: {average:.2f} {stars}")
    print("-" * 60)


def show_author_stats(books):
    """Выводит статистику: сколько книг у каждого автора."""
    print("\n📈 Статистика по авторам")
    print("-" * 60)
    
    if not books:
        print("📭 Нет книг для статистики.")
        return
    
    # Считаем количество книг на автора
    authors = [book["author"] for book in books]
    stats = Counter(authors)
    
    # Сортируем по количеству (убывание) и выводим
    for author, count in stats.most_common():
        # Рисуем мини-гистограмму
        bar = "▮" * count
        print(f"{author}: {bar} ({count})")
    
    print("-" * 60)
    print(f"Всего авторов: {len(stats)}")


def delete_book(books):
    """Заглушка: функция удаления будет реализована в другой ветке."""
    print("\n🗑️ Удаление книги")
    print("⚠️ Эта функция будет доступна после слияния ветки feature/delete")
    return books


def show_menu():
    """Показывает главное меню и возвращает выбор пользователя."""
    print("\n" + "=" * 60)
    print("📖 ТРЕКЕР ПРОЧИТАННЫХ КНИГ")
    print("=" * 60)
    print("1. ➕ Добавить книгу")
    print("2. 📋 Показать все книги")
    print("3. 📊 Показать среднюю оценку")
    print("4. 📈 Статистика по авторам")
    print("5. 🗑️ Удалить книгу")
    print("6. 🚪 Выход")
    print("-" * 60)
    return input("Ваш выбор (1-6): ").strip()


def main():
    """Главная функция: загружает данные и запускает цикл меню."""
    print("👋 Добро пожаловать в Трекер книг!")
    
    # Загружаем книги при старте
    books = load_books()
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            books = add_book(books)
        elif choice == "2":
            show_books(books)
        elif choice == "3":
            show_avg_rating(books)
        elif choice == "4":
            show_author_stats(books)
        elif choice == "5":
            books = delete_book(books)
        elif choice == "6":
            print("\n👋 Спасибо за использование! До новых встреч 📚")
            break
        else:
            print("❌ Неверный выбор. Пожалуйста, введите число от 1 до 6.")
        
        # Пауза перед возвратом в меню (чтобы пользователь успел прочитать вывод)
        if choice != "6":
            input("\nНажмите Enter, чтобы продолжить...")


# Точка входа в программу
if __name__ == "__main__":
    main()