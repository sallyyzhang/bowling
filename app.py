import json
from db import GamePlayer, Game, Player, Frame, db
from flask import Flask
from flask import request

app = Flask(__name__)
db_filename = "cms.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

# generalized response formats


def success_response(data="", code=200):
    if data=="":
       return json.dumps({"success": True}), code
    return json.dumps({"success": True, "data": data}), code



def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code


db.init_app(app)
with app.app_context():
    db.create_all()


# your routes here
@app.route("/api/games/<int:game_id>/", methods=["GET"])
def get_games(game_id):
    game = Game.query.filter_by(id=game_id).first()
    if game is None:
        return failure_response("gameNotFound", 406)
    resp = game.rep()
    complete = True
    resp["players"] = []
    for g in GamePlayer.query.filter_by(game_id=game_id).order_by(GamePlayer.score.desc()).all():
        resp["players"].append(g.serialize())
        if g.complete() == False:
           complete = False
    resp["isComplete"] = complete
    return success_response(resp)


@app.route("/api/players/", methods=["POST"])
def create_player():
    body = json.loads(request.data)
    game_id = body.get("gameID")
    player_name = body.get("name")
    player = Player.query.filter_by(name=player_name).first()
    duplicate = GamePlayer.query.\
    filter_by(player_name=player_name, game_id=game_id).first()
    if duplicate is None:
        player = Player(name=player_name)
        db.session.add(player)
        db.session.commit()
    else:
        return failure_response("duplicatePlayer", 406)
    game_player = GamePlayer(
        game_id=game_id, player_id=player.id, player_name=player_name
    )
    db.session.add(game_player)
    db.session.commit()
    return success_response(game_player.serialize(), 201)


@app.route("/api/games/", methods=["POST"])
def create_games():
    body = json.loads(request.data)
    name = body.get("name")
    new_game = Game(name=name)
    db.session.add(new_game)
    db.session.commit()
    return success_response(new_game.serialize(), 201)


@app.route("/api/frames/", methods=["POST"])
def post_frame():
    body = json.loads(request.data)
    gameid = body.get("gameID")
    name = body.get("name")
    framename = body.get("frameName")
    first_roll = body.get("firstRoll")
    second_roll = body.get("secondRoll")
    third_roll = body.get("thirdRoll")
    score = body.get("score")
    mutable = body.get("mutable")
    game_player = GamePlayer.query.filter_by(game_id=gameid, player_name=name).first()
    if game_player is None:
        return failure_response("playerNotFound", 406)

    frames = Frame.query.filter_by(gamePlayerid=game_player.id).all()
    playerScore = 0
    for frame in frames:
        if frame.score > playerScore:
            playerScore = frame.score
    game_player.score = playerScore
    frame = Frame.query.filter_by(gamePlayerid=game_player.id, frameName=framename).first()

    if frame is None:
        frame = Frame(
            gamePlayerid=game_player.id,
            frameName=framename,
            mutable=mutable,
            score=score,
            firstRoll=Frame.parsePins(first_roll),
            secondRoll=Frame.parsePins(second_roll),
            thirdRoll=Frame.parsePins(third_roll),
        )
        db.session.add(frame)
    else:
        frame.mutable=mutable
        frame.score=score
        frame.firstRoll=Frame.parsePins(first_roll)
        frame.secondRoll=Frame.parsePins(second_roll)
        frame.thirdRoll=Frame.parsePins(third_roll)
    db.session.commit()
    return success_response(frame.serialize(), 201)

@app.route("/api/games/<int:game_id>/", methods=["DELETE"])
def delete_player(game_id):
    body = json.loads(request.data)

    name = body.get("name")
    game_player = GamePlayer.query.filter_by(game_id = game_id, player_name=name).first()
    if game_player is None:
        return failure_response("playerNotFound", 406)
    db.session.delete(game_player)
    db.session.commit()

    if GamePlayer.query.filter_by(player_name=name).first() is None:
        player = Player.query.filter_by(name=name).first()
        if player is not None:
            db.session.delete(player)
            db.session.commit()
    return success_response()


if __name__ == "__main__":
    app.run()
