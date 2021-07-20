import requests


def find_all(string, to_find, start=0, end=10000000):
    # print(string)
    f = [string.find(to_find, start, end)]
    # print(f)
    i = 0
    while f[i] != -1:
        f.append(string.find(to_find, f[i] + 1, end))
        i += 1
    f.remove(f[len(f) - 1])
    return f


def get_current_region_standings(url):
    page = requests.get(url)
    data = page.text
    indices = []
    standings = {}

    indices.append(data.find("background-color:rgba", 35000))
    for i in range(data.count("tr style", 35000, 46000) - 1):
        keyword = data.find("background-color:rgba", indices[i] + 1)
        if keyword == -1:
            indices.append(38000)
        else:
            indices.append(keyword)

    for index in indices:
        name = ""
        start_name = data.find("alt=\"\">", index + 1) + 8
        end_name = data.find(" </a> </td>", start_name + 1)
        start_score = data.find(" <td>", index + 1) + 5
        end_score = data.find("</td> ", start_score + 1)
        # print(start_name, end_name, start_score, end_score, index)
        score = data[start_score:end_score]
        name = data[start_name:end_name]
        standings[name] = score
    # print(data)
    # print(URL[30:33])
    return standings


def get_upcoming_matches(URL):
    matches = []
    teams = []
    keyword = "class=\"match__name text-truncate\"> "
    new_link = "https://siege.gg/matches?tab=upcoming&competitions[]=" + URL[30:33] + "&page=1"
    page = requests.get(new_link)
    data = page.text
    for index in find_all(data, keyword, data.find("class=\"matches__upcoming tab-pane js-matches-list fade show "
                                                   "active\""),
                          data.find("class=\"matches__results tab-pane js-matches-list fade \"")):
        start_team_name = index + len(keyword)
        end_team_name = data.find("</s", index)
        team_name = data[start_team_name:end_team_name - 1]
        # print(team_name)
        # print(index)
        teams.append(team_name)
    for i in range(0, len(teams), 2):
        temp = list(matches)
        temp.append((teams[i], teams[i + 1]))
        matches = tuple(temp)
    matches = list(set(matches))
    return matches
    indices = []


# class="match__name text-truncate"
brazil_link = "https://siege.gg/competitions/325-brasileirao-2021-stage-2"
north_america_link = "https://siege.gg/competitions/320-north-american-league-2021-stage-2"
europe_link = "https://siege.gg/competitions/323-european-league-2021-stage-2"
gsa_link = "https://siege.gg/competitions/312-gsa-league-2021"
apac_south_link = "https://siege.gg/competitions/322-apac-south-division-2021-stage-2"
apac_north_link = "https://siege.gg/competitions/321-apac-north-division-2021-stage-2"

import random


def result():
    r = random.randint(0, 100)
    if r < 40:
        return "t1"
    elif r < 80:
        return "t2"
    elif r < 90:
        return "t1 OT"
    else:
        return "t2 OT"
    return r
