class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print ("Insufficient points to spend this amount.")
            return False
        else:
            self.gold_card_points -= amount

user1 = User("LeBron", "James", "ljames@email.com", 37)

user1.display_info()

user1.enroll()

user2 = User("Stephen", "Curry", "scurry@email.com", 34)

user3 = User("Giannis", "Antetokounmpo", "gantetokounmpo@email.com", 27)

user1.spend_points(50)

user2.enroll()

user2.spend_points(80)

user1.display_info()

user2.display_info()

user3.display_info()

user1.enroll()

user3.spend_points(40)