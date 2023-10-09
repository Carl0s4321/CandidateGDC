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
    rulingYear = 0
    progress = 0
    times_appeared = 0
    goals = []
    events = []

    # name (string), story (list of strings), portrait (list of strings), stats (dictionary), goals(function)
    def __init__(self, name, story, portrait, stats, id):
        self.name = name
        self.story = story
        self.portrait = portrait
        self.stats = stats
        self.id = id

    def updateStory(self):
        # BUSINESS TYCOON
        if self.id == 0:
            if self.rulingYear == 1:
                print(''' ''')
        # TECH INNOVATOR
        elif self.id == 1:
            pass
        # GOOD BOY
        elif self.id == 2:
            pass
        # EDUCATOR ELITE
        elif self.id == 3:
            pass
        # LAW AND ORDER ADVOCATE
        elif self.id == 4:
            pass
        # ENVIRONMENTALIST
        elif self.id == 5:
            if self.rulingYear == 1:
                print('''With the Environmentalist elected as the leader, the nation 
embarks on a journey toward sustainability. The first year sees sweeping 
changes, with strict regulations to reduce carbon emissions and promote 
renewable energy. Challenges arise as some citizens in energy-dependent 
industries face job losses, leading to protests and economic concerns. 
[Economy -6, Public Welfare -3, Environment +4]''')

            elif self.rulingYear == 2:
                print('''As the economy adapts to renewable energy and green technology, 
new jobs are created, but economic disparities persist. The Environmentalist 
faces the challenge of bridging the gap between the growing green sector and 
those affected by declining traditional industries. Meanwhile, opposition to 
the rapid changes intensifies, with some calling for a rollback of policies. 
[Economy +4, Public Welfare -3, Environment +3]''')
                self.stats.get("economy")

            elif self.rulingYear == 3:
                print('''The Environmentalist introduces policies to protect natural 
habitats and wildlife. Conservation efforts gain traction, but confrontations 
arise with industries seeking to exploit natural resources. Balancing 
environmental protection with economic interests becomes a major challenge. 
Protests both for and against environmental policies escalate, leading to 
tensions within the nation. 
[Environment +6, Economy -2, Law Enforcement -4]''')

            elif self.rulingYear == 4:
                print('''Despite economic growth, the nation faces fiscal pressures due 
to heavy investments in green infrastructure. Citizens express concerns about 
rising taxes and government spending. The Environmentalist must navigate 
a delicate balance between maintaining economic stability and continuing 
to fund environmental initiatives. Opposition parties grow stronger, 
demanding fiscal responsibility. 
[Economy -5, Country's Reputation -3, Public Welfare -2]''')

            elif self.rulingYear == 5:
                print('''The nation's commitment to sustainability gains international 
recognition, but it comes with expectations of global leadership in environmental
matters. Balancing international obligations with domestic priorities becomes 
a challenge. The Environmentalist faces pressure to allocate resources to global 
initiatives, which sparks debate and dissent at home. 
[Country's Reputation +5, Economy -3, Public Welfare -2]''')

            elif self.rulingYear == 6:
                print('''As the Environmentalist leader reaches the midpoint of their term, 
she reflects on her achievements and challenges. The nation stands as a symbol of 
sustainability, but the journey is far from over. The Environmentalist must continue 
to navigate the complexities of the policies and prepare for a smooth transition 
of power in two years. Choosing a successor who shares her vision while 
addressing the concerns of the opposition becomes a critical decision. 
[Country's Reputation +3, Economy +2, Public Welfare +1]''')

            elif self.rulingYear == 7:
                print('''With the Environmentalist leader's term now in its seventh year, 
the nation faces ongoing challenges. While the transition of power is not imminent, 
the leader must continue to build on the legacy and address unresolved issues. 
Economic stability improves, but public welfare concerns linger. Protests and political
polarization intensify as the nation looks ahead to the upcoming election year. 
[Economy +2, Public Welfare -1, Law Enforcement -2]''')

            elif self.rulingYear == 8:
                print('''As the Environmentalist leader's term reaches its eighth year, 
the nation stands as a symbol of sustainability. The leader's policies have left a 
lasting impact, with a more sustainable economy and environment. Renewable energy 
is now a cornerstone of the nation's power supply, and conservation efforts have 
preserved natural habitats. However, economic disparities persist, and the 
nation's reputation on the international stage remains a subject of debate. 
The nation looks ahead to its future. 
[Country's Reputation +1, Economy +1, Public Welfare +1]''')
        # DICTATOR
        else:
            pass

    #amount (int)
    def move_to_goal(self, amount):
        self.progress += amount
        goal = self.goals[0]
        if(self.progress > goal.progress_needed):
            print(goal.story_on_completion)
            self.goals.pop(0)
            self.progress -= goal.progress_needed

            if(len(self.goals) == 0):
                #provide an ending to game
                pass


class Goal:
    progress_needed = 0
    story_on_completion = ""
    def __init__(self, progress_needed, story):
        self.progress_needed = progress_needed
        self.story_on_completion = story



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
                "education_value":      CANDIDATE_STAT_BASE_VALUE*(-3),
                "reputation_value":     0,
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE,
                "economy_value":        CANDIDATE_STAT_BASE_VALUE*(4),
                "environment_value":    CANDIDATE_STAT_BASE_VALUE*(-2),
                "welfare_value":        CANDIDATE_STAT_BASE_VALUE*(-1),
                "law_value":            CANDIDATE_STAT_BASE_VALUE*(2),

                "education_text":       CANDIDATE_STAT_BASE_VALUE*(-3),
                "reputation_text":      0,
                "infrastructure_text":  CANDIDATE_STAT_BASE_VALUE,
                "economy_text":         CANDIDATE_STAT_BASE_VALUE*(4),
                "environment_text":     CANDIDATE_STAT_BASE_VALUE*(-2),
                "welfare_text":         CANDIDATE_STAT_BASE_VALUE*(-1),
                "law_text":             CANDIDATE_STAT_BASE_VALUE*(2),
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
                "education_value":      CANDIDATE_STAT_BASE_VALUE*2,
                "reputation_value":     CANDIDATE_STAT_BASE_VALUE*(-2),
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE*(4),
                "economy_value":        CANDIDATE_STAT_BASE_VALUE,
                "environment_value":    CANDIDATE_STAT_BASE_VALUE*(-3),
                "welfare_value":        CANDIDATE_STAT_BASE_VALUE*(-1),
                "law_value":            0,

                "education_text":      CANDIDATE_STAT_BASE_VALUE*2,
                "reputation_text":     CANDIDATE_STAT_BASE_VALUE*(-2),
                "infrastructure_text": CANDIDATE_STAT_BASE_VALUE*(4),
                "economy_text":        CANDIDATE_STAT_BASE_VALUE,
                "environment_text":    CANDIDATE_STAT_BASE_VALUE*(-3),
                "welfare_text":        CANDIDATE_STAT_BASE_VALUE*(-1),
                "law_text":            0,
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
                "education_value":      CANDIDATE_STAT_BASE_VALUE*(-2),
                "reputation_value":     CANDIDATE_STAT_BASE_VALUE*4,
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE*(-1),
                "economy_value":        CANDIDATE_STAT_BASE_VALUE*(-1),
                "environment_value":    CANDIDATE_STAT_BASE_VALUE*(-1),
                "welfare_value":        CANDIDATE_STAT_BASE_VALUE,
                "law_value":            CANDIDATE_STAT_BASE_VALUE*2,

                "education_text":       CANDIDATE_STAT_BASE_VALUE*(-2),
                "reputation_text":      CANDIDATE_STAT_BASE_VALUE*4,
                "infrastructure_text":  CANDIDATE_STAT_BASE_VALUE*(-1),
                "economy_text":         CANDIDATE_STAT_BASE_VALUE*(-1),
                "environment_text":     CANDIDATE_STAT_BASE_VALUE*(-1),
                "welfare_text":         CANDIDATE_STAT_BASE_VALUE,
                "law_text":             CANDIDATE_STAT_BASE_VALUE*2,
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
                "education_value":      CANDIDATE_STAT_BASE_VALUE*4,
                "reputation_value":     CANDIDATE_STAT_BASE_VALUE,
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE*(-2),
                "economy_value":        CANDIDATE_STAT_BASE_VALUE*(-3),
                "environment_value":    0,
                "welfare_value":        CANDIDATE_STAT_BASE_VALUE*2,
                "law_value":            CANDIDATE_STAT_BASE_VALUE*(-1),

                "education_text":       CANDIDATE_STAT_BASE_VALUE*4,
                "reputation_text":      CANDIDATE_STAT_BASE_VALUE,
                "infrastructure_text":  CANDIDATE_STAT_BASE_VALUE*(-2),
                "economy_text":         CANDIDATE_STAT_BASE_VALUE*(-3),
                "environment_text":     0,
                "welfare_text":         CANDIDATE_STAT_BASE_VALUE*2,
                "law_text":             CANDIDATE_STAT_BASE_VALUE*(-1),
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
                "education_value":      CANDIDATE_STAT_BASE_VALUE,
                "reputation_value":     CANDIDATE_STAT_BASE_VALUE*(-1),
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE*2,
                "economy_value":        CANDIDATE_STAT_BASE_VALUE*(-2),
                "environment_value": -  CANDIDATE_STAT_BASE_VALUE*(-1),
                "welfare_value":        CANDIDATE_STAT_BASE_VALUE*(-3),
                "law_value":            CANDIDATE_STAT_BASE_VALUE*4,

                "education_text":       CANDIDATE_STAT_BASE_VALUE,
                "reputation_text":      "?",
                "infrastructure_text":  CANDIDATE_STAT_BASE_VALUE*2,
                "economy_text":         CANDIDATE_STAT_BASE_VALUE*(-2),
                "environment_text":     CANDIDATE_STAT_BASE_VALUE*(-1),
                "welfare_text":         CANDIDATE_STAT_BASE_VALUE*(-3),
                "law_text":             CANDIDATE_STAT_BASE_VALUE*4,
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
                "education_value":      CANDIDATE_STAT_BASE_VALUE,
                "reputation_value":     CANDIDATE_STAT_BASE_VALUE*(-2),
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE*2,
                "economy_value":        CANDIDATE_STAT_BASE_VALUE*(-3),
                "environment_value":    CANDIDATE_STAT_BASE_VALUE*4,
                "welfare_value":        CANDIDATE_STAT_BASE_VALUE,
                "law_value":            CANDIDATE_STAT_BASE_VALUE*(-1),

                "education_text":       CANDIDATE_STAT_BASE_VALUE,
                "reputation_text":      CANDIDATE_STAT_BASE_VALUE*(-2),
                "infrastructure_text":  CANDIDATE_STAT_BASE_VALUE*2,
                "economy_text":         CANDIDATE_STAT_BASE_VALUE*(-3),
                "environment_text":     CANDIDATE_STAT_BASE_VALUE*4,
                "welfare_text":         CANDIDATE_STAT_BASE_VALUE,
                "law_text":             CANDIDATE_STAT_BASE_VALUE*(-1),
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
                "education_value":      CANDIDATE_STAT_BASE_VALUE,
                "reputation_value":     CANDIDATE_STAT_BASE_VALUE*(-8),
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE*2,
                "economy_value":        CANDIDATE_STAT_BASE_VALUE*2,
                "environment_value":    CANDIDATE_STAT_BASE_VALUE*(-6),
                "welfare_value":        CANDIDATE_STAT_BASE_VALUE*(-1),
                "law_value":            CANDIDATE_STAT_BASE_VALUE*10,

                "education_text":       CANDIDATE_STAT_BASE_VALUE,
                "reputation_text":      "?",
                "infrastructure_text":  CANDIDATE_STAT_BASE_VALUE*2,
                "economy_text":         CANDIDATE_STAT_BASE_VALUE*2,
                "environment_text":     "?",
                "welfare_text":         CANDIDATE_STAT_BASE_VALUE*(-1),
                "law_text":             CANDIDATE_STAT_BASE_VALUE*10,
            },
            6
        )
    )

    return candidate_list

def general_events():
    pass

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
    leader.updateStory()
    # INC RULING YEARS
    # while game_start:
    #     print("[YEAR:", year, "]")
    #     updateStory(leader.ID)


main()
