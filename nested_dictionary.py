ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

#Write a python expression that obtains the email address of Ramit
print (ramit["email"])

#Write a python expression that get the first interests of Ramit
print (ramit["interests"][0])

#Write a python expression that gets the email address of Jasmine
for x in ramit["friends"]:
    if x["email"]  == "jasmine@yahoo.com":
        print(x["email"])

#Write a python expression that gets the second of Jan's two interests
for x in ramit["friends"]:
    if x["name"] == "Jan":
        print(x["interests"][1])