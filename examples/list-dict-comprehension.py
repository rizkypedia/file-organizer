def check_temp(value):
    if value >=70:
        return "HOT"
    elif 69 >= value >=40:
        return "Warm"
    else:
        return "Cold"
        

#List comprehension
# {expression for expression in iterable}
# {expression for expression in iterable if conditional}
# {(if/else) for expression in iterable}
print('List comprehension')

x = [100,90,80,70,60,50,40,30,20,10]

y = [i if i>=60 else 'FAILED' for i in x  ]

z = [i for i in x if i>=60]
print(y)
print(z)

#Dictionary comprehension
# {key: expression for (key. value) in iterable}
# {key: expression for (key. value) in iterable if conditional}
# {key: (if/else) for (key. value) in iterable}
# {key: function(value) for (key. value) in iterable}

cities_in_F = {'New York': 32 , 'Boston': 75, 'Los Angeles' : 100, 'Chicago':50}

cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in  cities_in_F.items()}

print(cities_in_C)
weather = {'New York': "snowing", 'Boston':"sunny", 'Los Angeles':"sunny", 'Chicago':"cloudy"}

sunny_weather = {key: value for (key, value) in weather.items() if value =="sunny"}

print(sunny_weather)

desc_cities = {key: ("Warm" if value >=40 else "Cold" )for (key, value) in cities_in_F.items()}

print(desc_cities)

desc_cities_f = {key: check_temp(value) for (key, value) in cities_in_F.items()}

print(desc_cities_f)