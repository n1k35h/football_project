import simple_football_system as sfs

'''
This is the first part of the Football project and the below coding is a simple football application,
where user can add teams, add matches and view the league.

1) Develop a menu where user can choose an option

2) Establish a connection to the simple_football_system, which is the core engine behind the application

'''

MENU_PROMPT = """\n --- Simple Football Database App ---

Please choose one of the following options:

1) Add Team
2) Add Match
3) Display the League
4) Exit

Your selection: """

def menu():
    connection = sfs.connect()
    sfs.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "4":
        if user_input == "1":
            teamName = input("Enter the Team Name: ")
            sfs.add_team(connection, teamName)
            print(f"\n{teamName} has been added to the Team table.")

        elif user_input == "2":
            date = input("Enter the Date (DD/MM/YYYY): ")
            homeTeamID = int(input("Enter the Home Team ID: "))
            awayTeamID = int(input("Enter the Away Team ID: "))
            homeScore = int(input("Enter the Home Score: "))
            awayScore = int(input("Enter the Away Score: "))
            sfs.add_match(connection, date, homeTeamID, awayTeamID, homeScore, awayScore)
            print("\nMatch added to the table.")

        elif user_input == "3":
            leagues = sfs.displayleague(connection)
            print("\n")
            print(f"{'Team':<20}{'GP':<4}{'W':<3}{'D':<3}{'L':<3}{'Pts':<3}")
            print("-" * 36)
            for row in leagues:
                print(f"{row[0]:<20}{row[1]:<4}{row[2]:<3}{row[3]:<3}{row[4]:<3}{row[5]:<3}")

        else:
            print("\nInvalid input, please enter a valid option from the Menu!")

menu()
