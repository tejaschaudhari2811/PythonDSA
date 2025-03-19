# Practise single responsibility principle
class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def write(self, text):
        self.count +=1
        self.entries.append(f"{self.count} : {text}")

    def __str__(self):
        return "\n".join(self.entries)
    
class PersistenceManager:
    @staticmethod
    def save_file(journal, file):
        with open(file, "w") as f:
            f.write(str(journal))

j = Journal()
j.write("I cried today")
j.write("I felt like a loser")
file =r"C:\Users\Administrator\Desktop\PythonDSA\temp.txt"
PersistenceManager.save_file(j, file)

with open(file, "r") as f:
    print(f.read())



class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)
    
    def read(self, encoding = "utf-8"):
        return self.path.read_text(encoding)
    
    def write(self,data, encoding = "utf-8"):
        return self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip", mode="w")) as f:
            f.write(self.path)

    
"""
The class above violates the Single Responsibility principle from the concept of 
separation of concerns. Let us see how it should be written
"""

class FileManager:
    pass

class ZipFileManager:
    pass


