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
    id = 0
    wins = 0
    times_appeared = 0
    #name (string), story (list of strings), portrait (list of strings), stats (dictionary)
    def __init__(self, name, story, portrait, stats, id):
        self.name = name
        self.story = story
        self.portrait = portrait
        self.stats = stats
        self.id = id

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
                "infrastructure_value":0,
                "economy_value":0,
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

        if i < len(candidate3.story):
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

#used at the start of the game
def get_three_random_candidates(candidate_list):
    running_ids = set()
    while(len(running_ids) < 3):
        running_ids.add(random.randint(1, len(candidate_list)-1))
    
    running_candidates = []
    for id in running_ids:
        running_candidates.append(candidate_list[id])

    return running_candidates


#returns three candidates that appeared less than others
#always show the current candidate that is rerunning
def get_semi_random_candidates(current_candidate, candidate_list):

    highest_appearance = -1
    #amount of appearances, index of candidate
    first_lowest_appearance = [1000, -1]
    second_lowest_appearance = [1000, -1]

    #starts at 1 to exclude empty candidate
    for i in range(1, len(candidate_list)):
        highest_appearance = max(highest_appearance, candidate_list[i].times_appeared)

        #initialize
        if(first_lowest_appearance[1] == -1):
            first_lowest_appearance[0] = candidate_list[i].times_appeared
            first_lowest_appearance[1] = i
        elif(second_lowest_appearance[1] == -1):
            second_lowest_appearance[0] = candidate_list[i].times_appeared
            second_lowest_appearance[1] = i

        #check if appeared less
        elif(candidate_list[i].times_appeared < first_lowest_appearance[0]):
            first_lowest_appearance[0] = candidate_list[i].times_appeared
            first_lowest_appearance[1] = i
        elif(candidate_list[i].times_appeared < second_lowest_appearance[0]):
            second_lowest_appearance[0] = candidate_list[i].times_appeared
            second_lowest_appearance[1] = i

    #increase appearance
    current_candidate.times_appeared = highest_appearance
    candidate_list[first_lowest_appearance[1]].times_appeared += 1
    candidate_list[second_lowest_appearance[1]].times_appeared += 1

    list_of_ids = [current_candidate.id, first_lowest_appearance[1], second_lowest_appearance[2]]
    running_candidates = []
    #randomize order
    while len(list_of_ids) > 0:
        index = random.randint(0, len(list_of_ids)-1)
        id = list_of_ids[index]
        running_candidates.append[candidate_list[id]]
        list_of_ids.pop(index)

    return running_candidates

def candidate_vote(candidate1, candidate2, candidate3):

    while True:
        userInput = input("How many votes for ")
        if userInput in answerYes:
            print("YES!")
            break
        elif userInput in answerNo:
            print("NO!")
            break

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
    country = initialize_country()
    display_list = get_three_random_candidates(candidate_list)
    display_candidates(display_list[0], display_list[1], display_list[2])


main()




