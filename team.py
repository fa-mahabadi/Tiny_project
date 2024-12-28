class Team:
    all_teams = {}

    def __init__(self, team_name: str, win_game: int, lost_game: int, equal_game: int):
        self.team_name = team_name
        self.win_game = win_game
        self.lost_game = lost_game
        self.equal_game = equal_game
        self.total_game = self.win_game + self.equal_game + self.lost_game
        self.apply_score()

    def apply_score(self):
        """calculate score and create teams dictionary"""
        self.team_score = self.win_game * 3 + self.equal_game
        Team.all_teams[self.team_name] = {
            "win": self.win_game,
            "equal": self.equal_game,
            "lost": self.lost_game,
            "total_game": self.total_game,
            "score": self.team_score,
        }

    @classmethod
    def create_team(cls):
        """get input and create team"""
        team_name = input("Enter team name: ")
        win_game = int(input("Enter win game: "))
        lost_game = int(input("Enter lost game: "))
        equal_game = int(input("Enter equal game: "))
        team = Team(team_name, win_game, lost_game, equal_game)

        print(f"team {team_name} created successful ")

    @classmethod
    def sort_team(cls):
        """sort team dictionary base score"""
        if not cls.all_teams:
            print("not created teams")
            return
        print("\nLiga Table:")
        print(f"team      | win      | equal    | lost     |total_game| score   ")
        sorted_teams = sorted(
            cls.all_teams.items(), key=lambda item: item[1]["score"], reverse=True
        )
        for team, data in sorted_teams:
            print(
                f"{team:<10}|  {data['win']:<8}|  {data['equal']:<8}|  {data['lost']:<8}|  {data['total_game']:<8}| {data['score']:<8}"
            )
        print()


while True:
    print("1. create team")
    print("2. Liga table")
    print("3. exit")
    menu = int(input("Please enter your choose: "))

    if menu == 1:
        Team.create_team()
    elif menu == 2:
        Team.sort_team()
    elif menu == 3:
        exit()
    else:
        print("your selection must be from menu")
