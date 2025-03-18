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