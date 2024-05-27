import random

available_choices = ['Камінь', 'Ножиці', 'Папір']


def game(choice):
    comp_choice = random.choice(available_choices)
    print(f"Комп'ютер обрав: {comp_choice}")

    if choice == comp_choice:
        print("Нічия!")
    elif (choice == 'Камінь' and comp_choice == 'Ножиці') or \
            (choice == 'Ножиці' and comp_choice == 'Папір') or \
            (choice == 'Папір' and comp_choice == 'Камінь'):
        print("Гравець переміг!")
    else:
        print("Комп'ютер переміг!")


player_choice = input("Оберіть Камінь, Ножиці або Папір: ")

if player_choice in available_choices:
    print(f"Гравець обрав: {player_choice}")
    game(player_choice)
else:
    print("Неправильний ввід. Будь ласка, введіть Камінь, Ножиці або Папір.")
