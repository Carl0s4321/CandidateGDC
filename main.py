answerYes = ["Yes", "Y", "yes", "y"]
answerNo = ["No", "N", "no", "n"]

# CONSTANTS
STATS_BASE_VALUE = 50
POPULATION = 10000
CANDIDATE_STAT_BASE_VALUE = 2

import random

class Country:
    #id of candidate found in the initial list
    current_candidate = 0
    def __init__(self, population, education, reputation, infrastructure, economy, environment, publicWelfare, lawEnforcement):
        self.population = population
        self.education = education
        self.reputation = reputation
        self.infrastructure = infrastructure
        self.economy = economy
        self.environment = environment
        self.publicWelfare = publicWelfare
        self.lawEnforcement = lawEnforcement

def initialize_country():
    country = Country(POPULATION, STATS_BASE_VALUE, STATS_BASE_VALUE, STATS_BASE_VALUE, STATS_BASE_VALUE, STATS_BASE_VALUE, STATS_BASE_VALUE, STATS_BASE_VALUE)
    return country

class Candidate:
    wins = 0
    times_appeared = 0
    #name (string), story (list of strings), portrait (list of strings), stats (dictionary)
    def __init__(self, name, story, portrait, stats):
        self.name = name
        self.story = story
        self.portrait = portrait
        self.stats = stats

#returns a list of Candidates
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
                "education_value": CANDIDATE_STAT_BASE_VALUE*(-3),
                "reputation_value":0,
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE,
                "economy_value": CANDIDATE_STAT_BASE_VALUE*4,
                "environment_value": CANDIDATE_STAT_BASE_VALUE*(-2),
                "welfare_value": CANDIDATE_STAT_BASE_VALUE*(-1),
                "law_value": CANDIDATE_STAT_BASE_VALUE*2,

                "education_text": CANDIDATE_STAT_BASE_VALUE*(-3),
                "reputation_text":0,
                "infrastructure_text": CANDIDATE_STAT_BASE_VALUE,
                "economy_text":CANDIDATE_STAT_BASE_VALUE*4,
                "environment_text":CANDIDATE_STAT_BASE_VALUE*(-2),
                "welfare_text":CANDIDATE_STAT_BASE_VALUE*(-1),
                "law_text": CANDIDATE_STAT_BASE_VALUE*2,
            }
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
                "education_value": CANDIDATE_STAT_BASE_VALUE*2,
                "reputation_value": CANDIDATE_STAT_BASE_VALUE*(-2),
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE*(3),
                "economy_value": CANDIDATE_STAT_BASE_VALUE,
                "environment_value": CANDIDATE_STAT_BASE_VALUE*(-3),
                "welfare_value": CANDIDATE_STAT_BASE_VALUE*(-1),
                "law_value": 0,

                "education_text": CANDIDATE_STAT_BASE_VALUE*2,
                "reputation_text": CANDIDATE_STAT_BASE_VALUE*(-2),
                "infrastructure_text": CANDIDATE_STAT_BASE_VALUE*(3),
                "economy_text": CANDIDATE_STAT_BASE_VALUE,
                "environment_text": CANDIDATE_STAT_BASE_VALUE*(-3),
                "welfare_text": CANDIDATE_STAT_BASE_VALUE*(-1),
                "law_text": 0,
            }
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
                "education_value": CANDIDATE_STAT_BASE_VALUE*(-2),
                "reputation_value": CANDIDATE_STAT_BASE_VALUE*4,
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE*(-1),
                "economy_value": CANDIDATE_STAT_BASE_VALUE*(-1),
                "environment_value": CANDIDATE_STAT_BASE_VALUE*(-1),
                "welfare_value": CANDIDATE_STAT_BASE_VALUE,
                "law_value": CANDIDATE_STAT_BASE_VALUE*2,

                "education_text": CANDIDATE_STAT_BASE_VALUE*(-2),
                "reputation_text": CANDIDATE_STAT_BASE_VALUE*4,
                "infrastructure_text": CANDIDATE_STAT_BASE_VALUE*(-1),
                "economy_text": CANDIDATE_STAT_BASE_VALUE*(-1),
                "environment_text": CANDIDATE_STAT_BASE_VALUE*(-1),
                "welfare_text": CANDIDATE_STAT_BASE_VALUE,
                "law_text": CANDIDATE_STAT_BASE_VALUE*2,
            }
        )
    )
    candidate_list.append(
        Candidate(
            "Connie",
            [
                "       The Educator      ",
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
                "education_value": CANDIDATE_STAT_BASE_VALUE*4,
                "reputation_value": CANDIDATE_STAT_BASE_VALUE,
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE*(-2),
                "economy_value": CANDIDATE_STAT_BASE_VALUE*(-3),
                "environment_value": 0,
                "welfare_value": CANDIDATE_STAT_BASE_VALUE*2,
                "law_value": -CANDIDATE_STAT_BASE_VALUE,

                "education_text": CANDIDATE_STAT_BASE_VALUE*4,
                "reputation_text": CANDIDATE_STAT_BASE_VALUE,
                "infrastructure_text": CANDIDATE_STAT_BASE_VALUE*(-2),
                "economy_text": CANDIDATE_STAT_BASE_VALUE*(-3),
                "environment_text": 0,
                "welfare_text": CANDIDATE_STAT_BASE_VALUE*2,
                "law_text": -CANDIDATE_STAT_BASE_VALUE,
            }
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
                "reputation_value": -CANDIDATE_STAT_BASE_VALUE,
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE*2,
                "economy_value": CANDIDATE_STAT_BASE_VALUE*(-2),
                "environment_value": -CANDIDATE_STAT_BASE_VALUE,
                "welfare_value": CANDIDATE_STAT_BASE_VALUE*(-3),
                "law_value": CANDIDATE_STAT_BASE_VALUE*4,

                "education_text":CANDIDATE_STAT_BASE_VALUE,
                "reputation_text":"?",
                "infrastructure_text": CANDIDATE_STAT_BASE_VALUE*2,
                "economy_text": CANDIDATE_STAT_BASE_VALUE*(-2),
                "environment_text": -CANDIDATE_STAT_BASE_VALUE,
                "welfare_text": CANDIDATE_STAT_BASE_VALUE*(-3),
                "law_text": CANDIDATE_STAT_BASE_VALUE*4,
            }
        )
    )
    candidate_list.append( 
        Candidate(
            "Dianna",
            [
                "  Avid Environmentalist  ",
                "Leader of the Pine Party ",
                "Proposes to install      ",
                "solar panels on every    ",
                "building in the country  ",
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
                "reputation_value": CANDIDATE_STAT_BASE_VALUE*(-2),
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE*2,
                "economy_value": CANDIDATE_STAT_BASE_VALUE*(-3),
                "environment_value": CANDIDATE_STAT_BASE_VALUE*4,
                "welfare_value": CANDIDATE_STAT_BASE_VALUE,
                "law_value": -CANDIDATE_STAT_BASE_VALUE,

                "education_text": CANDIDATE_STAT_BASE_VALUE,
                "reputation_text": CANDIDATE_STAT_BASE_VALUE*(-2),
                "infrastructure_text": CANDIDATE_STAT_BASE_VALUE*2,
                "economy_text": CANDIDATE_STAT_BASE_VALUE*(-3),
                "environment_text": CANDIDATE_STAT_BASE_VALUE*4,
                "welfare_text": CANDIDATE_STAT_BASE_VALUE,
                "law_text": -CANDIDATE_STAT_BASE_VALUE,
            }
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
                "reputation_value": CANDIDATE_STAT_BASE_VALUE*(-8),
                "infrastructure_value": CANDIDATE_STAT_BASE_VALUE*2,
                "economy_value": CANDIDATE_STAT_BASE_VALUE*2,
                "environment_value": CANDIDATE_STAT_BASE_VALUE*(-6),
                "welfare_value": -CANDIDATE_STAT_BASE_VALUE,
                "law_value": CANDIDATE_STAT_BASE_VALUE*10,

                "education_text": CANDIDATE_STAT_BASE_VALUE,
                "reputation_text": CANDIDATE_STAT_BASE_VALUE*(-8),
                "infrastructure_text": CANDIDATE_STAT_BASE_VALUE*2,
                "economy_text": CANDIDATE_STAT_BASE_VALUE*2,
                "environment_text": CANDIDATE_STAT_BASE_VALUE*(-6),
                "welfare_text": CANDIDATE_STAT_BASE_VALUE*(-2),
                "law_text": CANDIDATE_STAT_BASE_VALUE*10,
            }
        )
    )

    return candidate_list

#prints out the candidates horizontally
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
    #insert the text
    display_text = display_text.format(
        #there looks like this could be solved this with a for loop but the format function
        #requires all parameters to be filled
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

    #add more lines to account for the longest story
    for i in range(0, longest_background):
        display_text += "{:<25}|{:<25}|{:<25}|\n"

        story1 = ""
        story2 = ""
        story3 = ""

        if i < len(candidate1.story):
            story1 = candidate1.story[i]

        if i < len(candidate2.story):
            story2 = candidate2.story[i]

        if i < len(candidate1.story):
            story3 = candidate3.story[i]

        display_text = display_text.format(
            story1, story2, story3)

    display_text += "-------------------------|-------------------------|-------------------------|\n"

    stat_names = ["Education:", "Reputation:", "Infrastructure:", "Economy:", "Environment:", "Public Welfare:", "Law Enforcement:"]
    #add lines based on the amount of stats
    for j in range(7, 14):
        display_text += "{:<25}|{:<25}|{:<25}|\n"
        display_text = display_text.format(
            stat_names[j%7] + str(tuple(candidate1.stats.values())[j]),
            stat_names[j%7] + str(tuple(candidate2.stats.values())[j]),
            stat_names[j%7] + str(tuple(candidate3.stats.values())[j]),
            )

    display_text += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    print(display_text)

#returns three candidates that appeared less than others
#(later) always show the candidate that is rerunning
# def get_semi_random_candidates():

#     running_candidates = []
#     return running_candidates

# def candidate_vote(candidate1, candidate2, candidate3):

#     while True:
#         userInput = input("How many votes for ")
#         if userInput in answerYes:
#             print("YES!")
#             break
#         elif userInput in answerNo:
#             print("NO!")
#             break

def main():
    print('''-----------------------------------------------------------------------                                                                                      
  .g8"""bgd `7MMF'MMP""MM""YMM `7MMF'MMM"""AMV `7MM"""YMM  `7MN.   `7MF'
.dP'     `M   MM  P'   MM   `7   MM  M'   AMV    MM    `7    MMN.    M
dM'       `   MM       MM        MM  '   AMV     MM   d      M YMb   M
MM            MM       MM        MM     AMV      MMmmMM      M  `MN. M
MM.           MM       MM        MM    AMV   ,   MM   Y  ,   M   `MM.M
`Mb.     ,'   MM       MM        MM   AMV   ,M   MM     ,M   M     YMM
  `"bmmmd'  .JMML.   .JMML.    .JMML.AMVmmmmMM .JMMmmmmMMM .JML.    YM
----------------...Carlos Sujanto and Jimmy Xu...----------------------''')

    candidate_list = initialize_candidates()

    display_candidates(candidate_list[0], candidate_list[1], candidate_list[2])
    display_candidates(candidate_list[3], candidate_list[4], candidate_list[6])


main()



country = initialize_country()
