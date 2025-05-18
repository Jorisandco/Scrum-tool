class People:
    def __init__(self, name :str, role :str, is_me :bool):
        self.name = name
        self.role = role
        self.is_me = is_me

    def get_name(self):
        return self.name
    
    def get_role(self):
        return self.role

    def get_all_info(self):
        return f"Name: {self.name}, Role: {self.role}, Is Me: {self.is_me}"