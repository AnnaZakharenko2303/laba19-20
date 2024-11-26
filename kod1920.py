import random
import math
from functools import reduce

def generate_random_points(n):
    """Генерация случайных точек."""
    return [(random.uniform(-10, 10), random.uniform(-10, 10)) for _ in range(n)]

def input_points():
    """Ввод точек вручную."""
    points = input("Введите точки в формате (x1, y1), (x2, y2), ... : ")
    points = points.strip().split('), (')
    points = [tuple(map(float, point.strip('()').split(','))) for point in points]
    return points

def distance(point1, point2):
    """Вычисление расстояния между двумя точками."""
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def find_nearest_point(point, points):
    """Находит ближайшую точку для заданной точки."""
    return min(points, key=lambda other_point: distance(point, other_point))

def add_nearest_points(points):
    """Возвращает массив точек с добавленной ближайшей точкой."""
    return [(point, find_nearest_point(point, points)) for point in points]

def main_menu():
    """Главное меню приложения."""
    while True:
        print("\nМеню:")
        print("1) Генерация случайных точек")
        print("2) Ввод точек вручную")
        print("3) Найти ближайшие точки")
        print("0) Завершение работы")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            num_points = int(input("Введите количество случайных точек: "))
            points = generate_random_points(num_points)
            print(f"Сгенерированные точки: {points}")
        
        elif choice == '2':
            points = input_points()
            print(f"Введенные точки: {points}")
        
        elif choice == '3':
            if 'points' not in locals():
                print("Ошибка: Необходимо сначала ввести или сгенерировать точки.")
                continue
            
            results = add_nearest_points(points)
            for point, nearest in results:
                print(f"Точка {point} ближайшая точка {nearest}")
        
        elif choice == '0':
            print("Завершение работы программы.")
            break
        
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()
