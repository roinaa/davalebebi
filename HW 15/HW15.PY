class FootballTeam:
    def __init__(self, team_name, coach):
        self.team_name = team_name
        self.coach = coach
        self.players = [] 

    def add_player(self, name, position, jersey_number, age, nationality):
        for player in self.players:
            if player['jersey_number'] == jersey_number:
                print(f"შეცდომა: მოთამაშე ნომრით {jersey_number} უკვე არის გუნდში.")
                return
        player_data = {
            'name': name,
            'position': position,
            'jersey_number': jersey_number,
            'age': age,
            'nationality': nationality
        }
        self.players.append(player_data)
        print(f"მოთამაშე '{name}' წარმატებით დაემატა გუნდს.")

    def remove_player(self, jersey_number):
        player_to_remove = None
        for player in self.players:
            if player['jersey_number'] == jersey_number:
                player_to_remove = player
                break
        if player_to_remove:
            self.players.remove(player_to_remove)
            print(f"მოთამაშე ნომრით {jersey_number} წარმატებით წაიშალა.")
        else:
            print(f"მოთამაშე ნომრით {jersey_number} ვერ მოიძებნა.")

    def update_player_info(self, jersey_number, key, value):
        player_found = False
        for player in self.players:
            if player['jersey_number'] == jersey_number:
                player[key] = value
                print(f"მოთამაშე {jersey_number}-ის ინფორმაცია განახლდა: დაემატა '{key}': {value}.")
                player_found = True
                break
        if not player_found:
            print(f"მოთამაშე ნომრით {jersey_number} ვერ მოიძებნა.")

    def display_team_info(self):
        print("\n--- კლუბის სრული ინფორმაცია ---")
        print(f"კლუბის სახელი: {self.team_name}")
        print(f"მწვრთნელი: {self.coach}")
        print("მოთამაშეები:")
        if not self.players:
            print("  გუნდი ცარიელია.")
        else:
            for player in self.players:
                print(f"  - {player}")
        print("---------------------------------")

    def display_player_info(self, jersey_number):
        for player in self.players:
            if player['jersey_number'] == jersey_number:
                print(f"\n--- მოთამაშის ინფორმაცია (ნომერი: {jersey_number}) ---")
                for key, value in player.items():
                    formatted_key = key.replace('_', ' ').capitalize()
                    print(f"  {formatted_key}: {value}")
                print("------------------------------------")
                return
        print(f"მოთამაშე ნომრით {jersey_number} ვერ მოიძებნა.")
