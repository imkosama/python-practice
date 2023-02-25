questions = [
    ["Which language was used to create fb?",
     "pyhton", "PHP", "Javascript", "Java", "None", 2],  # index value is our correct answer
    ["what is harry porter fullname?",
     "james", "lily", "molfey", "snape", "None", 1],
    ["How many bananas in 1 dozen?",
     "6", "10", "12", "15", "None", 3],
    ["who is the prime minister of india? ",
     "Rahul", "Soniya", "Nehru", "Modi", "None", 4],
    ["which is the favourite food in Maharashtra?",
     "Bhajiya pav", "Samosa Pav", "Missal pav", "Vada pav", "None", 4],
    ["which is the national fruit of India?",
     "Apple", "Mango", "Cherry", "banana", "None", 3],
    ["Which is the Capital of Maharashtra?",
     "osmanabad", "Mumbai", "Pune", "Nashik", "None", 3]
]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(question[0])
    print(f'\nQuestion for Rs.{levels[i]}')
    print(f"a.{question[1]}      b.{question[2]}")
    print(f"c.{question[3]}      d.{question[4]}")
    reply = int(input("enter your answer (1-4) or 0 to quit :\n "))
    if reply == 0:
        money = levels[i-1]
    if (reply == question[-1]):
        print(f'Correct answer .you have won Rs.{levels[i]}')
        if i == 4:
            money = 1000
        elif i == 9:
            money = 320000
        elif i == 14:
            money = 10000000

    else:
        print("wrong answer")
        break

print(f"your take home money is {money}")
