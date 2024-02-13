import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')

    for i in range(2):
        print(40*"*")
    
    print(r.status_code)
    print(r.text)
    print(type(r.text))

    for i in range(2):
        print(40*"*")

    categories = r.json()
    print(categories)

    for i in range(2):
        print(40*"*")

    for category in categories:
        print(category['name'])
