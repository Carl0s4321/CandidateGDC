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

    def __init__(self, population, education, reputation, infrastructure, economy, environment, welfare,
                 law):
        self.population = population
        self.education = education
        self.reputation = reputation
        self.infrastructure = infrastructure
        self.economy = economy
        self.environment = environment
        self.welfare = welfare
        self.law = law

    def updateCountryFromLeaderStat(self, added_stat):
        stats = ["education", "reputation", "infrastructure", "economy", "environment", "welfare", "law"]
        for stat in stats:
            setattr(self, stat, getattr(self, stat) + added_stat.get(f"{stat}_value"))

    def updateCountryFromEvent(self, added_stat):
        stats = ["education", "reputation", "infrastructure", "economy", "environment", "welfare", "law"]
        for stat in stats:
            if stat in added_stat:
                setattr(self, stat, getattr(self, stat) + added_stat.get(stat))


def initialize_country():
    country = Country(population, STATS_BASE_VALUE, STATS_BASE_VALUE, STATS_BASE_VALUE, STATS_BASE_VALUE,
                      STATS_BASE_VALUE, STATS_BASE_VALUE, STATS_BASE_VALUE)
    return country


class Candidate:
    id = 0
    rulingYear = 0
    progress = 0
    times_appeared = 0
    story_on_rule = []
    goals = []
    all_events = []
    events = []

    # name (string), story (list of strings), portrait (list of strings), stats (dictionary)
    # story_on_rule (list of strings), goals( list of goals), all_events (list of events)
    def __init__(self, id, name, story, portrait, stats, story_on_rule, goals, all_events):
        self.name = name
        self.story = story
        self.portrait = portrait
        self.stats = stats
        self.id = id

        self.story_on_rule = story_on_rule
        self.goals = goals
        self.all_events = all_events
        self.events = all_events

    def play_event(self, country):
        #make it somewhat random later
        if(len(self.events) > 0):
            self.events[0].display_event(self, country)

    def updateStory(self, country):
        if(self.rulingYear < len(self.story_on_rule)):
            print_separator()
            print(self.story_on_rule[self.rulingYear][0])
            country.updateCountryFromEvent(self.story_on_rule[self.rulingYear][1])
        

    #amount (int)
    def move_to_goal(self, amount):
        self.progress += amount
        goal = self.goals[0]

        #if there is enough progresss for the goal
        if(self.progress > goal.progress_needed):
            print_separator()
            print(goal.story_on_completion)
            self.goals.pop(0)
            self.progress -= goal.progress_needed

            #once all goals are completed
            if(len(self.goals) == 0):
                #provide an ending to game
                pass


class Goal:

    #                   (int)           (string)  (dict)
    def __init__(self, progress_needed, story, stat_additions):
        self.progress_needed = progress_needed
        self.story_on_completion = story
        self.stats = stat_additions

    def add_to_country(self, country):
        country.updateCountryFromEvent(self.stat_additions)


class Event:
    
    #decisions (dict{id : list[story_initial, story_final, dict{progress:int, stat1:int, ... , statx:int} ]})
    def __init__(self, story_initial, decisions):
        self.story_initial = story_initial
        self.decisions = decisions

    def display_event(self, candidate, country):
        print_separator()
        print(self.story_initial)
        for v in self.decisions.values():
            print(v[0])
        self.ask_for_input(candidate, country)

    def ask_for_input(self, candidate, country):
        while True:
            choice = input(">> ")
            if choice in self.decisions:
                decision = self.decisions.get(choice)

                print_separator()
                print(decision[1])

                candidate.move_to_goal(decision[2].get("progress"))

                country.updateCountryFromEvent(decision[2])
                break


                


            



# returns a list of Candidates
def initialize_candidates():
    candidate_list = []

    candidate_list.append(
        Candidate(
            0, "Antonino",
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
            #story on rule
            [['''As the Charismatic Businessman is elected, the country moves towards
becoming an economic powerhouse through the power of capitalism. Antonino's
deep pockets allowed him to flood the airwaves with advertisements and
he allows the government to operate like a business. New challenges 
sprout from privatizing certain city services and the increasing divide 
between the rich and poor.
[Economy +5, Public Welfare -2, Infrastructure +2]
''', {"economy":5, "welfare":-2, "infrastructure":2}],

        ],
            #goals
            [
                Goal(1, '''The Businessman is able to successfully remove taxes entirely,
this allows people to raise and work for as much capital as they like.
The government on the other hand is forced to operate as a business,
borrowing capital and trading stocks in order to fund projects. City
services are up for competition and the economy is booming!
[Economy + 10] [Law Enforcement - 8] [Environment - 2] ''',
                {"economy":10, "law":-8, "environment":-2} ),
                Goal(2, '''Test''',
                     {"economy":1})
            ],

            #events
            #story_initial, 
            #decisions (dict{
            #   id : list[story_initial, story_final, 
            #           dict{progress:int, stat1:int, ... , statx:int} ]})
            [
                Event('''There is competition in the waste management sector, workers are
being layed off and there is no profits to be made and nothing to sell!  
              ''',
                    {
                        "1": [
                            "1) Propose a solution", 
                            '''A solution to the situation was made, people pay the waste management company
similar to how people pay their electric and water bills. 
[Economy + 5] [Public Welfare - 5] [Goal + 1]''',
                            {"progress":1, "economy":5, "welfare":-5}
                            ],

                        "2": [
                            "2) It is not my problem",
                            '''Nothing was done, but competitors innovate to make waste management plausible.
[Economy + 2] [Reputation - 2]''',
                            {"progress":0, "economy":2, "reputation":-2}
                            ],

                        "3": [
                            "3) Protest",
                            '''Pressure was pushed onto the Businessman and innovated a subscription service
similar to electricity and hydro bills. People found this acceptable.
[Economy + 5] [Reputation + 2] [Public Welfare - 5] [Goal + 1]''',
                            {"progress":1, "economy":5, "reputation":2, "welfare":-5}
                            ],
                    }
                ),

            Event('''You spot a police officer accepting bribes from a criminal!''',
                    {
                        "1": [
                            "1) Report the transaction",
                            '''The report was made to the government and was handled internally.
[Law Enforcement - 1]''',
                            {"progress":0, "law":-1},
                            ],
                        "2": [
                            "2) Police officers need money too!",
                            '''Yes, so why don't you become a police officer too?
[Law Enforcement - 5] [Public Welfare - 2] [Economy + 3]''',
                            {"progress":0, "law":-5, "welfare":-2, "economy":3},
                            ],
                        "3" : [
                            "3) Spread on the internet and protest",
                            '''The message spread like wildfire and people are becoming worried about the
safety of the country. People protest to hold the government accountable.
People are now wary of police actions and are taking safety in their own hands.
[Law Enforcement + 1] [Public Welfare - 4]''',
                            {"progress":0, "law":1, "welfare":-4},
                            ]
                    }
                ),
            ]
        )
    )


    candidate_list.append(
        Candidate(
            1, "Markos",
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
            #story on rule
            [],
            #goals
            [],
            #events
            [],
            
        )
    )
    candidate_list.append(
        Candidate(
            2, "Sparky",
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
            #story on rule
            [],
            #goals
            [],
            #events
            [],
        )
    )
    candidate_list.append(
        Candidate(
            3, "Connie",
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
            #story on rule
            [],
            #goals
            [],
            #events
            [],
        )
    )
    candidate_list.append(
        Candidate(
            4, "Biben",
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
            #story on rule
            [],
            #goals
            [],
            #events
            [],
            
        )
    )
    candidate_list.append(
        Candidate(
            5, "Dianna",
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
            #story on rule
            [['''With the Environmentalist elected as the leader, the nation 
embarks on a journey toward sustainability. The first year sees sweeping 
changes, with strict regulations to reduce carbon emissions and promote 
renewable energy. Challenges arise as some citizens in energy-dependent 
industries face job losses, leading to protests and economic concerns. 
[Economy -6, Public Welfare -3, Environment +4]''',
{"economy":-6,"welfare":-3,"environment":4}], #year 1

           [ '''As the economy adapts to renewable energy and green technology, 
new jobs are created, but economic disparities persist. The Environmentalist 
faces the challenge of bridging the gap between the growing green sector and 
those affected by declining traditional industries. Meanwhile, opposition to 
the rapid changes intensifies, with some calling for a rollback of policies. 
[Economy +4, Public Welfare -3, Environment +3]''',
{"economy":4, "welfare":-3, "environment":3}], #year 2

['''The Environmentalist introduces policies to protect natural 
habitats and wildlife. Conservation efforts gain traction, but confrontations 
arise with industries seeking to exploit natural resources. Balancing 
environmental protection with economic interests becomes a major challenge. 
Protests both for and against environmental policies escalate, leading to 
tensions within the nation. 
[Environment +6, Economy -2, Law Enforcement -4]''',
 {"environment":6, "economy":-2, "law":-4}], #year 3

    ['''Despite economic growth, the nation faces fiscal pressures due 
to heavy investments in green infrastructure. Citizens express concerns about 
rising taxes and government spending. The Environmentalist must navigate 
a delicate balance between maintaining economic stability and continuing 
to fund environmental initiatives. Opposition parties grow stronger, 
demanding fiscal responsibility. 
[Economy -5, Country's Reputation -3, Public Welfare -2]''',
{"economy":-5, "reputation":-3, "welfare":-2}], #year 4

['''The nation's commitment to sustainability gains international 
recognition, but it comes with expectations of global leadership in environmental
matters. Balancing international obligations with domestic priorities becomes 
a challenge. The Environmentalist faces pressure to allocate resources to global 
initiatives, which sparks debate and dissent at home. 
[Country's Reputation +5, Economy -3, Public Welfare -2]''', 
{"reputation":5, "economy":-3, "welfare":-2}], #year 5

['''As the Environmentalist leader reaches the midpoint of their term, 
she reflects on her achievements and challenges. The nation stands as a symbol of 
sustainability, but the journey is far from over. The Environmentalist must continue 
to navigate the complexities of the policies and prepare for a smooth transition 
of power in two years. Choosing a successor who shares her vision while 
addressing the concerns of the opposition becomes a critical decision. 
[Country's Reputation +3, Economy +2, Public Welfare +1]''',
{"reputation":3, "economy":2, "welfare":1}], #year 6

['''With the Environmentalist leader's term now in its seventh year, 
the nation faces ongoing challenges. While the transition of power is not imminent, 
the leader must continue to build on the legacy and address unresolved issues. 
Economic stability improves, but public welfare concerns linger. Protests and political
polarization intensify as the nation looks ahead to the upcoming election year. 
[Economy +2, Public Welfare -1, Law Enforcement -2]''',
{"economy":2, "welfare":-1, "law":-2}], #year 7


['''As the Environmentalist leader's term reaches its eighth year, 
the nation stands as a symbol of sustainability. The leader's policies have left a 
lasting impact, with a more sustainable economy and environment. Renewable energy 
is now a cornerstone of the nation's power supply, and conservation efforts have 
preserved natural habitats. However, economic disparities persist, and the 
nation's reputation on the international stage remains a subject of debate. 
The nation looks ahead to its future. 
[Country's Reputation +1, Economy +1, Public Welfare +1]''',
{"reputation":1, "economy":1, "welfare":1}]], #year 8
            #goals
            [],
            #events
            [],
            
        )
    )
    candidate_list.append(
        Candidate(
            6, "Schwarz",
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
            #story on rule
            [],
            #goals
            [],
            #events
            [],
            
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
    
def print_separator():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    

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
    leader.rulingYear += 1
    leader.play_event(country)


    # INC RULING YEARS
    # while game_start:
    #     print("[YEAR:", year, "]")
    #     updateStory(leader.ID)


main()
