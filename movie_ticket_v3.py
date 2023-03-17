"""Movie Theatre ticketing system
Get the category and number of tickets required
Created by Alan, although he has no idea how to do squat using Pycharm"""


#Componet 3 - Calculate ticket price
def get_prices(type):
    prices = [["A", 12.5]["S", 9.50]["C", 10.5]["G", 0.0]]


# Component 1 - Welcome screen and set up variables
def sell_tickets():
    print( "********** Fanfare Movies - ticketing system ***********\n")

    adult_tickets = 0
    child_ticket = 0
    student_tickets = 0
    gift_tickets = 0
    tickets_sold = 0
    total_sales = 0


    #Component 2 - Get the category and number of tickets required

    ticket_wanted = "Y"
    while ticket_wanted == "Y":
        ticket_type = input("What kind of ticket do you want: ")
                            "\t'A' for Adult, or\n"
                            "\t's' for Student, or\n"
                            "\t'C' for Child, or\n"
                            "\t'G' for Gift, or \n"
                            ">> ") .upper()
        num_tickets = int(input(f"How many {ticket_type} tickets do you want: "
                                f""))
        print(f"\nYou have ordered {num_tickets}{ticket_type} ticket(s)!")
            f"at a cost of ${cost * num_tickets:. 2f}!")

        ticket_wanted = input("Do you want to buy another ticket? (Y/N)")
                                "").upper()

    # Main routine
    sell_tickets()
