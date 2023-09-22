class Ticket:
    counter = 2000
    tickets = []

    def __init__(self, staff_id, creator_name, contact_email, description):
        self.ticket_number = Ticket.counter
        Ticket.counter += 1
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"

    def resolve_password_change_request(self):
        if "Password Change" in self.description or "Change Password" in self.description:
            new_password = self.staff_id[:2] + self.creator_name[:3]
            self.response = f"Password has been changed to {new_password}."
            self.status = "Closed"

    @classmethod
    def ticket_stats(cls):
        num_tickets = len(cls.tickets)
        num_resolved_tickets = sum(1 for ticket in cls.tickets if ticket.status == "Closed")
        num_open_tickets = num_tickets - num_resolved_tickets
        return num_tickets, num_resolved_tickets, num_open_tickets

    @classmethod
    def print_all_tickets(cls):
        for ticket in cls.tickets:
            cls.print_ticket(ticket)

    @classmethod
    def print_ticket(cls, ticket):
        print("\nTicket Number:", ticket.ticket_number)
        print("Name of Creator:", ticket.creator_name)
        print("Staff ID:", ticket.staff_id)
        print("Email Address:", ticket.contact_email)
        print("Description:", ticket.description)
        print("Response:", ticket.response)
        print("Status:", ticket.status)
