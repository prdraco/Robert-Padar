const team = {
  _players: [ {
    firstName: 'Pablo',
    lastName: 'Sanchez',
    age: 21
  }, {
    firstName: 'Roger',
    lastName: 'Lopez',
    age: 23
  }, {
    firstName: 'Samuel',
    lastName: 'Jackson',
    age: 26
  } ],
  _games: [ {
    opponent: 'Broncos',
    teamPoints: 42,
    opponentPoints: 27
    }, {
    opponent: 'Acruze',
    teamPoints: 33,
    opponentPoints: 20
    }, {
    opponent: 'Torinos',
    teamPoints: 40,
    opponentPoints: 38
    }
  ],
  get games() {
    return this._games;
  },
  get players() {
    return this._players;
  },
  addPlayer(firstName, lastName, age) {
    let player = {
      firstName: firstName,
      lastName: lastName,
      age: age
    };
    this.players.push(player);
  },

  addGame (opponent, teamPoints, opponentPoints) {
    const game = {
      opponent: opponent,
      teamPoints: teamPoints,
      opponentPoints: opponentPoints
    }
  this.games.push(game);
  }
};

team.addPlayer('Steph' , 'Curry' , '28');
team.addPlayer('Lisa' , 'Leslie' , '44');
team.addPlayer('Bugs' , 'Bunny' , '76');

console.log(team._players);

team.addGame('Titans' , 100 , 97);
team.addGame('Kondor' , 79 , 88);
team.addGame('Rovoruse' , 80 , 97);

console.log(team._games);