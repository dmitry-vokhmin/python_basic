time = int(input("Введите нужное время в секундах >>>"))

hours = time // 3600
minutes = (time - hours * 3600) // 60
second = time - (hours * 3600 + minutes * 60)
print(f"Время в формате чч:мм:сс {hours}:{minutes}:{second}")
