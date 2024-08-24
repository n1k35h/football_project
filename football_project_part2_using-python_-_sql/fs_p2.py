import sqlite3

'''
This is the second part of the Football project, where Goal Scored and Goal Conceded is added to the league table.

Output of the League table
--------------------------
----------------------------------------------------------------------------------------------------
 Teams | Games Played | Games Won | Games Draw | Games Lost | Goals Scored | Goals Conceded | Points
----------------------------------------------------------------------------------------------------
Team A |      5       |     3     |     1      |     1      |      12      |      5         |   10

To Do:
------

SQLite tool:
* Create Database
* Create Table
* Create Queries - additional SQL queries for part 2 is searching matches by date and by teams

Python Tool:
* Functions - which will be the engine part that is required in the application connection

'''

# SQL Statements
CREATE_TEAM_TABLE = """ CREATE TABLE IF NOT EXISTS teams (
                            teamID INTEGER PRIMARY KEY NOT NULL,
                            teamName TEXT NOT NULL
);"""

CREATE_LEAGUE_TABLE = """ CREATE TABLE IF NOT EXISTS league (
                            teamID INTEGER,
                            matchesPlayed INTEGER DEFAULT 0,
                            wins INTEGER DEFAULT 0,
                            draws INTEGER DEFAULT 0,
                            losses INTEGER DEFAULT 0,
                            goalsScored INTEGER DEFAULT 0,
                            goalsConceded INTEGER DEFAULT 0,
                            points INTEGER DEFAULT 0,
                            CONSTRAINT FK_league_teams FOREIGN KEY (teamID) REFERENCES teams (teamID)
);"""

CREATE_MATCHES_TABLE = """ CREATE TABLE IF NOT EXISTS matches (
                            matchID INTEGER PRIMARY KEY NOT NULL,
                            date DATE NOT NULL,
                            homeTeamID INTEGER NOT NULL,
                            awayTeamID INTEGER NOT NULL,
                            homeScore INTEGER NOT NULL,
                            awayScore INTEGER NOT NULL,
                            CONSTRAINT FK_matches_home_team FOREIGN KEY (homeTeamID) REFERENCES teams (teamID),
                            CONSTRAINT FK_matches_away_team FOREIGN KEY (awayTeamID) REFERENCES teams (teamID)
);"""

# SQL Queries
INSERT_TEAM = " INSERT INTO teams (teamName) VALUES (?); "

INSERT_MATCHES = " INSERT INTO matches (date, homeTeamID, awayTeamID, homeScore, awayScore) VALUES (?, ?, ?, ?, ?); "

INSERT_LEAGUE = " INSERT INTO league (teamID) SELECT teamID FROM teams WHERE teamID NOT IN (SELECT teamID FROM league); "

UPDATE_TEAM = """ UPDATE league SET matchesPlayed = matchesPlayed + 1,
                                    wins = wins + ?,
                                    draws = draws + ?,
                                    losses = losses + ?,
                                    goalsScored = goalsScored + ?,
                                    goalsConceded = goalsConceded + ?,
                                    points = points + ? 
                                WHERE teamID = ?; """

DISPLAY_LEAGUE = """ SELECT teams.teamName, league.matchesPlayed, league.wins, league.draws, league.losses, league.goalsScored, league.goalsConceded, league.points FROM league
                    JOIN teams ON league.teamID = teams.teamID
                    ORDER BY league.points DESC, league.wins DESC; """

DISPLAY_ALL_MATCHES = """ SELECT matchID, date,
                            (SELECT teamName FROM teams WHERE teamID = matches.homeTeamID) AS 'Home Team', 
                            (SELECT teamName FROM teams WHERE teamID = matches.awayTeamID) AS 'Away Team', 
                            (SELECT homeScore ||'-'|| awayScore) AS Outcome FROM matches
                            ORDER BY date ASC; """

GET_MATCHES_BY_DATE = """ SELECT matchID, date, 
                            (SELECT teamName FROM teams WHERE teamID = matches.homeTeamID) AS 'Home Team',
                            (SELECT teamName FROM teams WHERE teamID = matches.awayTeamID) AS 'Away Team',
                            (SELECT homeScore ||'-'|| awayScore) AS Outcome FROM matches
                            WHERE date = ?
                            ORDER BY matchID ASC; """

GET_MATCHES_BY_TEAM = """ SELECT matches.matchID, matches.date, 
                            (SELECT teamName FROM teams WHERE teamID = matches.homeTeamID) AS 'Home Team',
                            (SELECT teamName FROM teams WHERE teamID = matches.awayTeamID) AS 'Away Team',
                            (SELECT homeScore ||'-'|| awayScore) AS Outcome FROM matches
                            WHERE homeTeamID = ? OR awayTeamID = ?
                            ORDER by matches.matchID ASC; """

# Functions of the 
def connect():
    return sqlite3.connect("fs_p2.db")

def create_tables(connection):
    with connection:
        connection.execute(CREATE_TEAM_TABLE)
        connection.execute(CREATE_LEAGUE_TABLE)
        connection.execute(CREATE_MATCHES_TABLE)

def add_team(connection, teamName):
    with connection:
        connection.execute(INSERT_TEAM, (teamName,))
        connection.execute(INSERT_LEAGUE)

def add_match(connection, date, homeTeamID, awayTeamID, homeScore, awayScore):
    with connection:
        connection.execute(INSERT_MATCHES, (date, homeTeamID, awayTeamID, homeScore, awayScore,))
        updateLeague(connection, homeTeamID, awayTeamID, homeScore, awayScore)

def updateLeague(connection, homeTeamID, awayTeamID, homeScore, awayScore):
    if homeScore > awayScore:
        homePoints, awayPoints = 3, 0
        homeWin, awayWin = 1, 0
        homeLoss, awayLoss = 0, 1
        draw = 0
    elif homeScore < awayScore:
        homePoints, awayPoints = 0, 3
        homeWin, awayWin = 0, 1
        homeLoss, awayLoss = 1, 0
        draw = 0
    else:
        homePoints, awayPoints = 1, 1
        homeWin = awayWin = 0
        homeLoss = awayLoss = 0
        draw = 1

    with connection:
        connection.execute(UPDATE_TEAM, (homeWin, draw, homeLoss, homeScore, awayScore, homePoints, homeTeamID,))
        connection.execute(UPDATE_TEAM, (awayWin, draw, awayLoss, awayScore, homeScore, awayPoints, awayTeamID,))

def displayleague(connection):
    with connection:    
        return connection.execute(DISPLAY_LEAGUE).fetchall()

def displayallmatches(connection):
    with connection:    
        return connection.execute(DISPLAY_ALL_MATCHES).fetchall()

def getmatchesbydate(connection, date):
    with connection:
        return connection.execute(GET_MATCHES_BY_DATE, (date,)).fetchall()
    
def getmatchesbyteam(connection, homeTeamID, awayTeamID):
    with connection:
        return connection.execute(GET_MATCHES_BY_TEAM, (homeTeamID, awayTeamID,)).fetchall()