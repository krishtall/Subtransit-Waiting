from funcs import update
from funcs import play

updateReleased = input('Обнова уже есть в плеймаркете? (да/нет): ')

if updateReleased == "да":
    play()
elif updateReleased == "нет":
    update(24)