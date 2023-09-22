from ticket import Ticket

def create_ticket():
    Creator = input("What is your Name?: ")
    Staff = input("What is your ID?: ")
    Email = input("What is your Email Address?: ")
    Problem = input("What is your Problem?: ")

    # Create a new ticket
    ticket = Ticket(Staff, Creator, Email, Problem)
    Ticket.tickets.append(ticket)
    print("Ticket created successfully!")

def edit_ticket():
    ticket_number = int(input("Enter the ticket number you want to edit: "))
    for ticket in Ticket.tickets:
        if ticket.ticket_number == ticket_number:
            print("Current Ticket Information:")
            Ticket.print_ticket(ticket)
            # You can add code here to edit ticket fields if needed
            break
    else:
        print("Ticket not found.")

def delete_ticket():
    ticket_number = int(input("Enter the ticket number you want to delete: "))
    for ticket in Ticket.tickets:
        if ticket.ticket_number == ticket_number:
            Ticket.tickets.remove(ticket)
            print("Ticket deleted successfully!")
            break
    else:
        print("Ticket not found.")

def create_multiple_tickets():
    n = int(input("How many tickets do you want to create: "))
    for _ in range(n):
        create_ticket()

def print_tickets():
    for ticket in Ticket.tickets:
        print("\nPrinting Ticket:")
        Ticket.print_ticket(ticket)

def main():
    while True:
        print("\nChoose an option:")
        print("1. Make a ticket")
        print("2. Create a ticket")
        print("3. Edit a ticket")
        print("4. Delete a ticket")
        print("5. Print all tickets")
        print("6. Print ticket statistics")
        print("7. Exit")
        choice = input("Enter the option number: ")

        if choice == "1":
            make = input("Do you want to make a ticket? (yes/no): ").lower()
            if make == "yes":
                create_ticket()
            elif make == "no":
                continue
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        elif choice == "2":
            create_multiple_tickets()

        elif choice == "3":
            edit_ticket()

        elif choice == "4":
            delete_ticket()

        elif choice == "5":
            print_tickets()

        elif choice == "6":
            # Display ticket statistics
            num_tickets, num_resolved_tickets, num_open_tickets = Ticket.ticket_stats()
            print("\nTicket Statistics:")
            print("Total Tickets:", num_tickets)
            print("Resolved Tickets:", num_resolved_tickets)
            print("Open Tickets:", num_open_tickets)

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please select a valid option (1-7).")

if __name__ == "__main__":
    main()