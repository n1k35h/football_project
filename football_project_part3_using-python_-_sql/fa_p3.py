import fs_p3 as fsp3

'''
This is the third part of the Football project, which incorporates the metrics of Goals Scored 
and Goals Conceded into the league table.

1) Develop a menu that allows users to select from various options, including eight new features:

                    a) Add Country
                    b) Add League
                    c) Add Players
                    d) Search League
                    e) Search Country
                    f) Statistic - Players, Teams, Matches

2) Establish a connection to the fs_p2 python file, which serves as the core engine for the application.

'''

MENU_PROMPT = """\n --- Football Database App ---

Please choose one of the following options:

1) Add Country
2) Add League
3) Add Team
4) Add Player
5) Add Matches
6) Display the League season
7) View all Match Results
8) Search by Date
9) Search by League
10) Search by Team
11) Search by Country
12) Player Statistic
13) Team Statistic
14) Match Statistic
15) Exit

Your selection: """

def menu():
    connection = fsp3.connect()
    fsp3.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "15":
        if user_input == "1":
            countryName = input("Enter the Country Name: ")
            fsp3.add_country(connection, countryName)
            print(f"\n{countryName} has been added to the Team table.")

        elif user_input == "2":
            leagueName = input("Enter the League Name: ")
            countryID = input("Enter Country ID: ")
            fsp3.add_league(connection, leagueName, countryID)
            print(f"\n{leagueName} has been added to the League table.")

            # date = input("Enter the Date (DD/MM/YYYY): ")
            # homeTeamID = int(input("Enter the Home Team ID: "))
            # awayTeamID = int(input("Enter the Away Team ID: "))
            # homeScore = int(input("Enter the Home Score: "))
            # awayScore = int(input("Enter the Away Score: "))
            # fs.add_match(connection, date, homeTeamID, awayTeamID, homeScore, awayScore)
            # print("\nMatch added to the table.")

        elif user_input == "3":
            teamName = input("Enter the Team Name: ")
            countryID = input("Enter Country ID: ")
            fsp3.add_team(connection, teamName, countryID)
            print(f"\n{teamName} has been added to the Team table.")
            
            # leagues = fs.displayleague(connection)
            # print("\n")
            # print(f"{'Team':<15}| {'GP':<4}| {'W':<3}| {'D':<3}| {'L':<3}| {'GS':<3}| {'GA':<3}| {'Pts':<3}")
            # print("-" * 53)
            # for row in leagues:
            #     print(f"{row[0]:<15}| {row[1]:<4}| {row[2]:<3}| {row[3]:<3}| {row[4]:<3}| {row[5]:<3}| {row[6]:<3}| {row[7]:<3}")

        elif user_input == "4":
            pass
            # matches = fs.displayallmatches(connection)
            # print("\n")
            # print(f"{'M ID':<5}| {'Match Date':<10} | {'Home Team':<10} | {'Away Team':<10} | {'Outcome':<10}")
            # print("-" * 55)
            # for row in matches:
            #     print(f"{row[0]:<5}| {row[1]:<10} | {row[2]:<10} | {row[3]:<10} | {row[4]:<10}")

        elif user_input == "5":
            pass
            # date = input("Enter the Date to view (DD/MM/YYYY): ")
            # ds = fs.getmatchesbydate(connection, date)
            # print("\n")
            # print(f"{'M ID':<5}| {'Match Date':<10} | {'Home Team':<10} | {'Away Team':<10} | {'Outcome':<10}")
            # print("-" * 55)

            # for row in ds:
            #     print(f"{row[0]:<5}| {row[1]:<10} | {row[2]:<10} | {row[3]:<10} | {row[4]:<10}")

        elif user_input == "6":
            pass
            # TeamID = input("Enter the Team ID: ")
            # teams = fs.getmatchesbyteam(connection, homeTeamID=TeamID, awayTeamID=TeamID)
            # print("\n")
            # # print("All ", TeamID,"matches")
            # print(f"{'M ID':<5}| {'Match Date':<10} | {'Home Team':<10} | {'Away Team':<10} | {'Outcome':<10}")
            # print("-" * 55)

            # for row in teams:
            #     print(f"{row[0]:<5}| {row[1]:<10} | {row[2]:<10} | {row[3]:<10} | {row[4]:<10}")

        elif user_input == "7":
            pass

        elif user_input == "8":
            pass

        elif user_input == "9":
            pass

        elif user_input == "10":
            pass

        elif user_input == "11":
            pass

        elif user_input == "12":
            pass

        else:
            print("\nInvalid input, please enter a valid option from the Menu!")



menu()