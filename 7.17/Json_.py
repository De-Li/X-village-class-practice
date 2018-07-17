# import json

# person = {
#     "firstName": "Jane",
#     "lastName": "Doe",
#     "hobbies": ["running", "sky diving", "singing"],
#     "age": 35,
#     "children": [
#         {
#             "firstName": "Alice",
#             "age": 6
#         },
#         {
#             "firstName": "Bob",
#             "age": 8
#         }
#     ]
# }

# with open('person.json', 'w') as f:
#     json.dump(person, f)

# with open('person.json', 'r') as f:
#     qwe = json.load(f)

# print(json.dumps(qwe, indent=4))
# # import json

# # with open('person.json') as f:
# #     person = json.load(f)
# #     print(person)
# #     print(json.dumps(person, indent=4))
import json
with open('music.json','r+') as f:
    catch=json.load(f)
    print(json.dumps(catch,indent=4))
