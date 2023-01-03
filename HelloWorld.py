print("Hello world Soumitra!")
name = "sam"
# Learning if and else
if name == "sam":
    print("i am inside if!")
    # learning list
    all_names = ["sam", "soumitra", "samadas"]
    #Loops in python
    for names in all_names:
        print("This list of names {0}".format(names))
    print("this is my nick name with List", all_names[2])
    print("this is my nick name with List expect first", all_names[1:])
    print("this is my nick name with List expect last", all_names[:-1])

    #Learning Dictonary
    name_dict = {
        "name": "soumitra",
        "nick_name": ["samadas", "sam"]
    }
    name_dict["nick_name"].append("master")
    print("this is my nick name with dictonary", name_dict["nick_name"])
    # print keys in dict
    print("this is current keys dictonary",name_dict.keys())
    # Delete some keys from dict
    del name_dict["nick_name"]
    print("this is current keys dictonary",name_dict.keys())
    # Learning exception code
    try:
        print("this is my nick name with dictonary after deletion", name_dict["nick_name"])
    except Exception as error:
        print("Nick_name is not present", error)
else:
    print("I am not soumitra")
