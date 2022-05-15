#>>> callahan = Professor("Callahan") 
#>>> elle = Student("Elle", callahan)
#>>> There are now, 1, students

#>>> elle.visit_office_hours(callahan)
#>>> Thanks, callahan

#>>> elle.visit_office_hours(Professor("Paulette"))
#>>> Thank, Paulette

#>>> [name for name in callahan.students]
# [elle]

#>>> x = Student("Vivian", Professor("Stromwell")).name
# There are now, 2, students

#>>> x
#

#>>> [name for name in callahan.students]
# [elle]

class MinList:
"""A list that can only pop the smallest element """
def __init__(self):
    self.items = []
    self.size = 0
def append(self, item):
    self.items.apped(item)
    self.size += 1
def pop(self):
    smallestitem = min(self.item)
    self.items.remove(smallestiem)
    self.size -= 1
    return smallestitem
class Email:
"""Every email object has 3 instance attributes: the
message, the sender name, and the recipient name.
"""
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name
class Server:
"""Each Server has an instance attribute clients, which
is a dictionary that associates client names with
client objects.
"""
    def __init__(self):
        self.clients = {}
    def send(self, email):
        client= self.clients[email.recipient_name]
        client.receive(email)
"""Take an email and put it in the inbox of the client
it is addressed to.
"""
    def register_client(self, client, client_name):
        self.client[client_name] = client
"""Takes a client object and client_name and adds them
to the clients instance attribute.
"""
Note: This worksheet is a problem bank—most TAs will not cover all the problems in discussion section.
6 Object-Oriented Programming
class Client:
"""Every Client has instance attributes name (which is
used for addressing emails to the client), server
(which is used to send emails out to other clients), and
inbox (a list of all emails the client has received).
"""
    def __init__(self, server, name):
        self.inbox = []
        self.sever = sever
        self.name = name
        self.sever.register_client(self, self.name)
    def compose(self, msg, recipient_name):
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)
"""Send an email with the given message msg to the
given recipient client.
"""
    def receive(self, email):
        self.inbox.append(email)
"""Take an email and add it to the inbox of this
client.
"""