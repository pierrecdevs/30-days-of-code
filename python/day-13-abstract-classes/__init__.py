from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(self): pass

#Write MyBook class
class MyBook(Book):
    
    def __init__(self, title: str, author: str, price: int):
        super().__init__(title=title, author=author)
        self.price = price

    def display(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nPrice: {self.price}\n")
        
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
