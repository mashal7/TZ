jaguar = {'model': 'XE', 'color': 'blue', 'year': 2020}
bmw = {'model': 'x5', 'color': 'white', 'year': 2015}
cars = [jaguar, bmw]
print(sorted(cars, key=lambda x: x['year']))