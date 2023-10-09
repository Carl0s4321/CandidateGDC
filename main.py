answerYes = ["Yes", "Y", "yes", "y"]
answerNo = ["No", "N", "no", "n"]

# CONSTANTS
STATS_BASE_VALUE = 50
CANDIDATE_STAT_BASE_VALUE = 2

# GLOBAL VARIABLES
game_start = True
year = 0
population = 10000

import random


class Country:
    # id of candidate found in the initial list
    current_candidate = 0

    def __init__(self, population, education, reputation, infrastructure, economy, environment, publicWelfare,
                 lawEnforcement):
        self.population = population
        self.education = education
        self.reputation = reputation
        self.infrastructure = infrastructure
        self.economy = economy
        self.environment = environment
        self.publicWelfare = publicWelfare
        self.lawEnforcement = lawEnforcement

    def updateCountryFromLeaderStat(self, added_stat):
        stats = ["education", "reputation", "infrastructure", "economy", "environment", "publicWelfare", "lawEnforcement"]
        for stat in stats:
            setattr(self, stat, getattr(self, stat) + added_stat.get(f"{stat}_value"))


def initialize_country():
    country = Country(population, STATS_BASE_VALUE, STATS_BASE_VALUE, STATS_BASE_VALUE, STATS_BASE_VALUE,
                      STATS_BASE_VALUE, STATS_BASE_VALUE, STATS_BASE_VALUE)
    return country


class Candidate:
    id = 0
    progress = 0
    times_appeared = 0

    # name (string), story (list of strings), portrait (list of strings), stats (dictionary), goals(function)
    def __init__(self, name, story, portrait, stats, id):
        self.name = name
        self.story = story
        self.portrait = portrait
        self.stats = stats
        self.id = id


# returns a list of Candidates
def initialize_candidates():
    candidate_list = []

    candidate_list.append(
        Candidate(
            "Antonino",
            [
                "   The Business Tycoon   ",
                "Focused on job creation, ",
                "infrastructure, reducing ",
                "crime rate for a safer,  ",
                "prosperous community     ",
            ],
            [
                r"     _-----_     ",
                r"    / \ \ \ \    ",
                r"   |  ^   ^  |   ",
                r"  (   O   O   )  ",
                r"  $|    >    |$  ",
                r"    \ ~~_~~ /    ",
                r"     \_____/     ",
                r"    /  ($)  \    ",
            ],
            {
                "education_value": CANDIDATE_STAT_BASE_VALUE * (-3),
                "reputation_value": 0,
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE,
                "economy_value": CANDIDATE_STAT_BASE_VALUE * (4),
                "environment_value": CANDIDATE_STAT_BASE_VALUE * (-2),
                "welfare_value": CANDIDATE_STAT_BASE_VALUE * (-1),
                "law_value": CANDIDATE_STAT_BASE_VALUE * (2),

                "education_text": CANDIDATE_STAT_BASE_VALUE * (-3),
                "reputation_text": 0,
                "infrastructure_text": CANDIDATE_STAT_BASE_VALUE,
                "economy_text": CANDIDATE_STAT_BASE_VALUE * (4),
                "environment_text": CANDIDATE_STAT_BASE_VALUE * (-2),
                "welfare_text": CANDIDATE_STAT_BASE_VALUE * (-1),
                "law_text": CANDIDATE_STAT_BASE_VALUE * (2),
            },
            0
        )
    )
    candidate_list.append(
        Candidate(
            "Markos",
            [
                "      The Innovator      ",
                "Pioneering technology    ",
                "smart cities, and STEM   ",
                "education, fostering     ",
                "innovation and knowledge ",
            ],
            [
                r"    __-===-__    ",
                r"   ////   \\\\   ",
                r"   |  -   -  |   ",
                r"  (''(0)=(0)'')  ",
                r"   |    \    |   ",
                r"    \  ___  /    ",
                r"     \_____/     ",
                r"    /  \=/  \    ",
            ],
            {
                "education_value": CANDIDATE_STAT_BASE_VALUE * 2,
                "reputation_value": CANDIDATE_STAT_BASE_VALUE * (-2),
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE * (4),
                "economy_value": CANDIDATE_STAT_BASE_VALUE,
                "environment_value": CANDIDATE_STAT_BASE_VALUE * (-3),
                "welfare_value": CANDIDATE_STAT_BASE_VALUE * (-1),
                "law_value": 0,

                "education_text": CANDIDATE_STAT_BASE_VALUE * 2,
                "reputation_text": CANDIDATE_STAT_BASE_VALUE * (-2),
                "infrastructure_text": CANDIDATE_STAT_BASE_VALUE * (4),
                "economy_text": CANDIDATE_STAT_BASE_VALUE,
                "environment_text": CANDIDATE_STAT_BASE_VALUE * (-3),
                "welfare_text": CANDIDATE_STAT_BASE_VALUE * (-1),
                "law_text": 0,
            },
            1
        )
    )
    candidate_list.append(
        Candidate(
            "Sparky",
            [
                "      The Good Boy       ",
                "Bark bark!               ",
                "                         ",
                "                         ",
                "                         ",
            ],
            [
                r"   __-------__   ",
                r"  / /       \ \  ",
                r" | /  o   o  | | ",
                r" | |   ___   | | ",
                r" '='\ / Y \ /'=' ",
                r"     |  U  |     ",
                r"     /\___/\     ",
                r"    /       \    ",
            ],
            {
                "education_value": CANDIDATE_STAT_BASE_VALUE * (-2),
                "reputation_value": CANDIDATE_STAT_BASE_VALUE * 4,
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE * (-1),
                "economy_value": CANDIDATE_STAT_BASE_VALUE * (-1),
                "environment_value": CANDIDATE_STAT_BASE_VALUE * (-1),
                "welfare_value": CANDIDATE_STAT_BASE_VALUE,
                "law_value": CANDIDATE_STAT_BASE_VALUE * 2,

                "education_text": CANDIDATE_STAT_BASE_VALUE * (-2),
                "reputation_text": CANDIDATE_STAT_BASE_VALUE * 4,
                "infrastructure_text": CANDIDATE_STAT_BASE_VALUE * (-1),
                "economy_text": CANDIDATE_STAT_BASE_VALUE * (-1),
                "environment_text": CANDIDATE_STAT_BASE_VALUE * (-1),
                "welfare_text": CANDIDATE_STAT_BASE_VALUE,
                "law_text": CANDIDATE_STAT_BASE_VALUE * 2,
            },
            2
        )
    )
    candidate_list.append(
        Candidate(
            "Connie",
            [
                "      Educator Elite     ",
                "Prioritizing education,  ",
                "healthcare, and social   ",
                "programs to improve      ",
                "citizen's well-being     "
            ],
            [
                r"     _______     ",
                r"  __/)))))))\    ",
                r" ///         \   ",
                r" \_(=(^)=(^)=)   ",
                r"   #    >    #   ",
                r"    \ \___/ /    ",
                r"     \_____/     ",
                r"      /   \      ",
            ],
            {
                "education_value": CANDIDATE_STAT_BASE_VALUE * 4,
                "reputation_value": CANDIDATE_STAT_BASE_VALUE,
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE * (-2),
                "economy_value": CANDIDATE_STAT_BASE_VALUE * (-3),
                "environment_value": 0,
                "welfare_value": CANDIDATE_STAT_BASE_VALUE * 2,
                "law_value": CANDIDATE_STAT_BASE_VALUE * (-1),

                "education_text": CANDIDATE_STAT_BASE_VALUE * 4,
                "reputation_text": CANDIDATE_STAT_BASE_VALUE,
                "infrastructure_text": CANDIDATE_STAT_BASE_VALUE * (-2),
                "economy_text": CANDIDATE_STAT_BASE_VALUE * (-3),
                "environment_text": 0,
                "welfare_text": CANDIDATE_STAT_BASE_VALUE * 2,
                "law_text": CANDIDATE_STAT_BASE_VALUE * (-1),
            },
            3
        )
    )
    candidate_list.append(
        Candidate(
            "Biben",
            [
                " Law and Order Advocate  ",
                "Tough on crime policies, ",
                "securing the country,    ",
                "prioritizing security    ",
                "focused infrastructure   "
            ],
            [
                r"    __-===-__    ",
                r"   /”`     `”\   ",
                r"   | /// /// |   ",
                r"  [   O   O   ]  ",
                r"   |    L    |   ",
                r"    \ mmmmm /    ",
                r"     \_____/     ",
                r"    /   | * \    ",
            ],
            {
                "education_value": CANDIDATE_STAT_BASE_VALUE,
                "reputation_value": CANDIDATE_STAT_BASE_VALUE * (-1),
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE * 2,
                "economy_value": CANDIDATE_STAT_BASE_VALUE * (-2),
                "environment_value": -  CANDIDATE_STAT_BASE_VALUE * (-1),
                "welfare_value": CANDIDATE_STAT_BASE_VALUE * (-3),
                "law_value": CANDIDATE_STAT_BASE_VALUE * 4,

                "education_text": CANDIDATE_STAT_BASE_VALUE,
                "reputation_text": "?",
                "infrastructure_text": CANDIDATE_STAT_BASE_VALUE * 2,
                "economy_text": CANDIDATE_STAT_BASE_VALUE * (-2),
                "environment_text": CANDIDATE_STAT_BASE_VALUE * (-1),
                "welfare_text": CANDIDATE_STAT_BASE_VALUE * (-3),
                "law_text": CANDIDATE_STAT_BASE_VALUE * 4,
            },
            4
        )
    )
    candidate_list.append(
        Candidate(
            "Dianna",
            [
                "  Avid Environmentalist  ",
                "Proposes to eradicate    ",
                "climate change through   ",
                "practical technological  ",
                "solutions.               ",
            ],
            [
                r"    _--===--_    ",
                r"   //|||||||\\   ",
                r"   |/       \|   ",
                r"  /|  /\ /\  |\  ",
                r"  |%    >    %|  ",
                r"  ||\ \___/ /||  ",
                r"  |||\_____/|||  ",
                r"  ||| /   \ |||  ",
            ],
            {
                "education_value": CANDIDATE_STAT_BASE_VALUE,
                "reputation_value": CANDIDATE_STAT_BASE_VALUE * (-2),
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE * 2,
                "economy_value": CANDIDATE_STAT_BASE_VALUE * (-3),
                "environment_value": CANDIDATE_STAT_BASE_VALUE * 4,
                "welfare_value": CANDIDATE_STAT_BASE_VALUE,
                "law_value": CANDIDATE_STAT_BASE_VALUE * (-1),

                "education_text": CANDIDATE_STAT_BASE_VALUE,
                "reputation_text": CANDIDATE_STAT_BASE_VALUE * (-2),
                "infrastructure_text": CANDIDATE_STAT_BASE_VALUE * 2,
                "economy_text": CANDIDATE_STAT_BASE_VALUE * (-3),
                "environment_text": CANDIDATE_STAT_BASE_VALUE * 4,
                "welfare_text": CANDIDATE_STAT_BASE_VALUE,
                "law_text": CANDIDATE_STAT_BASE_VALUE * (-1),
            },
            5
        )
    )
    candidate_list.append(
        Candidate(
            "Schwarz",
            [
                "       The Dictator      ",
                "Rules through propaganda ",
                "and military might,      ",
                "enforcing full control,  ",
                "in pursuit of dominance  ",
            ],
            [
                r"   .#########.   ",
                r"   |  x      |   ",
                r"   | \__ __/ |   ",
                r"  [   O   O   ]  ",
                r"   \\   V   //   ",
                r"    \\==_==//    ",
                r" _-==\_____/==-_ ",
                r"|   /***|***\   |",
            ],
            {
                "education_value": CANDIDATE_STAT_BASE_VALUE,
                "reputation_value": CANDIDATE_STAT_BASE_VALUE * (-8),
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE * 2,
                "economy_value": CANDIDATE_STAT_BASE_VALUE * 2,
                "environment_value": CANDIDATE_STAT_BASE_VALUE * (-6),
                "welfare_value": CANDIDATE_STAT_BASE_VALUE * (-1),
                "law_value": CANDIDATE_STAT_BASE_VALUE * 10,

                "education_text": CANDIDATE_STAT_BASE_VALUE,
                "reputation_text": "?",
                "infrastructure_text": CANDIDATE_STAT_BASE_VALUE * 2,
                "economy_text": CANDIDATE_STAT_BASE_VALUE * 2,
                "environment_text": "?",
                "welfare_text": CANDIDATE_STAT_BASE_VALUE * (-1),
                "law_text": CANDIDATE_STAT_BASE_VALUE * 10,
            },
            6
        )
    )

    return candidate_list


def special_events():
    # pandemic
    # conspiracy / misinformation
    # climate change
    # space activity
    # mafia/terrorist activity
    # war
    # economic depression
    pass


# prints out the candidates horizontally
def display_candidates(candidate1, candidate2, candidate3):
    longest_background = max(len(candidate1.story),
                             len(candidate2.story),
                             len(candidate3.story))

    display_text = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{:^25}|{:^25}|{:^25}|
-------------------------|-------------------------|-------------------------|
  []=================[]  |  []=================[]  |  []=================[]  |
  ||{}||  |  ||{}||  |  ||{}||  |
  ||{}||  |  ||{}||  |  ||{}||  |
  ||{}||  |  ||{}||  |  ||{}||  |
  ||{}||  |  ||{}||  |  ||{}||  |
  ||{}||  |  ||{}||  |  ||{}||  |
  ||{}||  |  ||{}||  |  ||{}||  |
  ||{}||  |  ||{}||  |  ||{}||  |
  ||{}||  |  ||{}||  |  ||{}||  |
  []=================[]  |  []=================[]  |  []=================[]  |
-------------------------|-------------------------|-------------------------|\n"""
    # insert the text
    display_text = display_text.format(
        # there looks like this could be solved this with a for loop but the format function
        # requires all parameters to be filled
        candidate1.name, candidate2.name, candidate3.name,
        candidate1.portrait[0], candidate2.portrait[0], candidate3.portrait[0],
        candidate1.portrait[1], candidate2.portrait[1], candidate3.portrait[1],
        candidate1.portrait[2], candidate2.portrait[2], candidate3.portrait[2],
        candidate1.portrait[3], candidate2.portrait[3], candidate3.portrait[3],
        candidate1.portrait[4], candidate2.portrait[4], candidate3.portrait[4],
        candidate1.portrait[5], candidate2.portrait[5], candidate3.portrait[5],
        candidate1.portrait[6], candidate2.portrait[6], candidate3.portrait[6],
        candidate1.portrait[7], candidate2.portrait[7], candidate3.portrait[7],
    )

    # add more lines to account for the longest story
    for i in range(0, longest_background):
        display_text += "{:<25}|{:<25}|{:<25}|\n"

        story1 = ""
        story2 = ""
        story3 = ""

        if i < len(candidate1.story):
            story1 = candidate1.story[i]

        if i < len(candidate2.story):
            story2 = candidate2.story[i]

        if i < len(candidate3.story):
            story3 = candidate3.story[i]

        display_text = display_text.format(
            story1, story2, story3)

    display_text += "-------------------------|-------------------------|-------------------------|\n"

    stat_names = ["Education:", "Reputation:", "Infrastructure:", "Economy:", "Environment:", "Public Welfare:",
                  "Law Enforcement:"]
    # add lines based on the amount of stats
    for j in range(7, 14):
        display_text += "{:<25}|{:<25}|{:<25}|\n"
        display_text = display_text.format(
            stat_names[j % 7] + str(tuple(candidate1.stats.values())[j]),
            stat_names[j % 7] + str(tuple(candidate2.stats.values())[j]),
            stat_names[j % 7] + str(tuple(candidate3.stats.values())[j]),
        )

    display_text += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    print(display_text)


# used at the start of the game
def get_three_random_candidates(candidate_list):
    running_ids = set()
    while (len(running_ids) < 3):
        running_ids.add(random.randint(0, len(candidate_list) - 1))

    running_candidates = []
    for id in running_ids:
        candidate = candidate_list[id]
        candidate.times_appeared += 1
        running_candidates.append(candidate)

    return running_candidates


# returns three candidates that appeared less than others
# always show the current candidate that is rerunning
def get_semi_random_candidates(current_candidate, candidate_list):
    highest_appearance = -1
    # amount of appearances, index of candidate
    first_lowest_appearance = [1000, -1]
    second_lowest_appearance = [1000, -1]

    for i in range(0, len(candidate_list)):
        highest_appearance = max(highest_appearance, candidate_list[i].times_appeared)

        # initialize
        if (first_lowest_appearance[1] == -1):
            first_lowest_appearance[0] = candidate_list[i].times_appeared
            first_lowest_appearance[1] = i
        elif (second_lowest_appearance[1] == -1):
            second_lowest_appearance[0] = candidate_list[i].times_appeared
            second_lowest_appearance[1] = i

        # check if appeared less
        elif (candidate_list[i].times_appeared < first_lowest_appearance[0]):
            first_lowest_appearance[0] = candidate_list[i].times_appeared
            first_lowest_appearance[1] = i
        elif (candidate_list[i].times_appeared < second_lowest_appearance[0]):
            second_lowest_appearance[0] = candidate_list[i].times_appeared
            second_lowest_appearance[1] = i

    # increase appearance
    current_candidate.times_appeared = highest_appearance
    candidate_list[first_lowest_appearance[1]].times_appeared += 1
    candidate_list[second_lowest_appearance[1]].times_appeared += 1

    list_of_ids = [current_candidate.id, first_lowest_appearance[1], second_lowest_appearance[2]]
    running_candidates = []
    # randomize order
    while len(list_of_ids) > 0:
        index = random.randint(0, len(list_of_ids) - 1)
        id = list_of_ids[index]
        running_candidates.append[candidate_list[id]]
        list_of_ids.pop(index)

    return running_candidates


def candidate_vote(*candidates):
    votes = {}

    for candidate in candidates:
        while True:
            user_input = input(f"How many votes for {candidate.name}?\n>> ")
            if user_input.isdigit():
                user_input = int(user_input)
                if user_input <= population:
                    votes[candidate] = int(user_input)
                    break
                else:
                    print("Invalid input. Please enter a valid number of votes.")
            else:
                print("Invalid input. Please enter a valid number of votes.")

    return votes


def doElection(candidate_list):
    print("*************************** VOTE YOUR LEADER *****************************")
    display_list = get_three_random_candidates(candidate_list)
    display_candidates(display_list[0], display_list[1], display_list[2])
    votes = candidate_vote(display_list[0], display_list[1], display_list[2])
    for candidate, vote_count in votes.items():
        if vote_count == max(votes.values()):
            print(f"{candidate.name} has won the election with {vote_count} votes!")
            return candidate


def updateStory(leader_id):
    # BUSINESS TYCOON
    if leader_id == 0:
        if year == 1:
            print('''The Environmentalist initiates sweeping changes. They implement strict 
regulations to reduce carbon emissions and promote renewable energy. 
The city's skyline begins to change as solar panels and wind turbines 
become a common sight. Environmental education is integrated into 
schools, raising awareness about sustainability.''')

# # TECH INNOVATOR
# elif leaderID == 1:
# # GOOD BOY
# elif leaderID == 2:
# # EDUCATOR ELITE
# elif leaderID == 3:
# # LAW AND ORDER ADVOCATE
# elif leaderID == 4:
# # ENVIRONMENTALIST
# elif leaderID == 5:
# # DICTATOR
# else:


def main():
    print('''-----------------------------------------------------------------------                                                                                      
  .g8"""bgd `7MMF'MMP""MM""YMM `7MMF'MMM"""AMV `7MM"""YMM  `7MN.   `7MF'
.dP'     `M   MM  P'   MM   `7   MM  M'   AMV    MM    `7    MMN.    M
dM'       `   MM       MM        MM  '   AMV     MM   d      M YMb   M
MM            MM       MM        MM     AMV      MMmmMM      M  `MN. M
MM.           MM       MM        MM    AMV   ,   MM   Y  ,   M   `MM.M
`Mb.     ,'   MM       MM        MM   AMV   ,M   MM     ,M   M     YMM
  `"bmmmd'  .JMML.   .JMML.    .JMML.AMVmmmmMM .JMMmmmmMMM .JML.    YM
----------------...Carlos Sujanto and Jimmy Xu...----------------------\n''')

    print('''In a distant land, ''' + str(population) + ''' souls set forth to build a new nation.  As homes 
rose and hopes soared, the need for a leader became clear. You, a simple
citizen and a population of like minded people, found yourself at the 
heart of this moment: choosing a leader.

              The nation's destiny hinged on your decision.\n\n''')

    candidate_list = initialize_candidates()
    country = initialize_country()
    leader = doElection(candidate_list)
    country.updateCountryFromLeaderStat(leader.stats)

    # while game_start:
    #     print("[YEAR:", year, "]")
    #     updateStory(leader.ID)


main()
