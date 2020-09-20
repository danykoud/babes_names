# database = "sqlite"
database = "postgres"

connect_string = ""

if database == "sqlite":
    connect_string = "sqlite:///Babies_Names.db"
    
elif database == "postgres": 
    connect_string = "postgres://uojmftnmharlnr:2afb0b29037d9b4cbf71fe7772cb4a0f499dad2c2133f74579a1f5d7cd3726da@ec2-54-160-202-3.compute-1.amazonaws.com:5432/d1rehkgcfdf1oa"