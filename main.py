answerYes = ["Yes", "Y", "yes", "y"]
answerNo = ["No", "N", "no", "n"]

# CONSTANTS
STATS_BASE_VALUE = 50
POPULATION = 10000

class Country:
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
            "Empty",
            [
                "                        ",
            ],
            [
                r"                 ",
                r"                 ",
                r"                 ",
                r"                 ",
                r"                 ",
                r"                 ",
                r"                 ",
                r"                 ",
            ],
            {
                "education_value":0,
                "education_text":"0",

                "reputation_value":0,
                "reputation_text":"0",

                "infrastructure_value":0,
                "infrastructure_text":"0",

                "economy_value":0,
                "economy_text":"0",

                "environment_value": 0,
                "environment_text":"0",

                "health_value":0,
                "health_text":"0",

                "law_value":0,
                "law_text":"?",            
            }
        )
    )
    candidate_list.append( 
        Candidate(
            "Dianna",
            [
                "Avid environmentalist    ",
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
                "education_value":0,
                "education_text":"0",

                "reputation_value":5,
                "reputation_text":"5",

                "infrastructure_value":15,
                "infrastructure_text":"15",

                "economy_value":5,
                "economy_text":"5",

                "environment_value": 50,
                "environment_text":"50",

                "health_value":5,
                "health_text":"5",

                "law_value":0,
                "law_text":"0",            
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
    for j in range(0, 7):
        display_text += "{:<25}|{:<25}|{:<25}|\n"
        display_text = display_text.format(
            stat_names[j] + str(tuple(candidate1.stats.values())[j]), 
            stat_names[j] + str(tuple(candidate2.stats.values())[j]),
            stat_names[j] + str(tuple(candidate3.stats.values())[j]),
            )

    display_text += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

    print(display_text)


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
    display_candidates(candidate_list[0], candidate_list[1], candidate_list[0])


main()

while True:
    userInput = input("Who do you want to vote?\n>>")
    if userInput in answerYes:
        print("YES!")
        break
    elif userInput in answerNo:
        print("NO!")
        break

country = initialize_country()
