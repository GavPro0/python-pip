import requests

def get_categories():
  r = requests.get('https://api.escuelajs.co/api/v1/categories')
  print(r.status_code)
  print(r.text)
  print(type(r.text))
  get_categories = r.json()

  for category in get_categories:
    print(category['name'])


