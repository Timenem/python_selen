"""
You are the judge at a competitive eating competition and you need to choose a winner!

There are three foods at the competition and each type of food is worth a different amount of points. Points are as follows:

    Chickenwings: 5 points

    Hamburgers: 3 points

    Hotdogs: 2 points

Write a function that helps you create a scoreboard. It takes as a parameter a list of objects representing the participants, for example:

[
  {name: "Habanero Hillary", chickenwings: 5 , hamburgers: 17, hotdogs: 11},
  {name: "Big Bob" , chickenwings: 20, hamburgers: 4, hotdogs: 11}
]

It should return "name" and "score" properties sorted by score; if scores are equals, sort alphabetically by name.

[
  {name: "Big Bob", score: 134},
  {name: "Habanero Hillary", score: 98}
]

"""
def scoreboard(w):
    m = []
    for i in w:
        d = {'name':i['name'],'score':0}
        for k in i:
            if k in 'chickenwingshamburgershotdogs':
                d['score'] += (5*i['chickenwings'] if 'chickenwings' in k else 3*i['hamburgers'] if 'hamburgers' in k else 2*i['hotdogs'])
        m.append(d)
    return sorted(m, key = lambda x: (-x['score'], x['name']))
