
class Book:

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        print(f"{self.title} {self.author} {self.pages}")


b1 = Book("Iz", "Abdurehim Otkur", 210)
b2 = Book("Oyghanghan Zemin", "Tomur Davamet", 155)

print(b1)
print(b2)
