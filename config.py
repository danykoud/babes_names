database = "sqlite"
# database = "postgres"

connect_string = ""

if database == "sqlite":
    connect_string = "sqlite:///Babies_Names.db"
    
elif database == "postgres": 
    connect_string = "postgresql+psycopg2://postgres:/babynames_db"