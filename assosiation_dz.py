class Player:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def show_players(self):
        print('Players in team:')
        for player in self.players:
             print(player.name)

player1 = Player("Alice")
player2 = Player("Bob")

team = Team()
team.add_player(player1)
team.add_player(player2)
team.show_players()



class Employee:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = [ ]

    def add_employee(self, employee):
        self.employees.append(employee)

    def show_employees(self):
        print(f"Employees in {self.company_name}:")
        for employee in self.employees:
            print(employee.name)

employee = Employee("John")

company_a = Company("Company A")
company_b = Company("Company B")

company_a.add_employee(employee)
company_b.add_employee(employee)

company_a.show_employees()
company_b.show_employees()



class Room:
    def __init__(self, name):
        self.name = name

class House:
    def __init__(self):
        self.rooms = [
            Room("Living Room"),
            Room("Bedroom")
        ]

    def number_of_rooms(self):
        print(f"Number of rooms: {len(self.rooms)}")

house = House()
house.number_of_rooms()



class Page:
    def __init__(self, number):
        self.number = number

class Book:
    def __init__(self, num_pages):
        self.pages = [Page(i) for i in range(1, num_pages+1)]

    def count_pages(self):
        print("Pages in book:", len(self.pages))

book = Book(3)
book.count_pages()



class CPU:
    def __init__(self, model):
        self.model = model

class RAM:
    def __init__(self, size):
        self.size = size

class Computer:
    def __init__(self):
        self.cpu = CPU("Intel i7")
        self.ram = RAM("16GB")

    def show_specs(self):
        print('Computer has:')
        print('CPU:', self.cpu.model)
        print('RAM:', self.ram.size)

computer = Computer()
computer.show_specs()



class Song:
    def __init__(self, title):
        self.title = title

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

song = Song("Shape of You")
playlist = Playlist()
playlist.add_song(song)

del playlist

print('Song still exists:', song is not None)



class Paragraph:
    def __init__(self, text):
        self.text = text

class Document:
    def __init__(self):
        self.paragraphs = [
            Paragraph("Intro"),
            Paragraph("Body"),
            Paragraph("Conclusion")
        ]

    def delete(self):
        self.paragraphs.clear()

document = Document()
document.delete()

print("Paragraphs after document deletion:", len(document.paragraphs))