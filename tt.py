import json

data = '''[{
  "userName": "denise45",
  "email": "erichard@example.com",
  "password": "yk7BRA*3W*"
},
{
  "userName": "ronaldrogers",
  "email": "david94@example.org",
  "password": "1%98fCjxrt"
},
{
  "userName": "matthew25",
  "email": "carlsonana@example.net",
  "password": "#e&4MF@rC2"
},
{
  "userName": "james79",
  "email": "william75@example.net",
  "password": "_vr9HnQYor"
},
{
  "userName": "tina19",
  "email": "nicholassparks@example.net",
  "password": "3S4WszAm8^"
}]'''

data_j = json.loads(data)
print (data_j[1])