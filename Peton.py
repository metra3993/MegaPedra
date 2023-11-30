import time
import json

def welcome():
    print("Добро пожаловать!")
    for i in [3, 2, 1]:
        print("Загрузка Игры Новеллы")
        print("Игра будет готова через %s" % i, end='')
        print(" секунд")
        time.sleep(i)
    print("Игра готова")

def start_game():
    name = input("Введите ваше имя: ")
    print(f"Салам, {name}! Давай поиграем")
    time.sleep(1)
    print("Ты находишься в темном лесу. Перед тобой развилка.")
    print("1. Пойти налево")
    print("2. Пойти направо")
    time.sleep(2)
    choice1 = input("Куда пойдешь? (1 или 2): ")
    time.sleep(1)
    if choice1 == "1":
        print("Ты идешь налево и встречаешь злого негра.")
        print("1. Сражаться с негром")
        print("2. Убежать от негра")
        choice2 = input("Выбери вариант (1 или 2): ")
        if choice2 == "1":
            print("Ты победил негра! Поздравляю, ты выиграл мешок картошки!")
            return {'result': 'win_with_negro'}
        elif choice2 == "2":
            print("Ты не смог убежать от негра, т.к. на нем не было цепи. "
                  "Он догнал тебя и затанцевал тебя досмерти. Ты умер!")
            print('GAME OVER')
            return {'result': 'lose_with_negro'}
        else:
            print("Неверный ввод. Игра окончена.")
            return {'result': 'invalid_input'}
    elif choice1 == "2":
        print("Ты идешь направо и видишь океан.")
        print("1. Попробовать перепрыгнуть океан")
        print("2. Пойти обратно")
        choice3 = input("Выбери вариант (1 или 2): ")
        if choice3 == "1":
            print("Ты дурак? Ты не смог перепрыгнуть и утонул. Конец игры!")
            return {'result': 'lose_with_ocean'}
        elif choice3 == "2":
            print("Ты вернулся на развилку. Жизнь продолжается.")
            return {'result': 'continue'}
        else:
            print("Неверный ввод. Игра окончена.")
            return {'result': 'invalid_input'}
    else:
        print("Неверный ввод. Игра окончена.")
        return {'result': 'invalid_input'}

def save_progress(data, filename='progress.json'):
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_progress(filename='progress.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def ask_to_save_progress(data):
    save_choice = input("Хотите сохранить результат игры? (да/нет): ").lower()
    if save_choice == "да":
        save_filename = input("Введите имя файла для сохранения: ")
        save_progress(data, save_filename)
        print(f"Результат сохранен в файле {save_filename}.json")

def main():
    welcome()

    saved_progress = load_progress()
    if saved_progress:
        print("Найден сохраненный прогресс!")

    result_data = start_game()

    if 'result' in result_data:
        saved_progress = result_data

    ask_to_save_progress(saved_progress)

main()