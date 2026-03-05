# This lab builds a many-to-many relationship
# between Author and Book using Contract as the join model


# ============================
# BOOK CLASS
# ============================

class Book:

    # store all book instances
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        # return all contracts connected to this book
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        # return all authors connected to this book
        return list(set([contract.author for contract in self.contracts()]))


# ============================
# AUTHOR CLASS
# ============================

class Author:

    # store all authors
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        # return all contracts connected to this author
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        # return all books connected to this author
        return list(set([contract.book for contract in self.contracts()]))

    def sign_contract(self, book, date, royalties):
        # create and return a new contract
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        # return total royalties from all contracts
        return sum(contract.royalties for contract in self.contracts())


# ============================
# CONTRACT CLASS
# ============================

class Contract:

    # store all contracts
    all = []

    def __init__(self, author, book, date, royalties):

        # validation checks
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")

        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")

        if not isinstance(date, str):
            raise Exception("date must be a string")

        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        # return all contracts that match the given date
        return [contract for contract in cls.all if contract.date == date]