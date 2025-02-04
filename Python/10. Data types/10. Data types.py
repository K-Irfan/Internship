x=['Int','Float','Range','Complex','Str','List','Tuple','Set','Frozen set','Dict','Bool','Byte','Byte array','Memory view','None']
def datatypes():
    for i,no in enumerate(x, start=1):
        print(f"{i}. {no}")
print(f"Number of datatypes in Python are: {len(x)}")
datatypes()