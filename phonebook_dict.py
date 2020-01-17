phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

#print Elizabeth's phone number
print("Elizabeth: " + "%s" % (phonebook_dict['Elizabeth']))

#add an entry into the current dictionary - Kareem: 938-489-1234
phonebook_dict ["Kareem"] = "938-489-1234"

#delete Alice's phone entry
del phonebook_dict ["Alice"]

#change(add) Bob's phone number to 968-345-2345
phonebook_dict["Bob"] = "968-345-2345"

#print all the phone entries in dictionary
print(phonebook_dict)