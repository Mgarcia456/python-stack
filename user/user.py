class User:
  def __init__(self, first_name, last_name, email, age ):
    self.first_name = first_name
    self.last_name = last_name
    self.email = email
    self.age = age
    self.is_rewards_member = False
    self.gold_card_points = 0
  def display_info(self):
    return f"{self.first_name} {self.last_name} {self.email} {self.age}"

  def enroll(self):
    self.is_rewards_member = True
    self.gold_card_points = 200
    print (f"{self.first_name} {self.last_name} is now a rewards member {self.is_rewards_member} and now has {self.gold_card_points} points")
    return self.is_rewards_member


  def points(self):
    self.gold_card_points = + 80
    print (f"{self.first_name} {self.last_name} has now earned {self.gold_card_points} points for a new total of 280 points!")
    return self.gold_card_points

  def spend_points(self):
    self.gold_card_points -= 50
    print (f"{self.first_name} {self.last_name} spent 50 points new total {self.gold_card_points} points!")
    return self.gold_card_points

user1 = User ("miguel", "garcia", "coolguy46@icloud.com", "45 years old" )
user2 = User ("john", "garcia", "badguy46@icloud.com", "32 years old" )
print(user2.enroll())
print(user2.spend_points())
print(user1.enroll())
print(user1.points())
user1.enroll().points(80).display_info()
user2.enroll().spend_points(50).display_info()