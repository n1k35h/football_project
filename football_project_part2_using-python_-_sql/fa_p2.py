import fs_p2 as fs

'''
This is the second part of the Football project, which incorporates the metrics of Goals Scored 
and Goals Conceded into the league table.

1) Develop a menu that allows users to select from various options, including three new features:

                    a) View all matches
                    b) search matches by date
                    c) search matches by teams

2) Establish a connection to the fs_p2 python file, which serves as the core engine for the application.

'''

MENU_PROMPT = """\n --- Football Database App ---

Please choose one of the following options:

1) Add Team
2) Add Match
3) Display the League
4) View all Match Results
5) Search by Dates
6) Search by Teams
7) Exit

Your selection: """

def menu():
    connection = fs.connect()
    fs.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "7":
        if user_input == "1":
            teamName = input("Enter the Team Name: ")
            fs.add_team(connection, teamName)
            print(f"\n{teamName} has been added to the Team table.")

        elif user_input == "2":
            date = input("Enter the Date (DD/MM/YYYY): ")
            homeTeamID = int(input("Enter the Home Team ID: "))
            awayTeamID = int(input("Enter the Away Team ID: "))
            homeScore = int(input("Enter the Home Score: "))
            awayScore = int(input("Enter the Away Score: "))
            fs.add_match(connection, date, homeTeamID, awayTeamID, homeScore, awayScore)
            print("\nMatch added to the table.")

        elif user_input == "3":
            leagues = fs.displayleague(connection)
            print("\n")
            print(f"{'Team':<15}| {'GP':<4}| {'W':<3}| {'D':<3}| {'L':<3}| {'GS':<3}| {'GA':<3}| {'Pts':<3}")
            print("-" * 53)
            for row in leagues:
                print(f"{row[0]:<15}| {row[1]:<4}| {row[2]:<3}| {row[3]:<3}| {row[4]:<3}| {row[5]:<3}| {row[6]:<3}| {row[7]:<3}")

        elif user_input == "4":
            matches = fs.displayallmatches(connection)
            print("\n")
            print(f"{'M ID':<5}| {'Match Date':<10} | {'Home Team':<10} | {'Away Team':<10} | {'Outcome':<10}")
            print("-" * 55)
            for row in matches:
                print(f"{row[0]:<5}| {row[1]:<10} | {row[2]:<10} | {row[3]:<10} | {row[4]:<10}")

        elif user_input == "5":
            date = input("Enter the Date to view (DD/MM/YYYY): ")
            ds = fs.getmatchesbydate(connection, date)
            print("\n")
            print(f"{'M ID':<5}| {'Match Date':<10} | {'Home Team':<10} | {'Away Team':<10} | {'Outcome':<10}")
            print("-" * 55)

            for row in ds:
                print(f"{row[0]:<5}| {row[1]:<10} | {row[2]:<10} | {row[3]:<10} | {row[4]:<10}")

        elif user_input == "6":
            TeamID = input("Enter the Team ID: ")
            teams = fs.getmatchesbyteam(connection, homeTeamID=TeamID, awayTeamID=TeamID)
            print("\n")
            # print("All ", TeamID,"matches")
            print(f"{'M ID':<5}| {'Match Date':<10} | {'Home Team':<10} | {'Away Team':<10} | {'Outcome':<10}")
            print("-" * 55)

            for row in teams:
                print(f"{row[0]:<5}| {row[1]:<10} | {row[2]:<10} | {row[3]:<10} | {row[4]:<10}")

        else:
            print("\nInvalid input, please enter a valid option from the Menu!")

menu()
