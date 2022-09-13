"""
Each week you are meeting with your friends to spend some quality time together. Usually you're hanging out in a bar on Friday nights, or going out of town on Saturdays, or playing the board games on Sundays. You want to simplify the process of gathering people and that's why you've decided to write a program which could automate this process.
You should create the class Party(place) which will send the invites to all of your friends. Also you should create the class Friend and each friend will be an instance of this class.
Sometimes the circle of friends is changing - new friends appear, the old ones disappear from your life (for example - move to another town). To form right connections you should create the Party class with the next methods:

add_friend (Friend(name)) - add friend 'name' to the list of the 'observers' (people, which will get the invitations, when the new party is scheduled).
del_friend (friend) - remove 'friend' from the 'observers' list.
send_invites() - send the invites with the right day and time to the each person on the list of 'observers'.
Class Friend should have the show_invite() method which returns the string with the last invite that the person has received with the right place, day and time. The right place - is the 'place' which is given to the Party instance in the moment of creation. If the person didn't get any invites, this method should return - "No party..."
In this mission you could use the Observer design pattern. 
"""

class Friend:
    def __init__(self, name):
        self.name = name
        self.message = 'No party...'

    def invite(self, message):
        self.message = message

    def show_invite(self):
        return self.message


class Party:
    def __init__(self, place):
        self.place = place
        self.friends = []

    def add_friend(self, friend):
        self.friends.append(friend)

    def del_friend(self, friend):
        self.friends.remove(friend)

    def send_invites(self, date):
        for friend in self.friends:
            friend.invite(f'{self.place}: {date}')
