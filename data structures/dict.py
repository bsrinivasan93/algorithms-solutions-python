dict = {'nyc':'ny','sf':'ca'}
print(dict)
dict['atl']='ga'
print(dict)
for city,state in dict.items():
    print(f"City {city} State {state}")
for city in dict.keys():
    print(f"City {city}")
for state in dict.values():
    print(f"state {state}")
    