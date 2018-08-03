//Character dict
var characterDict = {};
var you;

//Character classes
class Character{
    constructor(sessionId, x_position, y_position, hp){
        //{x:0,y:0}
        console.log("in character() constructor");
        this.x_position = x_position;
        this.y_position = y_position;
        this.sessionId = sessionId;
        this.hp = hp
        characterDict[this.sessionId] = this;
        console.log("out character() constructor");
        console.log(Object.keys(characterDict).length);
    }
}

function createCharacter(sessionId, x_position, y_position, hp){
    new Character(sessionId, x_position, y_position, hp);

    for (var key in characterDict) {
        console.log(characterDict[key].sessionId + ", " + characterDict[key].x_position + ", " + characterDict[key].y_position)
    }
};
