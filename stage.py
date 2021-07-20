from util import get_upcoming_matches, get_current_region_standings, result


class Stage:
    final_standings = {}
    upcoming_matches = []

    def __init__(self, url):
        self.standings = get_current_region_standings(url)
        self.teams = list(get_current_region_standings(url))
        self.upcoming_matches = get_upcoming_matches(url)
        self.new_standings = {}
        self.top_four = {}
        self.num_placements = {}

    def step(self):
        new_standings = {t: int(self.standings[t]) for t in self.teams}  # {t: 0 for t in self.teams}
        # print(new_standings)
        for match in self.upcoming_matches:
            team_1 = match[0]
            team_2 = match[1]
            # print(team_1 + " vs. " + team_2)
            # haha no switch case go brrr
            match_result = result()
            if match_result == "t1":
                new_standings[team_1] += 3
                # print("Winner: " + team_1)
                # print(team_1 + " points: " + str(new_standings[team_1]))
            if match_result == "t1 OT":
                new_standings[team_1] += 2
                new_standings[team_2] += 1
                # print("OT Winner: " + team_1)
                # print(team_1 + " points: " + str(new_standings[team_1]))
            if match_result == "t2":
                new_standings[team_2] += 3
                # print("Winner: " + team_2)
                # print(team_2 + " points: " + str(new_standings[team_2]))
            if match_result == "t2 OT":
                new_standings[team_1] += 1
                new_standings[team_2] += 2
                # print("OT Winner: " + team_2)
                # print(team_2 + " points: " + str(new_standings[team_2]))
        standings_sorted = sorted(new_standings.items(), key=lambda kv: (kv[1], kv[0]))
        return {t[0]: t[1] for t in standings_sorted}

    def run(self, steps):
        self.num_placements = {t: [0 for i in list(self.standings)] for t in list(self.standings)}
        for i in range(steps):
            standings_step = self.step()
            # print(standings_step)
            for team in standings_step.keys():
                self.num_placements[team][list(standings_step).index(team)] += 100 * 1 / steps
        self.top_four = {t: sum(self.num_placements[t][len(standings_step) - 4:]) * 100 / steps for t in
                         list(self.num_placements)}

    def display_stats(self):
        placements_clean = {t: [str(self.num_placements[t][i])[:5] + "%" for i in range(len(self.num_placements[t]))] for t in self.num_placements}
        top_four_clean={t: str(self.top_four[t]*100)[:5] + "%" for t in self.top_four}
        print("chance that each team ends up in each place on leaderboard")
        print(placements_clean)
        print("chance that team ends up in top four")
        print(top_four_clean)
