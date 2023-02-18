import json

state_capitals = {
    'Andhra Pradesh': 'Hyderabad',
    'Gujarat': 'Gandhinagar',
    'Karnataka': 'Bengaluru',
    'Maharashtra': 'Mumbai',
    'Punjab': 'Chandigarh',
    'Tamil Nadu': 'Chennai',
    'West Bengal': 'Kolkata'
}


with open('D:\\vaishali\\python\\assignments\\assignment_6\\state_and_capital.json', 'w') as file:
    json.dump(state_capitals, file)
