class Users:

    def __init__(self, db):
        self.db = db

    def list(self):
        for user_data in self.db:
            print(f"{user_data[0]} | {user_data[1]} | {user_data[2]} | {user_data[3]}")
        print() # Empty row

    def get_next_id(self):
        max_id = 0
        for r in self.db:
            id_value = int(r[0])
            if max_id < id_value:
                max_id = id_value
        return str(max_id + 1)

    def add(self, rec):
        rec[0] = str(self.get_next_id())
        self.db.append(rec)

    def find(self, id_value):
        key = 0
        for r in self.db:
            if r[0] == id_value:
                break
            key += 1
        return key

    def update(self, rec):
        id_value = rec[0]
        key = self.find(id_value)
        self.db[key] = rec

    def remove(self, id_value):
        key = self.find(id_value)
        del self.db[key]

    def search_by_name(self, name):
        for rec in self.db:
            if rec[1] == name:
                return rec

user_db = [
    ['1', 'Ivan', 'email@domain.com', '0822334455'],
    ['2', 'Peter', 'peter@email.com', '0812345678']
]
users = Users(user_db)

users.add(['', 'Vasil', 'vasil@mail.com', '0891123456'])
users.list()

users.update(['3', 'Vasil', 'vasil_new@mail.com', '087321456'])
users.list()

users.remove('3') # by id
users.list()

row = users.search_by_name('Ivan')
print(row)
