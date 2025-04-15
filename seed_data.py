from main import db, Book, Author


def data_load():
    authors = [
        Author(author_key="/authors/OL1A", name="J.K. Rowling"),
        Author(author_key="/authors/OL2A", name="Rick Riordan"),
        Author(author_key="/authors/OL3A", name="George Orwell"),
        Author(author_key="/authors/OL4A", name="Miguel de Cervantes"),
        Author(author_key="/authors/OL5A", name="Harper Lee"),
        Author(author_key="/authors/OL6A", name="Thanhha Lai"),
        Author(author_key="/authors/OL7A", name="Pam Muñoz Ryan"),
        Author(author_key="/authors/OL8A", name="F. Scott Fitzgerald"),
        Author(author_key="/authors/OL9A", name="Stephen E. Ambrose"),
        Author(author_key="/authors/OL10A", name="Dr. Seuss"),
        Author(author_key="/authors/OL11A", name="D.J. McHale"),
        Author(author_key="/authors/OL12A", name="Scott Westerfeld"),
        Author(author_key="/authors/OL13A", name="Suzanne Collins"),
        Author(author_key="/authors/OL14A", name="Robert Louis Stevenson"),
        Author(author_key="/authors/OL15A", name="C.S. Lewis"),
        Author(author_key="/authors/OL16A", name="J.R.R. Tolkien"),
        Author(author_key="/authors/OL17A", name="Ann Brashares"),
        Author(author_key="/authors/OL18A", name="Lois Lowry"),
        Author(author_key="/authors/OL19A", name="John Green"),
        Author(author_key="/authors/OL20A", name="Jeanne DuPrau"),
        Author(author_key="/authors/OL21A", name="S.E. Hinton"),
        Author(author_key="/authors/OL22A", name="Jenny Lawson"),
    ]

    db.add_all(authors)

    books = [

        Book(title="Harry Potter and the Sorcerer's Stone", author_key="/authors/OL1A", isbn="978000001001",
             publish_date="1997", subject="Fantasy"),
        Book(title="Harry Potter and the Chamber of Secrets", author_key="/authors/OL1A", isbn="978000001002",
             publish_date="1998", subject="Fantasy"),
        Book(title="Harry Potter and the Prisoner of Azkaban", author_key="/authors/OL1A", isbn="978000001003",
             publish_date="1999", subject="Fantasy"),
        Book(title="Harry Potter and the Goblet of Fire", author_key="/authors/OL1A", isbn="978000001004",
             publish_date="2000", subject="Fantasy"),
        Book(title="Harry Potter and the Order of the Phoenix", author_key="/authors/OL1A", isbn="978000001005",
             publish_date="2003", subject="Fantasy"),
        Book(title="Harry Potter and the Half-Blood Prince", author_key="/authors/OL1A", isbn="978000001006",
             publish_date="2005", subject="Fantasy"),
        Book(title="Harry Potter and the Deathly Hallows", author_key="/authors/OL1A", isbn="978000001007",
             publish_date="2007", subject="Fantasy"),
        Book(title="The Lightning Thief", author_key="/authors/OL2A", isbn="978000001008", publish_date="2005",
             subject="Fantasy"),
        Book(title="The Sea of Monsters", author_key="/authors/OL2A", isbn="978000001009", publish_date="2006",
             subject="Fantasy"),
        Book(title="The Titan's Curse", author_key="/authors/OL2A", isbn="978000001010", publish_date="2007",
             subject="Fantasy"),
        Book(title="The Battle of the Labyrinth", author_key="/authors/OL2A", isbn="978000001011", publish_date="2008",
             subject="Fantasy"),
        Book(title="The Last Olympian", author_key="/authors/OL2A", isbn="978000001012", publish_date="2009",
             subject="Fantasy"),
        Book(title="The Lost Hero", author_key="/authors/OL2A", isbn="978000001013", publish_date="2010",
             subject="Fantasy"),
        Book(title="The Son of Neptune", author_key="/authors/OL2A", isbn="978000001014", publish_date="2011",
             subject="Fantasy"),
        Book(title="The Mark of Athena", author_key="/authors/OL2A", isbn="978000001015", publish_date="2012",
             subject="Fantasy"),
        Book(title="The House of Hades", author_key="/authors/OL2A", isbn="978000001016", publish_date="2013",
             subject="Fantasy"),
        Book(title="The Blood of Olympus", author_key="/authors/OL2A", isbn="978000001017", publish_date="2014",
             subject="Fantasy"),
        Book(title="The Red Pyramid", author_key="/authors/OL2A", isbn="978000001018", publish_date="2010",
             subject="Fantasy"),
        Book(title="The Throne of Fire", author_key="/authors/OL2A", isbn="978000001019", publish_date="2011",
             subject="Fantasy"),
        Book(title="The Serpent's Shadow", author_key="/authors/OL2A", isbn="978000001020", publish_date="2012",
             subject="Fantasy"),
        Book(title="The Sword of Summer", author_key="/authors/OL2A", isbn="978000001021", publish_date="2015",
             subject="Fantasy"),
        Book(title="The Hammer of Thor", author_key="/authors/OL2A", isbn="978000001022", publish_date="2016",
             subject="Fantasy"),
        Book(title="The Ship of the Dead", author_key="/authors/OL2A", isbn="978000001023", publish_date="2017",
             subject="Fantasy"),
        Book(title="The Hunger Games", author_key="/authors/OL13A", isbn="978000001024", publish_date="2008",
             subject="Dystopian"),
        Book(title="Catching Fire", author_key="/authors/OL13A", isbn="978000001025", publish_date="2009",
             subject="Dystopian"),
        Book(title="Mockingjay", author_key="/authors/OL13A", isbn="978000001026", publish_date="2010",
             subject="Dystopian"),
        Book(title="The Lion, the Witch and the Wardrobe", author_key="/authors/OL15A", isbn="978000001027",
             publish_date="1950", subject="Fantasy"),
        Book(title="Prince Caspian", author_key="/authors/OL15A", isbn="978000001028", publish_date="1951",
             subject="Fantasy"),
        Book(title="The Voyage of the Dawn Treader", author_key="/authors/OL15A", isbn="978000001029",
             publish_date="1952", subject="Fantasy"),
        Book(title="The Silver Chair", author_key="/authors/OL15A", isbn="978000001030", publish_date="1953",
             subject="Fantasy"),
        Book(title="The Horse and His Boy", author_key="/authors/OL15A", isbn="978000001031", publish_date="1954",
             subject="Fantasy"),
        Book(title="The Magician's Nephew", author_key="/authors/OL15A", isbn="978000001032", publish_date="1955",
             subject="Fantasy"),
        Book(title="The Last Battle", author_key="/authors/OL15A", isbn="978000001033", publish_date="1956",
             subject="Fantasy"),
        Book(title="The Fellowship of the Ring", author_key="/authors/OL16A", isbn="978000001034", publish_date="1954",
             subject="Fantasy"),
        Book(title="The Two Towers", author_key="/authors/OL16A", isbn="978000001035", publish_date="1954",
             subject="Fantasy"),
        Book(title="The Return of the King", author_key="/authors/OL16A", isbn="978000001036", publish_date="1955",
             subject="Fantasy"),
        Book(title="The Hobbit: An Unexpected Journey", author_key="/authors/OL16A", isbn="978000001037",
             publish_date="1937", subject="Fantasy"),
        Book(title="The Hobbit: There and Back Again", author_key="/authors/OL16A", isbn="978000001038",
             publish_date="1937", subject="Fantasy"),
        Book(title="The Silmarillion", author_key="/authors/OL16A", isbn="978000001039", publish_date="1977",
             subject="Fantasy"),
        Book(title="Sylo", author_key="/authors/OL11A", isbn="978000001040", publish_date="2013",
             subject="Science Fiction"),
        Book(title="Storm", author_key="/authors/OL11A", isbn="978000001041", publish_date="2014",
             subject="Science Fiction"),
        Book(title="Strike", author_key="/authors/OL11A", isbn="978000001042", publish_date="2015",
             subject="Science Fiction"),
        Book(title="Leviathan", author_key="/authors/OL12A", isbn="978000001043", publish_date="2009",
             subject="Science Fiction"),
        Book(title="Behemoth", author_key="/authors/OL12A", isbn="978000001044", publish_date="2010",
             subject="Science Fiction"),
        Book(title="Goliath", author_key="/authors/OL12A", isbn="978000001045", publish_date="2011",
             subject="Science Fiction"),
        Book(title="Fantastic Beasts and Where to Find Them", author_key="/authors/OL1A", isbn="978000001046",
             publish_date="2001", subject="Fantasy"),
        Book(title="1984", author_key="/authors/OL3A", isbn="978000001047", publish_date="1949", subject="Dystopian"),
        Book(title="Animal Farm", author_key="/authors/OL3A", isbn="978000001048", publish_date="1945",
             subject="Political Satire"),
        Book(title="Don Quixote", author_key="/authors/OL4A", isbn="978000001049", publish_date="1605",
             subject="Classic"),
        Book(title="To Kill a Mockingbird", author_key="/authors/OL5A", isbn="978000001050", publish_date="1960",
             subject="Classic"),
        Book(title="Inside Out and Back Again", author_key="/authors/OL6A", isbn="978000001051", publish_date="2011",
             subject="Historical Fiction"),
        Book(title="Esperanza Rising", author_key="/authors/OL7A", isbn="978000001052", publish_date="2000",
             subject="Historical Fiction"),
        Book(title="The Great Gatsby", author_key="/authors/OL8A", isbn="978000001053", publish_date="1925",
             subject="Classic"),
        Book(title="Band of Brothers", author_key="/authors/OL9A", isbn="978000001054", publish_date="1992",
             subject="History"),
        Book(title="The Cat in the Hat", author_key="/authors/OL10A", isbn="978000001055", publish_date="1957",
             subject="Children's"),
        Book(title="Treasure Island", author_key="/authors/OL14A", isbn="978000001056", publish_date="1883",
             subject="Adventure"),
        Book(title="Sisterhood of the Traveling Pants", author_key="/authors/OL17A", isbn="978000001057",
             publish_date="2001", subject="Young Adult"),
        Book(title="The Giver", author_key="/authors/OL18A", isbn="978000001058", publish_date="1993",
             subject="Dystopian"),
        Book(title="The Fault in Our Stars", author_key="/authors/OL19A", isbn="978000001059", publish_date="2012",
             subject="Young Adult"),
        Book(title="The City of Ember", author_key="/authors/OL20A", isbn="978000001060", publish_date="2003",
             subject="Science Fiction"),
        Book(title="The Outsiders", author_key="/authors/OL21A", isbn="978000001061", publish_date="1967",
             subject="Young Adult"),
        Book(title="Furiously Happy", author_key="/authors/OL22A", isbn="978000001062", publish_date="2015",
             subject="Memoir"),

    ]

    db.add_all(books)
    db.commit()

    print("Seeded database successfully!")
