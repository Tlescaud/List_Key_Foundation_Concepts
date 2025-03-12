# 3-1 exercise

names = ['terry davis','fred jones','jerry','thomas lescaud']
print(names[0])
print(names[1])
print(names[2])
print(names[-1])

# 3-2 excercise print message to names with f-string

message = f'I love tom and {names[2].title()}.'
print(message)

message = f'I know a guy named {names[0].title()}.'
print (message)

message = f'I knew it was {names[1].title()}.'
print(message)

message = f'Wow look at {names[-1].title()} go, that is so awesome.'
print(message)

# 3-3 exercise "Your own list"

favorite_vehicle = [ 'toyota', 'benz','hyundai','dodge']
print(favorite_vehicle[0].title())
print(favorite_vehicle[1])
print(favorite_vehicle[2])
print(favorite_vehicle[-1])


message = f'I love me some vehicles especially a {favorite_vehicle[-1]} charger hemi v8'
print(message)
