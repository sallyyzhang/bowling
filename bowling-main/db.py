from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# your classes here


class Game(db.Model):
    __tablename__ = "game"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

    def serialize(self):
        return {"gameID": self.id, "name": self.name,"isComplete":False,"players":[]}
    def rep(self):
        return {"gameID":self.id,"name":self.name}

class Frame(db.Model):
    __tablename__ = "frame"
    id = db.Column(db.Integer, primary_key=True)
    frameName = db.Column(db.String, default="frame", nullable=False)
    firstRoll = db.Column(db.String, default="[-1]", nullable=False)
    secondRoll = db.Column(db.String, default="[-1]", nullable=False)
    thirdRoll = db.Column(db.String, default="[-1]", nullable=False)
    mutable = db.Column(db.Boolean, default=False, nullable=False)
    gamePlayerid = db.Column(
        db.Integer, db.ForeignKey("game_player.id"), nullable=False
    )
    score = db.Column(db.Integer, default=0, nullable=False)

    @staticmethod
    def parsePins(pins_lst):
        if pins_lst == [-1]:
            return "-1"
        pins_string = ""
        for pins in pins_lst:
            pins_string += str(pins)
        return pins_string

    @staticmethod
    def getPins(pins_str):
        if pins_str == "-1":
            return [-1]
        pins_lst = []
        if "10" in pins_str:
            pins_lst.append(10)
            index = pins_str.find("10")
            pins_str = pins_str[:index] + pins_str[index+2:]
        for pins in pins_str:
            pins_lst.append(int(pins))
        return pins_lst

    def serialize(self):
        resp = {
            "firstRoll": Frame.getPins(self.firstRoll),
            "secondRoll": Frame.getPins(self.secondRoll),
            "thirdRoll": Frame.getPins(self.thirdRoll),
            "mutable": self.mutable,
            "score": self.score,
        }
        return resp


class Player(db.Model):
    __tablename__ = "player"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    games = db.relationship("GamePlayer")

    def serialize(self):
        return {"name": self.name}

    def rep(self):
        resp = {"name": self.name}
        resp["games"] = [g.serialize() for g in self.games]
        return resp


class GamePlayer(db.Model):
    __tablename__ = "game_player"
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("game.id"), nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey("player.id"), nullable=False)
    player_name = db.Column(db.String, nullable=False)
    isComplete = db.Column(db.Boolean, default=False, nullable=False)
    score = db.Column(db.Integer, default=0)
    frames = db.relationship("Frame", cascade="delete")

    def complete(self):
        if len(self.frames)!=10:
           return False
        for f in self.frames:
           if f.mutable:
            return False
        return True

    def serialize(self):
        resp = { "name": self.player_name, "score": self.score}
        for f in self.frames:
            resp[f.frameName] = f.serialize()
        for f in range(len(self.frames)+1,11):
            resp["frame"+str(f)] = {
                    "firstRoll": [-1],
                    "secondRoll": [-1],
                    "thirdRoll": [-1],
                    "score": -1,
                    "mutable": True,
                }
        return resp
