class User:
    users = []
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__access_level = 'user'
    
    def __repr__(self):
        return f'id: {self.__id}, name: {self.__name}, access level: {self.__access_level}'
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)
        self._User__access_level = 'admin'
        User.users.append(self)

    def add_user(self, id, name, is_admin=False):
        if is_admin:
            Admin(id, name)
            print(f'Admin {self.get_name()} added admin {name} with id {id}\n')
        else:
            User.users.append(User(id, name))
            print(f'Admin {self.get_name()} added user {name} with id {id}\n')

    def remove_user(self, id):
        for user in User.users:
            if user.get_id() == id:
                User.users.remove(user)
                print(f'Admin {self.get_name()} removed user {user.get_name()} with id {id}\n')
                return
        print(f'Admin {self.get_name()} could not find user with id {id}\n')

    def get_users(self):
        print(f'Admin {self.get_name()} looks at users:')
        for i, user in enumerate(User.users, 1):
            print(f'{i}. {user}')
        print()

    def get_user_by_id(self, id):
        for user in User.users:
            if user.get_id() == id:
                return user
        return None

admin_1 = Admin(1, 'John')
print(admin_1)
admin_1.get_users()
admin_1.add_user(2, 'Jane')
admin_1.get_users()
user_Bob = User(3, 'Bob')
admin_1.add_user(4, 'Mark', True)
admin_2 = admin_1.get_user_by_id(4)
admin_2.get_users()
admin_2.add_user(3, 'Bob')
admin_2.remove_user(2)
admin_1.get_users()
admin_1.get_user_by_id(3).set_name('Robert')
admin_2.get_users()



