katz_deli = []

def line():
    if not katz_deli:
        print('the line is currently empty')
    else:
        # was uncertain of how to initiate a count in a string inside a conditional
        #the enumerate() solution implemented below is a product of stack overflow, chatgpt and w3schools
        line_info = "The line is currently:"
        for position, customer in enumerate(katz_deli, start=1):
            line_info += f"\n{position}. {customer}"
        return line_info
    

def take_a_number(katz_deli,name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Hello {name}, you are in position {position} in the queue")

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        serving_name = katz_deli.pop(0)
        print(f"Now serving {serving_name}.")

        # Print remaining customers in line
        position = 1
        while position <= len(katz_deli):
            customer = katz_deli[position - 1]
            print(f"{position}. {customer}")
            position += 1