"""Movie Theatre ticketing system
Get the category and number of tickets required
Created by Alan, although he has no idea how to do squat using Pycharm"""


# Component 4 - Confirm order
def confirm_order(ticket, number, cost):
    confirm = ""
    while confirm != "Y" and confirm != "N":
        confirm = input(f"\nYou have ordered {number} {ticket} tickets(s)"
                        f"at a cost of ${cost * number:.2f}\n"
                        f"('Y' or 'N'").upper()
        if confirm == "Y":
            return True
        else:
            return False


#Componet 3 - Calculate ticket price
def get_prices(type):
    prices = [["A", 12.5], ["S", 7], ["C", 9], ["G", 0.0]]


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
    ticket_type = input("What kind of ticket do you want: \n"
                        "\t'A' for Adult, or\n"
                        "\t'S' for Student, or\n"
                        "\t'C' for Child, or\n"
                        "\t'G' for Gift, or \n"
                        ">> ").upper()
    num_tickets = int(input(f"How many {ticket_type} tickets do you want: "
                            f""))

    cost = get_prices(ticket_type)
    if confirm_order(ticket_type, num_tickets, cost):
            print("Order confirmed")
            # Component 5 -Update totals:
            total_sales += cost
            tickets_sold = num_tickets
            if ticket_type == "A":
                adult_tickets += num_tickets
            elif ticket_type == "S":
                student_tickets += num_tickets
            elif ticket_type == "C":
                child_ticket += num_tickets
            else:
                gift_tickets +=num_tickets

    else:
        print("Order cancelled")

    ticket_wanted = input("Do you want to buy another ticket? Y/N :"
                            "").upper()



# Main routine
sell_tickets()
