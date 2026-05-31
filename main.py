import json
import os

DATA_FILE = "books.json"

def load_books():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_books(books):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

def add_book(books):
    author = input("Автор: ").strip()
    title = input("Название: ").strip()
    
    # Проверка дубликатов (повод для Issue)
    if any(b["author"] == author and b["title"] == title for b in books):
        print("⚠️ Эта книга уже добавлена!")
        return books
    
    while True:
        try:
            rating = int(input("Оценка (1-5): "))
            if 1 <= rating <= 5:
                break
            print("Оценка должна быть от 1 до 5.")
        except ValueError:
            print("Введите целое число.")
            
    date = input("Дата прочтения (YYYY-MM-DD): ").strip()
    books.append({"author": author, "title": title, "rating": rating, "date_read": date})
    save_books(books)
    print("✅ Книга добавлена.")
    return books

def show_books(books):
    if not books:
        print("📚 Список пуст.")
        return
    for i, b in enumerate(books, 1):
        print(f"{i}. {b['title']} — {b['author']} | Оценка: {b['rating']} | Дата: {b['date_read']}")

def show_avg_rating(books):
    if not books:
        print("Нет данных для расчёта.")
        return
    avg = sum(b["rating"] for b in books) / len(books)
    print(f"📊 Средняя оценка: {avg:.2f}")

def show_author_stats(books):
    if not books:
        print("Нет данных для статистики.")
        return
    stats = {}
    for b in books:
        stats[b["author"]] = stats.get(b["author"], 0) + 1
    print("📈 Книги по авторам:")
    for author, count in stats.items():
        print(f"  {author}: {count}")

def delete_book(books):
    show_books(books)
    if not books:
        return books
    try:
        idx = int(input("Введите номер книги для удаления: ")) - 1
        if 0 <= idx < len(books):
            removed = books.pop(idx)
            save_books(books)
            print(f"🗑️ Удалена: '{removed['title']}'")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Введите число.")
    return books

def main():
    books = load_books()
    while True:
        print("\n📖 Трекер прочитанных книг")
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Показать среднюю оценку")
        print("4. Статистика по авторам")
        print("5. Удалить книгу")
        print("6. Выход")
        
        choice = input("Выбор: ").strip()
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
            print("👋 До встречи!")
            break
        else:
            print("❌ Неверный пункт меню.")

if __name__ == "__main__":
    main()