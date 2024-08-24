import sqlite3

'''
This is the third part of the Football project, during which additional tables and queries will be incorporated
to enhance the project's football-related features.

Additional tables
-----------------
* Country
* Players
* League
* Players position
* seasons
* Statistics

Additional SQL Queries
----------------------
* Search by League
* Search by Country
* Statistic for Player, Team and Matches

Python Tool:
* more Functions

'''

# SQL Statements
# Table creation
CREATE_COUNTRY_TABLE = """ CREATE TABLE IF NOT EXISTS country (
                            countryID INTEGER PRIMARY KEY NOT NULL,
                            countryName TEXT NOT NULL
);"""

CREATE_LEAGUE_TABLE = """ CREATE TABLE IF NOT EXISTS leagues (
                            leagueID INTEGER PRIMARY KEY NOT NULL,
                            leagueName TEXT NOT NULL,
                            countryID INTEGER NOT NULL,
                            CONSTRAINT FK_leagues_country FOREIGN KEY (countryID) REFERENCES country (countryID)
);"""

CREATE_TEAM_TABLE = """ CREATE TABLE IF NOT EXISTS teams (
                            teamID INTEGER PRIMARY KEY NOT NULL,
                            teamName TEXT NOT NULL,
                            countryID INTEGER NOT NULL,
                            CONSTRAINT FK_teams_country FOREIGN KEY (countryID) REFERENCES country (countryID)
);"""

# CREATE_POSITION_TABLE = """ CREATE TABLE IF NOT EXISTS positions (
#                                 posID INTEGER PRIMARY KEY NOT NULL,
#                                 posName TEXT NOT NULL
# ); """

# CREATE_PLAYER_TABLE = """ CREATE TABLE IF NOT EXISTS players (
#                             playerID INTEGER PRIMARY KEY NOT NULL,
#                             playerName TEXT NOT NULL,
#                             dob DATE NOT NULL,
#                             height_cm INTEGER NOT NULL,
#                             posID INTEGER NOT NULL,
#                             teamID INTEGER NOT NULL,
#                             countryID INTEGER NOT NULL,
#                             CONSTRAINT FK_players_positions FOREIGN KEY (posID) REFERENCES positions (posID)
#                             CONSTRAINT FK_players_teams FOREIGN KEY (teamID) REFERENCES teams (teamID)
#                             CONSTRAINT FK_players_country FOREIGN KEY (countryID) REFERENCES country (countryID)
# ); """



# CREATE_SEASON_TABLE = """ CREATE TABLE IF NOT EXISTS seasons (
#                             seasonID INTEGER PRIMARY KEY NOT NULL,
#                             seasonName TEXT NOT NULL,
#                             teamID INTEGER NOT NULL,
#                             leagueID INTEGER NOT NULL,
#                             matchesPlayed INTEGER DEFAULT 0,
#                             wins INTEGER DEFAULT 0,
#                             draws INTEGER DEFAULT 0,
#                             losses INTEGER DEFAULT 0,
#                             goalsScored INTEGER DEFAULT 0,
#                             goalsConceded INTEGER DEFAULT 0,
#                             points INTEGER DEFAULT 0,
#                             CONSTRAINT FK_seasons_teams FOREIGN KEY (teamID) REFERENCES teams (teamID),
#                             CONSTRAINT FK_seasons_leagues FOREIGN KEY (leagueID) REFERENCES leagues (leagueID)
# );"""

# CREATE_MATCHES_TABLE = """ CREATE TABLE IF NOT EXISTS matches (
#                             matchID INTEGER PRIMARY KEY NOT NULL,
#                             seasonID INTEGER NOT NULL,
#                             date DATE NOT NULL,
#                             homeTeamID INTEGER NOT NULL,
#                             awayTeamID INTEGER NOT NULL,
#                             homeScore INTEGER NOT NULL,
#                             awayScore INTEGER NOT NULL,
#                             CONSTRAINT FK_matches_home_team FOREIGN KEY (homeTeamID) REFERENCES teams (teamID),
#                             CONSTRAINT FK_matches_away_team FOREIGN KEY (awayTeamID) REFERENCES teams (teamID),
#                             CONSTRAINT FK_matches_seasons FOREIGN KEY (seasonID) REFERENCES seasons (seasonID)
# );"""

# CREATE_PLAYER_MATCH_STATS_TABLE = """ CREATE TABLE IF NOT EXISTS pms (
#                                         matchID INTEGER PRIMARY KEY NOT NULL,
#                                         playerID INTEGER NOT NULL,
#                                         posID INTEGER NOT NULL,
#                                         minutes INTEGER NOT NULL,
#                                         shot INTEGER NOT NULL,
#                                         shotOn INTEGER NOT NULL,
#                                         keyPasses INTEGER NOT NULL,
#                                         passes INTEGER NOT NULL,
#                                         crosses INTEGER NOT NULL,
#                                         tackles INTEGER NOT NULL,
#                                         intercep INTEGER NOT NULL, 
#                                         foulconceded INTEGER NOT NULL,
#                                         foulWon INTEGER NOT NULL,
#                                         offside INTEGER NOT NULL,
#                                         cleared INTEGER NOT NULL,
#                                         goals INTEGER NOT NULL,
#                                         assists INTEGER NOT NULL,
#                                         goalConceded INTEGER NOT NULL,
#                                         owng INTEGER NOT NULL,
#                                         yellowCard INTEGER NOT NULL,
#                                         redCard INTEGER NOT NULL,
#                                         motm INTEGER NOT NULL,
#                                         rating INTEGER NOT NULL
# ); """

# CREATE_PLAYER_STAT = """ CREATE TABLE IF NOT EXISTS playerstats (
#                             playerID
#                             seasonID
#                             teamID
#                             apps 
#                             minutes 
#                             totalShot 
#                             shotPerGame 
#                             keyPasses 
#                             totalPasses 
#                             totalPC 
#                             accPasses 
#                             crosses 
#                             totalGoals 
#                             totalAssists 
#                             totalGA 
#                             totalGoalConceded 
#                             totelYC 
#                             totalRC 
#                             avgRating 
# ); """

# SQL Queries
INSERT_COUNTRY = " INSERT INTO country (countryName) VALUES (?); "

INSERT_LEAGUE = "INSERT INTO leagues (leagueName, countryID) VALUES (?, ?)"

INSERT_TEAM = " INSERT INTO teams (teamName, countryID) VALUES (?, ?); "

# INSERT_MATCHES = " INSERT INTO matches (date, homeTeamID, awayTeamID, homeScore, awayScore) VALUES (?, ?, ?, ?, ?); "

# INSERT_LEAGUE = " INSERT INTO seasons (teamID) SELECT teamID FROM teams WHERE teamID NOT IN (SELECT teamID FROM seasons); "

# UPDATE_TEAM = """ UPDATE seasons SET matchesPlayed = matchesPlayed + 1,
#                                     wins = wins + ?,
#                                     draws = draws + ?,
#                                     losses = losses + ?,
#                                     goalsScored = goalsScored + ?,
#                                     goalsConceded = goalsConceded + ?,
#                                     points = points + ? 
#                                 WHERE teamID = ?; """

# DISPLAY_LEAGUE = """ SELECT teams.teamName, league.matchesPlayed, league.wins, league.draws, league.losses, league.goalsScored, league.goalsConceded, league.points FROM league
#                     JOIN teams ON league.teamID = teams.teamID
#                     ORDER BY league.points DESC, league.wins DESC; """

# DISPLAY_ALL_MATCHES = """ SELECT matchID, date,
#                             (SELECT teamName FROM teams WHERE teamID = matches.homeTeamID) AS 'Home Team', 
#                             (SELECT teamName FROM teams WHERE teamID = matches.awayTeamID) AS 'Away Team', 
#                             (SELECT homeScore ||'-'|| awayScore) AS Outcome FROM matches
#                             ORDER BY date ASC; """

# GET_MATCHES_BY_DATE = """ SELECT matchID, date, 
#                             (SELECT teamName FROM teams WHERE teamID = matches.homeTeamID) AS 'Home Team',
#                             (SELECT teamName FROM teams WHERE teamID = matches.awayTeamID) AS 'Away Team',
#                             (SELECT homeScore ||'-'|| awayScore) AS Outcome FROM matches
#                             WHERE date = ?
#                             ORDER BY matchID ASC; """

# GET_MATCHES_BY_TEAM = """ SELECT matches.matchID, matches.date, 
#                             (SELECT teamName FROM teams WHERE teamID = matches.homeTeamID) AS 'Home Team',
#                             (SELECT teamName FROM teams WHERE teamID = matches.awayTeamID) AS 'Away Team',
#                             (SELECT homeScore ||'-'|| awayScore) AS Outcome FROM matches
#                             WHERE homeTeamID = ? OR awayTeamID = ?
#                             ORDER by matches.matchID ASC; """

# Functions of the 
def connect():
    return sqlite3.connect("fs_p3.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_COUNTRY_TABLE)
        connection.execute(CREATE_LEAGUE_TABLE)
        connection.execute(CREATE_TEAM_TABLE)
        # connection.execute(CREATE_MATCHES_TABLE)

def add_country(connection, countryName):
    with connection:
        connection.execute(INSERT_COUNTRY, (countryName,))

def add_league(connection, leagueName, countryID):
    with connection:
        # connection.execute(INSERT_TEAM, (teamName,))
        connection.execute(INSERT_LEAGUE, (leagueName, countryID,))

def add_team(connection, teamName, countryID):
    with connection:
        connection.execute(INSERT_TEAM, (teamName, countryID,))

# def add_match(connection, date, homeTeamID, awayTeamID, homeScore, awayScore):
#     with connection:
#         connection.execute(INSERT_MATCHES, (date, homeTeamID, awayTeamID, homeScore, awayScore,))
#         updateLeague(connection, homeTeamID, awayTeamID, homeScore, awayScore)

# def updateLeague(connection, homeTeamID, awayTeamID, homeScore, awayScore):
#     if homeScore > awayScore:
#         homePoints, awayPoints = 3, 0
#         homeWin, awayWin = 1, 0
#         homeLoss, awayLoss = 0, 1
#         draw = 0
#     elif homeScore < awayScore:
#         homePoints, awayPoints = 0, 3
#         homeWin, awayWin = 0, 1
#         homeLoss, awayLoss = 1, 0
#         draw = 0
#     else:
#         homePoints, awayPoints = 1, 1
#         homeWin = awayWin = 0
#         homeLoss = awayLoss = 0
#         draw = 1

#     with connection:
#         connection.execute(UPDATE_TEAM, (homeWin, draw, homeLoss, homeScore, awayScore, homePoints, homeTeamID,))
#         connection.execute(UPDATE_TEAM, (awayWin, draw, awayLoss, awayScore, homeScore, awayPoints, awayTeamID,))

# def displayleague(connection):
#     with connection:    
#         return connection.execute(DISPLAY_LEAGUE).fetchall()

# def displayallmatches(connection):
#     with connection:    
#         return connection.execute(DISPLAY_ALL_MATCHES).fetchall()

# def getmatchesbydate(connection, date):
#     with connection:
#         return connection.execute(GET_MATCHES_BY_DATE, (date,)).fetchall()
    
# def getmatchesbyteam(connection, homeTeamID, awayTeamID):
#     with connection:
#         return connection.execute(GET_MATCHES_BY_TEAM, (homeTeamID, awayTeamID,)).fetchall()