class BookStore:
    NoOfBooks = 0
    
    def __init__(self, name, author):
        self.Name = name
        self.Author = author
        self.NoOfBooks = self.NoOfBooks+1
        
    def Display(self):
        print(self.Name, "by ", self.Author, ", No. of books: ", self.NoOfBooks)
        
def main():
    Obj1 = BookStore("Linux Systm Programming", "Robert Love")
    Obj1.Display()
    
    Obj2 = BookStore("C Programming", "Dennis Richie")
    Obj2.Display()

if __name__=="__main__":
    main()