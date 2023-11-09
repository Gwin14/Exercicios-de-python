class Titanic:
    passengerId = None
    survived = None
    pClass = None
    name = None
    sex = None
    age = None
    sibSp = None
    parch = None
    ticket = None
    fare = None
    cabin = None
    embarked = None

    def __init__(
        self,
        passengerId,
        survived,
        pClass,
        name,
        sex,
        age,
        sibSp,
        parch,
        ticket,
        fare,
        cabin,
        embarked,
    ):
        self.passengerId = passengerId
        self.survived = survived
        self.pClass = pClass
        self.name = name
        self.sex = sex
        self.age = age
        self.sibSp = sibSp
        self.parch = parch
        self.ticket = ticket
        self.fare = fare
        self.cabin = cabin
        self.embarked = embarked
