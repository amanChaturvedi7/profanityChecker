import urllib

def read_text():
    doc=open("doc.txt")
    contents= doc.read()
    print(contents)
    check_profanity(contents)
    doc.close()

def check_profanity(text_to_be_checked):
    connection=urllib.urlopen("http://www.purgomalum.com/service/xml?text=" + text_to_be_checked)
    output=connection.read()
    print(output)
    connection.close()

read_text()
raw_input("exit<Enter>")