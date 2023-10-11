import random

# CONSTANTS
STATS_BASE_VALUE = 50
CANDIDATE_STAT_BASE_VALUE = 2

# GLOBAL VARIABLES
year = 1
population = 10000


class Country:
    # id of candidate found in the initial list

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
        self.current_candidate = -1

    def updateCountryFromLeaderStat(self, added_stat):
        stats = ["education", "reputation", "infrastructure", "economy", "environment", "welfare", "law"]
        for stat in stats:
            setattr(self, stat, getattr(self, stat) + added_stat.get(f"{stat}_value"))

    def updateCountryFromEvent(self, added_stat):
        stats = ["education", "reputation", "infrastructure", "economy", "environment", "welfare", "law"]
        for stat in stats:
            if stat in added_stat:
                setattr(self, stat, getattr(self, stat) + added_stat.get(stat))

    def printCountryStats(self):
        print_separator()
        print("[COUNTRY STATS]")
        print("Population:", self.population)
        print("Education:", self.education)
        print("Reputation:", self.reputation)
        print("Infrastructure:", self.infrastructure)
        print("Economy:", self.economy)
        print("Environment:", self.environment)
        print("Public Welfare:", self.welfare)
        print("Law Enforcement:", self.law)

    #check if a stat is negative
    def check_stat(self):
        stats = ["education", "reputation", "infrastructure", "economy", "environment", "welfare", "law"]
        for stat in stats:
            if getattr(self, stat) < 0:
                return stat
        return ""


def initialize_country():
    country = Country(population, STATS_BASE_VALUE, STATS_BASE_VALUE, STATS_BASE_VALUE, STATS_BASE_VALUE,
                      STATS_BASE_VALUE, STATS_BASE_VALUE, STATS_BASE_VALUE)
    return country


class Candidate:

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
        self.events = all_events.copy()

        self.progress = 0
        self.times_appeared = 0
        self.electionsWon = 0

    def play_event(self, country):
        if(len(self.events) == 0):
            if(len(self.all_events) > 0):
                self.events = self.all_events.copy()
        #make it somewhat random later
        if(len(self.events) > 0):
            random_index = random.randint(0,len(self.events)-1)
            self.events[random_index].display_event(self, country)

            # prevent the event from playing twice until all have been seen
            self.events.pop(random_index)
            # copy the original into the new
            if len(self.events) == 0:
                self.events = self.all_events.copy()


    def updateStory(self, country):
        if self.electionsWon < len(self.story_on_rule):
            print_separator()
            print(self.story_on_rule[self.electionsWon - 1][0])
            country.updateCountryFromEvent(self.story_on_rule[self.electionsWon - 1][1])

    # amount (int)
    def move_to_goal(self, amount, country):
        self.progress += amount
        goal = self.goals[0]

        # if there is enough progress for the goal
        if self.progress > goal.progress_needed:
            print_separator()
            print(goal.story_on_completion)
            goal.add_to_country(country)
            self.goals.pop(0)
            self.progress -= goal.progress_needed

    def check_goal(self):
        if len(self.goals) < 1:
            return True
        else:
            return False


class Goal:

    #                   (int)           (string)  (dict)
    def __init__(self, progress_needed, story, stat_additions):
        self.progress_needed = progress_needed
        self.story_on_completion = story
        self.stats = stat_additions

    def add_to_country(self, country):
        country.updateCountryFromEvent(self.stats)


class Event:

    # decisions (dict{id : list[story_initial, story_final, dict{progress:int, stat1:int, ... , statx:int} ]})
    def __init__(self, story_initial, decisions):
        self.story_initial = story_initial
        self.decisions = decisions

    def display_event(self, candidate, country):
        print_separator()
        print(self.story_initial + "\n")
        for v in self.decisions.values():
            print(v[0])
        self.ask_for_input(candidate, country)

    def ask_for_input(self, candidate, country):
        while True:
            choice = input(">> ")
            if choice in self.decisions:
                decision = self.decisions.get(choice)

                print_whitespace()
                print_separator()
                print(decision[1])

                candidate.move_to_goal(decision[2].get("progress"), country)
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
            # story on rule
            [['''As the Charismatic Businessman is elected, the country moves towards
becoming an economic powerhouse through the power of capitalism. Antonino's
deep pockets allowed him to flood the airwaves with advertisements and
he allows the government to operate like a business. New challenges 
sprout from privatizing certain city services and the increasing divide 
between the rich and poor.
[Economy +3, Public Welfare -2, Infrastructure +2]''',
              {"economy": 3, "welfare": -2, "infrastructure": 2}],  # year 1

             ['''Continuation of economic prosperity, with increased 
job opportunities and GDP growth. Challenges emerge as labor unions 
protest for workers' rights, seeking better wages and working conditions. 
The leader must navigate labor disputes while maintaining economic stability. 
[Economy +5, Public Welfare -3, Law Enforcement -3]''',
              {"economy": 5, "welfare": -3, "law": -3}],  # year 2

             ['''The nation faces environmental backlash as pollution levels rise 
and natural resources are exploited to the point where water becomes 
scarce. Environmental activists organize protests, demanding stricter 
regulations. The Business Tycoon must balance environmental concerns 
with the desire for economic growth. 
[Economy +4, Public Welfare -4, Environment -8, Reputation -4]''',
              {"economy": 4, "welfare": -4, "environment": -8, "reputation": -4}],  # year 3

             ['''Economic challenges hit the nation in the fourth year as global 
market fluctuations lead to a recession. Unemployment rises, and 
protests against economic policies intensify. The Business Tycoon 
faces public unrest while working to stabilize the economy and
bringing water back. 
[Economy -8, Public Welfare -3, Law Enforcement -3, Reputation -2, Environment -5]''',
              {"economy": -8, "welfare": -3, "law": -3, "reputation": -2, "environment": -5}],  # year 4

             ['''The economy has seen growth, but economic disparities persist. 
Environmental concerns remain, and the nation's reputation has 
fluctuated. The leader must decide on their legacy and prepare 
for a smooth transition of power. 
[Economy +2, Public Welfare -2, Environment -3, Reputation +3]''',
              {"economy": 2, "welfare": -2, "environment": -3, "reputation": 3}]],  # year 5
            # goals
            [
                Goal(4, '''The Businessman is able to successfully remove taxes entirely,
this allows people to raise and work for as much capital as they like.
The government on the other hand is forced to operate as a business,
borrowing capital and trading stocks in order to fund projects. City
services are up for competition and the economy is booming!
[Economy + 10] [Law Enforcement - 8] [Environment - 2] ''',
                {"economy":10, "law":-8, "environment":-2} ),
                Goal(4, '''Test''',
                     {"economy":1})
            ],

            # events
            # story_initial,
            # decisions (dict{
            #   id : list[story_initial, story_final, 
            #           dict{progress:int, stat1:int, ... , statx:int} ]})
            [
                Event('''There is competition in the waste management sector, workers are
being laid off and there is no profits to be made and nothing to sell!  
              ''',
                    {
                        "1": [
                            "1) Propose a solution", 
                            '''A solution to the situation was made, people pay the waste management company
similar to how people pay their electric and water bills. 
[Economy + 10] [Public Welfare - 5] [Goal + 2]\n''',
                            {"progress":2, "economy":10, "welfare":-5}
                            ],

                        "2": [
                            "2) It is not my problem",
                            '''Nothing was done, but competitors innovate to make waste management plausible.
[Economy + 2] [Reputation - 2]\n''',
                            {"progress":0, "economy":2, "reputation":-2}
                            ],

                        "3": [
                            "3) Protest",
                            '''Pressure was pushed onto the Businessman and innovated a subscription service
similar to electricity and hydro bills. People found this acceptable.
[Economy + 5] [Reputation + 2] [Public Welfare - 5] [Goal + 1]\n''',
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
            # story on rule
            [['''With the Tech Innovator elected as the leader, the nation 
anticipates a technological revolution. Year one witnesses the launch 
of tech-focused initiatives, stimulating economic growth, improvisation
of science subjects at school, and job creation in the tech sector. 
However, concerns arise about privacy and data security as well as 
a growing digital divide. 
[Economy +2, Infrastructure +2, Public Welfare -1, Education 3]''',
              {"economy": 2, "welfare": -1, "infrastructure": 2, "education": 3}],  # year 1

            ['''Significant technological advancements are made, 
including the rollout of advanced smart city infrastructure. While the 
tech sector thrives, privacy concerns escalate, with data breaches and 
cyberattacks making headlines. Balancing technological progress with 
cyber-security becomes a challenge. 
[Education +3, Infrastructure +5, Public Welfare -2, Law Enforcement -3]''',
              {"education": 3, "infrastructure": 5, "welfare": -2, "law": -3}],  # year 2

             ['''A massive data breach of citizens' personal 
information comes to light, causing widespread security concerns and
public outrage. The leader faces mounting pressure to address the 
breach, protect citizens' data, and hold those responsible 
accountable. Balancing cyber-security and privacy with national 
security becomes a critical challenge. Stricter regulations are 
demanded, and protests intensify. The leader must navigate the 
fallout of the breach while ensuring the nation's security and 
maintaining public trust. 
[Law Enforcement +3, Public Welfare -5, Economy -3, Reputation -8]''',
              {"economy": 3, "environment": -6, "welfare": -3, "reputation": -8}], # year 3

             ['''Public trust in the government erodes further due 
to the fallout from the previous year's data breach. 
Widespread protests erupt, demanding greater transparency, 
data protection, and accountability. Economic challenges 
persist as global market fluctuations lead to a recession, 
impacting the tech sector.
[Economy -5, Law Enforcement -5, Public Welfare -4, Reputation -9]''',
              {"economy": -5, "law": -5, "welfare": -4, "reputation": -9}], # year 4

             ['''While technological progress has been made, 
economic challenges and cyber-security concerns linger. The leader 
must decide on their legacy and prepare for a smooth transition of power. 
Challenges include addressing economic disparities and maintaining 
technological innovation while leaving a lasting legacy. 
[Economy -2, Law Enforcement -3, Public Welfare -2, Reputation -7, Education +3]''',
              {"economy": -2, "law": -3, "welfare": -2, "reputation": -7, "education": 3}]],  # year 5
            # goals
            [
                Goal(4, '''The innovator's influence extends to the introduction of STEM 
education into school curricula, the rapid advancement of AI 
technology, and the deployment of emergency service drones. 
This multifaceted approach reflects their commitment to 
pushing the boundaries of education, technological innovation, 
and public safety. The innovator's vision is reshaping the 
landscape, embracing change, and driving progress across
these critical domains.
[Economy + 5] [Education + 7] [Reputation + 8] [Law enforcement + 6]''',
                     {"economy": 5, "environment": 7, "reputation": 8, "law": 6}),
                Goal(4, '''The leader's achievements encompass the establishment of faster
and more reliable wireless connections, the integration of 
advanced robotics across critical industries, and ambitious 
strides in space exploration. These accomplishments reflect 
a visionary agenda dedicated to enhancing connectivity, 
innovation, and expanding the frontiers of human exploration. 
With a comprehensive approach that spans essential sectors, 
the leader's legacy is shaping a future marked by technological
advancement and cosmic exploration.
[Economy + 7] [Reputation + 4] [Infrastructure + 10] [Welfare + 12]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Under the leadership of the tech innovator, the country thrives as a symbol 
of innovation and unwavering commitment. Citizens embrace a fully automated 
society, where cutting-edge technology drives progress and efficiency, 
reshaping the way they live and work. This visionary approach has transformed 
the nation into a shining example of what can be achieved through technological 
advancement and forward-thinking policies.
                     
                        Technology!
                        [Ending 10 of 16]''',
                     {"economy": 7, "reputation": 4, "infrastructure": 10, "welfare": 12})
            ],
            # events
            [
                Event('''Under the leader's innovative policy, STEM education joins the 
curriculum, sparking a wave of scientific curiosity and technological 
exploration in schools.''',
                      {
                          "1": [
                              "1) Educate yourself in STEM education",
                              '''It's challenging, but interesting...
[Economy - 2] [Reputation + 1] [Education + 2] [Goal + 2]''',
                              {"progress": 2, "economy": -2, "reputation": 1, "education": 2},
                          ],
                          "2": [
                              "2) Money should be used to make better roads!",
                              '''While education holds significance, 
the general public perceives other pressing concerns. Some individuals 
are expressing their beliefs during the board meeting.
[Economy - 2] [Reputation - 1] [Education + 2] [Goal + 1]''',
                              {"progress": 1, "economy": -2, "reputation": -1, "education": -2},
                          ],
                          "3": [
                              "3) Boo! Science is fake!",
                              '''Certain groups are protesting because they 
believe the new policy is a covert means of promoting political agendas 
to their children in schools, prompting the deployment of Law enforcement
to maintain public safety.
[Law Enforcement + 1] [Reputation - 5] [Economy - 1]''',
                              {"progress": 0, "law": 1, "reputation": -5, "economy": -1},
                          ],
                      }
                      ),
                Event('''The rapid advancements in AI have catalyzed a shift 
across industries, compelling many companies to integrate AI technologies 
into their operations. From healthcare to manufacturing, AI's ability to 
automate tasks and analyze large datasets is revolutionizing business 
processes and decision-making. Furthermore, the automotive sector is 
experiencing a transformation, as AI-powered autonomous vehicles emerge 
as a promising solution for safer and more efficient transportation.''',
                      {
                          "1": [
                              "1) AI is AMAZING!",
                              '''You get yourself a shiny new phone with an 
AI assistant, and guess what? It turns out to be super handy, like 
having a buddy in your pocket.
[Economy + 3] [Reputation + 2] [Public Welfare + 1] [Goal + 2]''',
                              {"progress": 2, "economy": 3, "reputation": 2, "welfare": 1},
                          ],
                          "2": [
                              "2) Skeptical",
                              '''AI stuff is moving pretty fast, huh? 
It's got its pros and cons. We'll see how it all pans out...
[Economy + 1] [Environment - 3] [Goal + 1] ''',
                              {"progress": 1, "economy": 1, "environment": -3},
                          ],
                          "3": [
                              "3) Protest, AI is taking over!",
                              '''A large crowd brandishing signs
that read 'THEY TOOK OUR JOBS' is proceeding down the route to 
city hall, with law enforcements personnel positioned along 
the way.
[Law Enforcement + 1] [Reputation -3] [Public Welfare -2] [Goal + 0]''',
                              {"progress": 0, "law": 1, "reputation": -3, "welfare": -2},
                          ]}
                      ),
                Event('''Given the significant progress in AI development, 
the leader suggests incorporating AI into emergency services drones. 
This proposal aims to leverage advanced technology for more 
effective emergency responses.''',
                      {
                          "1": [
                              "1) No more 911 hold times!",
                              '''Considerable funds are invested in 
drone construction, but the faster response times delight the 
populace, resulting in reduced crime rates.
[Law Enforcement 4] [Economy - 5] [Environment - 2] [Reputation + 3] [Goal + 2]''',
                              {"progress": 2, "law": 4, "economy": -5, "reputation": 3, "environment": -2},
                          ],
                          "2": [
                              "2) 'I'm sorry, I didn't quite catch that'",
                              '''You and a bunch of others are pretty 
frustrated because the 911 system just can't seem to get what 
you're saying on those calls. It's seriously annoying, right?
[Economy - 3] [Reputation - 1]''',
                              {"progress": 0, "economy": -3, "reputation": -1},
                          ],
                      }
                      ),
                Event('''The government has begun digging tunnels throughout
the city to install underground fiber connections, aimed at 
boosting wireless speeds. However, this initiative has caused 
significant traffic congestion in the area.''',
                      {
                          "1": [
                              "1) It'll be worth it!",
                              '''Despite the traffic snarls, 
some people are pretty supportive of the government's move to install
those fiber connections in the ground. It's a bit of a hassle now, 
but the promise of faster wireless connections is definitely worth 
it in the long run.
  [Public Welfare - 3] [Reputation + 2] [Environment - 3] [Goal +2]''',
                              {"progress": 2, "welfare": -3, "reputation": 2, "environment": -3},
                          ],
                          "2": [
                              "2) Become a law-abiding citizen",
                              '''Plenty of people are pretty fed up with 
the government causing all this traffic chaos just for faster wireless 
connections. It feels like they could have planned it better to 
minimize the disruption to the people's daily lives. Causing the 
project to be put on hold and traffic is gone.
[Public Welfare + 3] [Reputation + 2] [Environment + 3]''',
                              {"progress": 0, "reputation": 2, "environment": 3, "welfare": 3},
                          ],
                      }
                      ),
                Event('''The production of advanced robotics designed for 
healthcare, industry, and space exploration has surged, resulting 
in heightened operational efficiency. However, this technological 
wave has also sparked concerns as it contributes to job displacement.''',
                      {
                          "1": [
                              "1) Go Markos!",
                              '''Part of the people notice the shift in
job market, however they applaud the government's commitment to advanced
robotics, which will make the country as a beacon of innovation.
[Infrastructure + 1] [Economy + 2] [Environment - 7] [Goal + 2]''',
                              {"progress": 2, "infrastructure": 1, "economy": 2, "environment": -7},
                          ],
                          "2": [
                              "2) WHERE ARE OUR JOBS!",
                              '''Amidst the proposal, a sweeping wave of 
layoffs occurred, instantly depriving thousands of people of 
their livelihoods. The public demands for a change. In response, 
the government swiftly adjusted its policy to narrow its impact 
solely to space exploration.
[Environment + 3] [Reputation - 5] [Infrastructure - 1] [Goal + 1]''',
                              {"progress": 1, "environment": 3, "infrastructure": -1, "reputation": -5},
                          ],
                      }
                      ),
                Event('''The government is pushing forward with a wide-ranging 
space development program, encompassing a Mars base, mining 
operations, and extensive research. This grand undertaking 
seeks to utilize Mars' resources and expand our cosmic 
knowledge. However, objections have arisen, with concerns 
about environmental impacts and resource allocation, 
reflecting the ongoing debate surrounding space 
exploration's balance with earthly needs.''',
                      {
                          "1": [
                              "1) Soon to make alien friends!",
                              '''The idea of extraterrestrial life utterly 
captivates your imagination.
[Economy - 3] [Environment - 2] [Reputation: + 2] [Goal + 2]''',
                              {"progress": 2, "reputation": 2, "economy": -3, "environment": -2},
                          ],
                          "2": [
                              "2) I can see the debris from all the way down here!",
                              '''Numerous trials and errors have characterized 
the government's efforts to send a ship to Mars, with many of these 
attempts resulting in destruction and scattering across the galaxy. 
This has sparked concerns about the safety of potential debris 
returning to Earth in the future.
[Environment - 5] [Reputation + 1] [Economy - 2] [Education + 2] [Goal + 1]''',
                              {"progress": 1, "economy": -2, "reputation": 1, "education": 2, "environment": -5},
                          ],
                          "3": [
                              "3) Fix whats on earth first!",
                              '''The public directs their protests toward issues of 
greater concern, such as healthcare and employment. These demonstrations 
underscore the pressing societal challenges that demand attention. As 
they voice their grievances, the public highlights the need for solutions 
to more immediate and substantial problems.
[Law enforcement - 3] [Reputation - 4] [Economy - 3]''',
                              {"progress": 0, "law": -3, "reputation": -4, "economy": -3},
                          ],
                      }
                      ),
            ],

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
            # story on rule
            [['''Woof woof! Woof! Woof woof woof!
[Education -2, Public Welfare +6, Economy +3, Reputation +7]''',
             {"education": -2, "welfare": 6, "economy": 6, "reputation": 7}], # year 1

            ['''Bark bark bark!
[Law enforcement -10, Environment +4, Education -3]''',
             {"law": -10, "environment": 4, "education": -3}], # year 2

            ['''Ruff!
[Economy -4, Law enforcement -2, infrastructure -7]''',
             {"economy": -4, "law": -2, "infrastructure": -7}], # year 3

             ['''Arf arf! Bark!
[Law enforcement +20, Reputation: +10''',
              {"law": 20, "reputation": 10}], # year 4

             ['''Woof woof! grr... bark!
[Education -10, Economy +6, infrastructure +5, Reputation +10]''',
              {"education": -10, "economy": 6, "infrastructure": 5, "reputation": 10}]], # year 5
            # goals
            [
                Goal(4, '''The leader's successful campaign has resulted in a series of new 
policies, ranging from granting dogs the right to vote, acknowledging 
dogs as equal members of society, and extending support to stray dogs 
and cats. These groundbreaking policies have ignited a wave of both 
enthusiasm and debate within the community, as citizens grapple with 
the far-reaching implications of these unique and inclusive measures. 
The future holds great anticipation for how these policies will shape 
the dynamics of the city and its relationship with its furry residents.
[Reputation + 13] [Public Welfare + 10]''',
                     {"reputation": 13, "welfare": 10}),
                Goal(4, '''The leader's successful incorporation of new policies has resulted 
in a country where dogs play multifaceted roles, including sniffing 
out illegal substances and contraband, conducting medical assessments,
and actively serving in the police force. These innovative approaches 
have not only enhanced security and healthcare but also deepened the 
bond between dogs and humans, creating a harmonious society where their 
unique capabilities are celebrated and valued.
[Reputation + 18] [Education + 11] [Public Welfare + 12]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Under the leadership of the dogs, the country transforms into a harmonious 
haven where canines and humans coexist in perfect synergy. The policies 
implemented by these canine leaders create a society that values and cares 
for its four-legged companions, fostering a unique bond of trust and 
collaboration. In this heartwarming environment, dogs and humans thrive 
together, reflecting a model of unity and mutual support for the rest of 
the world to admire.
                     
                        Bark bark!
                        [Ending 11 of 16]''',
                     {"reputation": 18, "education": 11, "welfare": 12})],
            # events
            [
                Event('''Under the leadership of the Great Sparky, an unprecedented proposal 
has emerged the prospect of granting dogs the right to vote. This unique 
policy has sparked a mix of amusement and curiosity among the citizenry, 
as questions arise about the practicality and implications of such a novel 
idea.''',
                      {
                          "1": [
                              "1) Dogs need to be heard too!",
                              '''You were thrilled to learn about this 
policy and so is your dog!
[Reputation + 3] [Public Welfare +1] [Goal + 2]''',
                              {"progress": 2, "reputation": 3, "welfare": 1},
                          ],
                          "2": [
                              "2) Post in Social Media",
                              '''Despite being a dog person yourself,
you expressed your opinion in Twatter that open dialogue is needed
about potential impact on the electoral process before forming a
firm opinion.
[Reputation + 1] [Education + 2] [Goal + 1]''',
                              {"progress": 1, "reputation": 1, "education": 2},
                          ],
                          "3": [
                              "3) Wake up sheeple!",
                              '''You, along with a group of people strongly
oppose the policy in public, underscoring concerns about its potential 
exploitation solely based on Sparky's adorable appearance. Police
are deployed to keep the peace.
[Law Enforcement + 2] [Reputation - 3]''',
                              {"progress": 0, "law": 2, "reputation": -5},
                          ],
                      }
                      ),
                Event('''Under the leader's latest proposal, dogs are being 
put forward as equal members of our society, sparking a mixture 
of enthusiasm, curiosity, and debate among the populace.''',
                      {
                          "1": [
                              "1) Pop open a champagne",
                              '''In a heartwarming moment, you and your dog 
celebrate the day they become an equal member of society. With
this policy in effect, budget is allocated to fund to manufacture
dog ID cards.
[Reputation + 2] [Economy - 3] [Goal + 2]''',
                              {"progress": 2, "reputation": 2, "economy": -3},
                          ],
                          "2": [
                              "2) Show how ridiculous this policy is",
                              '''A group of citizens decides to stage a mock 
"Dog Election Day" to lampoon the policy of granting dogs 
full societal membership. With tiny voting booths and treats 
used as ballots, dogs are encouraged to cast their "barks" in 
this farcical event.
[Reputation - 3] [Public Welfare + 1]''',
                              {"progress": 0, "welfare": 1, "reputation": -3},
                          ]}
                      ),
                Event('''The leader has decided to introduce a policy that supports 
stray dogs and even extends the same assistance to cats. This 
empathetic move is widely embraced by the community, highlighting 
its inclusive and humane nature.''',
                      {
                          "1": [
                              "1) Good boy!",
                              '''You are happy that more stray dogs are able to be 
taken care of.
[Reputation + 4] [Economy - 7] [Goal + 2]''',
                              {"progress": 2, "economy": -7, "reputation": 4},
                          ],
                          "2": [
                              "2) Attend a community meeting",
                              '''You shared your interest with the group about 
the need for a balanced approach that considers both animal welfare and other
pressing societal needs.
[Economy - 3] [Reputation + 2] [Goal + 1]''',
                              {"progress": 1, "economy": -3, "reputation": 2},
                          ],
                      }
                      ),
                Event('''A groundbreaking proposal is proposed, suggesting that dogs
be trained to detect various medical conditions. This innovative concept 
has ignited excitement and hope among citizens, who foresee the potential 
life-saving benefits of these canine companions.''',
                      {
                          "1": [
                              "1) I'll get better in no time!",
                              '''You feel significantly less apprehensive about clinic 
visits when dogs are responsible for conducting medical assessments. Their 
comforting presence and potential to detect health issues provide a reassuring 
and calming effect, making the experience far more manageable. However it
required a substantial amount of budget allocated to train dogs medical
lessons.
[Public Welfare + 5] [Reputation + 2] [Economy - 10] [Goal +2]''',
                              {"progress": 2, "welfare": 5, "reputation": 2, "economy": -10},
                          ],
                          "2": [
                              "2) Do I have to learn dog language?",
                              '''Concerns have emerged over the language barrier between 
dogs and humans during medical assessments, prompting discussions on effective 
communication protocols. To deal with the matter, dog language schools are established.
[Public Welfare + 3] [Economy - 3] [Education + 5] [Goal + 1]''',
                              {"progress": 1, "welfare": 3, "education": 5, "economy": -3},
                          ],
                          "3": [
                              "3) Allergic to dogs!",
                              '''Protests have arisen from dog-allergic individuals 
concerned about their ability to access medical checkups using canine 
assessors. The leader notices their voices and decide to keep
human doctors.
[Public Welfare + 1] [Reputation + 1] [Economy -2] [Goal + 1]''',
                              {"progress": 1, "reputation": 1, "economy": -2, "welfare": 1},
                          ],
                      }
                      ),
                Event('''Dogs are trained to detect illegal drugs, alcohol, contraband, 
explosives, and more, a measure that promises to bolster security and safety.''',
                      {
                          "1": [
                              "1) I feel safer already!",
                              '''While resources are invested in training dogs, the
peace of mind they provide, assuring your safety during the night, is priceless.. 
[Law enforcement + 4] [Economy - 3] [Environment - 3] [Goal + 2]''',
                              {"progress": 2, "law": 4, "economy": -3, "environment": -3},
                          ],
                          "2": [
                              "2) Protest, protest, protest!",
                              '''Protests have erupted with strong objections to the 
proposal, citing concerns about the inhumane treatment of dogs as they're 
exposed to explosives, weapons, drugs, and other potential dangers.
But now dogs are knowledgeable regarding nation's security.
[Public Welfare - 3] [Economy - 3] [Education + 7]''',
                              {"progress": 0, "welfare": -3, "economy": -3, "education": 7},
                          ],
                      }
                      ),
                Event('''The leader is proposing to have a sufficient number of trained 
dogs available to assist in every police chase, an initiative aimed at enhancing
law enforcement efforts.''',
                      {
                          "1": [
                              "1) The force could use a little hand",
                              '''You receive news that your loyal dog has applied to 
join the forces, however the nearest academy is a 2 hour car ride, enhancing
the need to have more academies.
[Law Enforcement + 4] [Public Welfare - 3] [Goal + 2]''',
                              {"progress": 2, "law": 4, "welfare": -3},
                          ],
                          "2": [
                              "2) Public Speech",
                              '''People challenged the effectiveness and ethics 
of using dogs in this context. Aren't people enough?
[Reputation - 2] [Education + 1]''',
                              {"progress": 0, "reputation": -2, "education": 1},
                          ],
                          "3": [
                              "3) Graffiti",
                              '''You and some people who believe in the same cause
spray graffiti of raising awareness to emphasize potential risks, they're 
seen everywhere around the city.
[Education + 4] [Reputation - 2] [Infrastructure - 1]''',
                              {"progress": 0, "education": 4, "reputation": -2, "infrastructure": -1},
                          ],
                      }
                      ) ],
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
            # story on rule
            [['''With the Education Leader elected as the head of the nation, 
a new era of social progress begins. Year one witnesses the introduction
of policies aimed at improving education, healthcare, and social 
programs. The nation's education system and healthcare services 
receive substantial investments, but concerns about budget 
constraints arise. 
[Education +8, Public Welfare +6, Economy -3, Infrastructure +1]''',
              {"education": 8, "welfare": 6, "economy": -3, "infrastructure": 1}], # year 1

             ['''The second year sees continued investments in education, 
healthcare, and social programs, resulting in improved access 
to quality services. However, managing the increased demand 
for these programs becomes a challenge, leading to concerns 
about efficiency and cost control. 
[Education +7, Public Welfare +5, Economy -5, Infrastructure +1, Reputation: -2]''',
              {"education": 7, "welfare": 5, "economy": -5, "infrastructure": 1, "reputation": -2}], # year 2

             ['''In year three, the focus is on improving healthcare access 
and funding. While healthcare services become more accessible, 
the rising costs strain the budget. The leader must address 
the healthcare funding crisis while maintaining support for
education and social programs. 
[Public Welfare +5, Economy -7, Infrastructure +1]''',
             {"welfare": 5, "economy": -7, "infrastructure": 1}], #year 3

             ['''A devastating pandemic outbreak strikes the nation, 
straining the healthcare system and economy. Hospitals are 
overwhelmed, and unemployment rises as businesses shut down to 
mitigate the spread. Social programs are stretched thin,
and economic challenges mount as a result of the pandemic's impact. 
Balancing public health, economic stability, and social support becomes a complex and urgent challenge.
[Economy -10, Public Welfare -4, Law Enforcement: -3, Reputation -3]''',
              {"economy": -10, "welfare": -4, "reputation": -3, "law": -3}], # year 4

             ['''As the Visionary Leader's term comes to an end in year five, 
the nation reflects on their legacy. While education, healthcare, 
and social programs have improved, the shadow of the recent 
pandemic still looms. Economic challenges persist as the nation 
focuses on recovering from the pandemic's impact.The leader 
must secure a legacy that balances social progress with
economic stability.
[Education +2, Public Welfare +1, Economy -3, Infrastructure -1, Reputation +1]''',
              {"education": 2, "welfare": 1, "economy": -3, "infrastructure": -1, "reputation": 1}]],  # year 5
            # goals
            [
                Goal(4, '''Under this leadership, a suite of policies has been set in motion. 
These include bolstering education through increased school budgets 
and higher pay for hardworking teachers, addressing income inequality 
and housing accessibility, and equipping citizens with financial 
knowledge through education on complex financial topics. The diverse 
range of policies reflects a comprehensive approach to societal improvement.
[Education 13] [Reputation + 10] [Public Welfare + 15]''',
                     {"education": 13, "reputation": 10, "welfare": 15}),
                Goal(4, '''TThe leader has rolled out a trio of impactful policies. Online
healthcare services provide convenient access to medical advice and
prescriptions, while education programs aid prisoner reintegration. 
Furthermore, employment opportunities target the unemployed and 
homeless, fostering societal and economic well-being.
[Reputation + 18] [Education + 11] [Public Welfare + 12]
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Under the educator's guidance, the nation thrives as a hub of education and 
enlightenment. The policies in place ensure that every citizen is well-educated, 
fostering a society of empowered individuals. This commitment to education 
results in a prosperous and knowledgeable population.
                     
                        Genius!
                        [Ending 12 of 16]''',
                     {"reputation": 18, "education": 11, "welfare": 12})],
            # events
            [
                Event('''The education leader suggests higher school budgets 
and increased pay for hardworking teachers, emphasizing a commitment to education 
and teacher recognition.''',
                      {
                          "1": [
                              "1) Volunteer to help",
                              '''With most of the budget allocated to improving 
education, any help is accepted. You offered your time and skills to 
assist schools or teachers, contributing to the improvement of education.
[Reputation + 2] [Economy - 6] [Education + 4] [Goal + 2]''',
                              {"progress": 2, "reputation": 2, "economy": -6, "education": 4},
                          ],
                          "2": [
                              "2) Gather information",
                              '''You asked your friend who is a high school 
teacher regarding the new policy. While it is a much more improved policy,
there are still some areas which could be improved, such as better 
school buildings.
[Reputation + 1] [Economy -2] [Education + 1] [Infrastructure -3] [Goal + 1]''',
                              {"progress": 1, "economy": -2, "reputation": 1, "education": 1, "infrastructure": -3},
                          ]
                      }
                      ),
                Event('''The new policy aims to bolster income support programs 
and increase the availability of affordable housing, addressing economic 
disparities and housing accessibility concerns.''',
                      {
                          "1": [
                              "1) Time to go to RentFester.ca!",
                              '''With the new policy, searching for a better 
living space becomes less of a worry.
[Reputation + 4] [Economy + 1] [Goal + 2]''',
                              {"progress": 2, "reputation": 2, "economy": -3},
                          ],
                          "2": [
                              "2) 'I'm a landlord and I hate low rent prices!'",
                              '''A certain group strongly objects to the policy,
as it poses as threat to their financial interests and investments.
[Reputation - 2] [Economy -1]''',
                              {"progress": 0, "economy": -1, "reputation": -2},
                          ]}
                      ),
                Event('''Focus on offering education on intricate subjects like 
finance, insurance, investments, and taxes. By providing accessible 
education, the policy aims to enhance financial literacy and help 
individuals make informed decisions in their financial lives.''',
                      {
                          "1": [
                              "1) Time to learn!",
                              '''The policy has received widespread praise,
but it came at a significant cost. Hiring highly qualified teachers
from overseas was an expensive necessity to provide top-notch 
education in complex financial subjects.
[Reputation + 5] [Economy - 15] [Goal + 2]''',
                              {"progress": 2, "economy": -15, "reputation": 5},
                          ],
                          "2": [
                              "2) Lower the tax!",
                              '''Due to the hiring of expensive foreign
educators, tax becomes higher in order to cover the cost. Many people
don't agree with this policy and decided to protest. The leader decided
hire only some foreign teachers.
[Economy - 6] [Reputation - 2] [Goal + 1]''',
                              {"progress": 1, "economy": -6, "reputation": -2},
                          ],
                      }
                      ),
                Event('''Online doctors are introduced. They offer instant
medical advice through phone calls or video chats, along with 
prescription delivery from the nearest pharmacy, leading to
easier access of medication''',
                      {
                          "1": [
                              "1) Leave a good review of the service",
                              '''You had a fever and didn't 
know what to do, so you called the service and did as they say,
you were healthy again the next day. However it did cost you money 
to call them.
[Public Welfare + 7] [Reputation + 5] [Economy - 2] [Goal +2]''',
                              {"progress": 2, "welfare": 7, "reputation": 5, "economy": -2},
                          ],
                          "2": [
                              "2) Protest about medication abuse",
                              '''Some people are expressing their concerns
due to the easy process getting a prescription. The leader stepped in
and enforced more strict regulation.
[Reputation + 1] [Economy - 3] [Public Welfare + 2] [Goal + 1]''',
                              {"progress": 1, "welfare": 3, "education": 5, "economy": -3},
                          ],
                          "3": [
                              "3) Do nothing",
                              '''You lay alone in your room as you did nothing.''',
                              {"progress": 0},
                          ],
                      }
                      ),
                Event('''Prioritizing employment opportunities creation for the unemployed 
and homeless population. Providing individuals with a chance to regain 
their economic stability and societal integration. A big allocation of
budget is needed.''',
                      {
                          "1": [
                              "1) Help the homeless",
                              '''While they're learning to self-improve, you helped
them by giving them groceries. This inspired other people to do the
same as well. 
[Reputation + 5] [Economy - 7] [Goal + 2]''',
                              {"progress": 2, "reputation": 5, "economy": -7},
                          ],
                          "2": [
                              "2) Protest",
                              '''Protests have broken out with objections to the 
policy. Critics are primarily concerned about resources allocation,
believing it would be better used in other vital services, such as
law enforcement. The government ignored this.
[Law enforcement -4 ] [Economy - 3] [Goal + 1]''',
                              {"progress": 1, "law": -4, "economy": -3},
                          ],
                      }
                      ),
                Event('''The new policy emphasizes educating prisoners who are willing
to reintegrate into society. While this initiative costs a fortune, it aims to 
provide inmates with educational opportunities, equipping them with skills 
and knowledge to increase their chances of successful reintegration into 
the community upon their release. ''',
                      {
                          "1": [
                              "1) ",
                              '''The inmates are learning their best for the new
world they're about to enter. These programs reduces the likelihood of
re-offending. 
[Law Enforcement + 4] [Public Welfare + 3] [Economy -8] [Goal + 2]''',
                              {"progress": 2, "law": 4, "welfare": 3, "economy": -8},
                          ],
                          "2": [
                              "2) Protest",
                              '''These programs costs a lot, there are more
pressing matters at hand, such as building better roads! 
[Reputation - 2] [Economy - 1][Goal + 1]''',
                              {"progress": 1, "reputation": -2, "economy": -1},
                          ]}
                      )],
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
            # story on rule
            [['''With the Law and Order Advocate elected as the leader, the 
nation anticipates tough crime policies and increased security. 
Year one witnesses the implementation of strict crime measures, 
resulting in a reduction in crime rates. However, concerns arise 
about civil liberties and budget allocations for law enforcement. 
Immigration levels rise, leading to debates about border security. 
[Law Enforcement +7, Economy +1, Public Welfare -2, Education -2, Reputation +1]''',
              {"law": 7, "economy": 1, "welfare": -2, "education": -2, "reputation": 1}],  # year 1

             ['''The second year sees a continued focus on security measures, 
including security-focused infrastructure upgrades. Crime rates 
remain low, but civil liberties concerns intensify. Balancing 
security with personal freedoms becomes a challenge, leading to 
protests and debates.
[Law Enforcement +7, Infrastructure +3, Public Welfare -3, Economy +1, Education -1, Reputation -2]''',
              {"law": 7, "infrastructure": 3, "welfare": -3, "economy": 1, "education": -1, "reputation": -2}],
             # year 2

             ['''The nation is shaken by a devastating terrorist attack, 
stemming from concerns about immigration and weak border control. 
The attack leaves the country in shock, and citizens demand 
answers from their government. Trust in leadership wanes, 
and social tensions rise as some blame immigration policies.
The leader must navigate a deeply divided nation, where
security concerns compete with the need for unity.
[Law Enforcement -10, Infrastructure -5, Public Welfare -5, Economy -3, Reputation -7]''',
              {"law": -10, "infrastructure": -5, "welfare": -5, "economy": -3, "reputation": -7}],  # year 3

             ['''In the wake of the devastating terrorist attack,
year five is marked by a collective effort to rebuild and heal. 
The scars of the attack still linger, but the nation is determined 
to move forward. Citizens come together to support the victims 
and their families, and acts of unity become a symbol of resilience. 
The leader, aware of the importance of fostering unity, 
focuses on policies that promote social cohesion, 
support for those affected by the attack, and rebuilding damaged 
infrastructure. Challenges remain as economic disparities persist, 
but the nation is committed to rebuilding stronger than ever. 
[Infrastructure +4, Public Welfare +3, Economy -2, Law Enforcement +5, Reputation +15]''',
              {"infrastructure": 4, "welfare": 3, "economy": -2, "law": 5, "reputation": 15}],  # year 4

             ['''The Leader's legacy is one of resilience and unity, 
reminding the nation that, even in the face of adversity, they 
can come together to overcome challenges. As the leader's term 
concludes, the nation looks to the future with hope and a 
renewed commitment to a better tomorrow.
[Public Welfare +4, Economy +1, Infrastructure +3, Reputation +15, Law Enforcement +8]''',
              {"welfare": 4, "economy": 1, "infrastructure": 3, "reputation": 15, "law": 8}]],  # year 5
            # goals
            [],
            # events
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
            # story on rule
            [['''With the Environmentalist elected as the leader, the nation 
embarks on a journey toward sustainability.Strict regulations to reduce 
carbon emissions and promote renewable energy. Challenges arise as some 
citizens in energy-dependent industries face job losses, leading to 
protests and economic concerns. 
[Economy -6, Public Welfare -3, Environment +4]''',
{"economy":-6,"welfare":-3,"environment":4}], # year 1

           [ '''As the economy adapts to renewable energy and green technology, 
new jobs are created, but economic disparities persist. The Environmentalist 
faces the challenge of bridging the gap between the growing green sector and 
those affected by declining traditional industries. Meanwhile, opposition to 
the rapid changes intensifies, with some calling for a rollback of policies. 
[Economy +4, Public Welfare -3, Environment +3]''',
              {"economy": 4, "welfare": -3, "environment": 3}],  # year 2

['''The Environmentalist introduces policies to protect natural 
habitats and wildlife. Conservation efforts gain traction, but confrontations 
arise with industries seeking to exploit natural resources. Balancing 
environmental protection with economic interests becomes a major challenge. 
Protests both for and against environmental policies escalate, leading to 
tensions within the nation. 
[Environment +6, Economy -2, Law Enforcement -4]''',
 {"environment":6, "economy":-2, "law":-4}], # year 3

    ['''Despite economic growth, the nation faces fiscal pressures due 
to heavy investments in green infrastructure. Citizens express concerns about 
rising taxes and government spending. The Environmentalist must navigate 
a delicate balance between maintaining economic stability and continuing 
to fund environmental initiatives. Opposition parties grow stronger, 
demanding fiscal responsibility. 
[Economy -5, Reputation -3, Public Welfare -2]''',
{"economy":-5, "reputation":-3, "welfare":-2}], # year 4

['''The nation's commitment to sustainability gains international 
recognition, but it comes with expectations of global leadership in environmental
matters. Balancing international obligations with domestic priorities becomes 
a challenge. The Environmentalist faces pressure to allocate resources to global 
initiatives, which sparks debate and dissent at home. 
[Country's Reputation +5, Economy -3, Public Welfare -2]''', 
{"reputation":5, "economy":-3, "welfare":-2}]], #year 5
            #goals
            [
                Goal(4, '''The Environmentalist is able to install solar panels on every,
single building, reducing electricity costs by more than half. Placing 
planters on the sides of buildings where solar panels cannot fit. The 
summers are less hot and the winters aren't so cold anymore. Her ideals
become reality and people are now seeing the value of the environment.
[Economy + 7] [Environment + 7] [Reputation + 7] ''',
                {"economy":7, "environment":7, "reputation":7} ),
                Goal(4, '''The ambitious goal of redesigning all roads to be underground
allowed significantly improved air quality, reduced noise pollution,
improved aesthetic, increased safety (separating  pedestrians and 
vehicles), reduced road weathering and more space for vegetation or
development.
[Economy + 5] [Environment + 25] [Infrastructure + 15] [Welfare + 10]
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

Under the Environmentalist's lead, the country moves towards self sustaining
prosperity. The lost souls have found themselves living in clean air,
land and water. No longer will they have to fight over money, nor food
take care of the land and the land will take of you. 
                     
                        Defeated Climate Change
                        [Ending 14 of 16]''',
                {"ending":1, "economy":5, "environment":25, "infrastructure":15, "welfare":10} ),
],
            #events
            [
                Event('''A high carbon tax wanted to be implemented to develop the projects
of the Environmentalist. This causes upset in people's lives who
are trying to live normally.''',
                      {
                          "1": [
                              "1) Accept the tax",
                              '''People will be upset in the short run, but it will pay
  off in the long run.
  [Economy - 5] [Reputation - 7] [Environment + 2] [Goal + 2]''',
                              {"progress": 2, "economy": -5, "reputation": -5, "environment": 2},
                          ],
                          "2": [
                              "2) Criticize for a lower tax",
                              '''Finding middle ground between the two parties, a lower
  carbon tax is implemented but for how long?
  [Economy - 2] [Reputation - 2] [Environment + 1] [Goal + 1]''',
                              {"progress": 1, "economy": -2, "reputation": -2, "environment": 1},
                          ],
                          "3": [
                              "3) Protest for no carbon tax",
                              '''The group protests for no carbon tax. The result 
  that was only carbon tax applied to large businesses. The 
  people are satisfied, but businesses have to deal with it.
  [Environment + 1] [Reputation + 1] [Economy - 1]''',
                              {"progress": 0, "economy": -1, "reputation": 1, "environment": 1},
                          ],
                      }
                      ),
                Event('''Garbage is being cleaned, sorted and recycled instead
of being burned. This does not affect the existing blue 
and green bins. There is now new jobs and training for 
this area. And education is going out to help sort out
individuals sort out their own garbage, which will make
the jobs in waste management easier. Additionally sorting
out landfills will slowly make them disappear.''',
                      {
                          "1": [
                              "1) Be educated and sort your trash",
                              '''You follow the initiative of the program and
  other people take notice and follow suit. 
  [Economy + 2] [Environment + 10] [Welfare - 7][Goal + 1]''',
                              {"progress": 1, "economy": 2, "welfare": -7, "environment": 10},
                          ],
                          "2": [
                              "2) If they sort our trash then I don't have too",
                              '''Some people are willing to support the program
  and some are not, surely not because trash is dirty.
  [Environment + 5] [Welfare - 5] [Goal + 1]''',
                              {"progress": 1, "welfare": -5, "environment": 5},
                          ],
                          "3": [
                              "3) Protest, we can't people be exposed to dirty garbage!",
                              '''The protesters are met with a strong message:
  "Why are you protesting against cleaning up your own mess, 
  leaving other people to clean your mess instead!?" 
  the protesters are conflicted, leaving the operation to continue
  [Goal + 1]''',
                              {"progress": 1},
                          ],
                          "4": [
                              "4) Volunteer to sort our the landfill",
                              '''You and a bunch of volunteers grab protective 
  equipment from the sponsoring program and are determined to
  clean out a landfill.  
  [Environment + 15] [Welfare - 15] [Goal + 2]''',
                              {"progress": 2, "environment": 15, "welfare": -15},
                          ],
                      }
                      ),
                Event('''The Environmentalist proposes to cut down livestock
production down to a quarter. Livestock is known to produce
a high amount of carbon dioxide require tons of water and 
have a high ratio of vegetation to flesh ratio. Meat products
are becoming more expensive and harder to acquire.''',
                    {
                        "1": [
                            "1) Change your diet to less meat",
                            '''People starting eating less meat and enjoy the benefits 
of healthy eating. Many livestock farmers are losing
their jobs and some people are not ready to change.
[Economy - 5] [Reputation - 5] [Environment + 10] ''',
                            {"progress":0, "economy":-5, "reputation":-5, "environment":10},
                            ],
                        "2": [
                            "2) Protest with the farmers and meat lovers",
                            '''You are against the change and pressure is put on the
Environmentalist. After careful thinking, she proposes to reduce
the production down to three-quarters. People are somewhat
unhappy, but accept it.
[Economy - 1] [Reputation - 2] [Environment + 5] ''',
                            {"progress":0, "economy":-1, "reputation":-2, "environment":5},
                            ],
                    }
                ),
                Event('''The Environmentalist is making controversial move,
they are making a law to prevent littering and employing
enforcement agents to oversee them, as well as agents to
enforce the sorting of garbage sorting into the proper bins.''',
                    {
                        "1": [
                            "1) Protest against a law for something this simple",
                            '''People band together and protest against laws against 
the enforcement of littering. The citizens feel that this
is restricting their civil freedoms. The proposed alternative
is to allow people to enforce themselves.
[Law Enforcement + 5] [Education + 2] [Environment + 5] ''',
                            {"progress":0, "law":5, "education":2, "environment":5},
                            ],
                        "2": [
                            "2) Become a law-abiding citizen",
                            '''The step forward is to be active, people hold
each other accountable for their actions and a clean
society is becoming closer to reality.
[Law Enforcement + 10] [Reputation - 5] [Environment + 5] [Goal + 1]''',
                            {"progress":1, "reputation":-5, "environment":5, "law":10},
                            ],
                    }
                ),
                Event('''There is now a proposal to install vegetation and planters
on the sides of buildings. This would help improve air quality,
regulate temperatures and manage stormwater. As well as create
jobs for their construction. But has high installation and 
maintenance costs, as well as needing a complex watering system.''',
                    {
                        "1": [
                            "1) Companies should not be forced to have green walls!",
                            '''A critique has been given to the Environmentalist 
to review. The response was that the government will reimburse
companies who implement green walls, thereby rewarding those
who commit to the cause.
[Infrastructure + 5] [Economy - 7] [Environment + 5] [Goal + 1]''',
                            {"progress":1, "infrastructure":5, "economy":-7, "environment":5},
                            ],
                        "2": [
                            "2) Protest against this thing!",
                            '''Plants do not belong on walls and we don't want
creatures burrowing into our buildings either. The
pockets of companies lives another day.
[Economy + 7] [Reputation - 3] ''',
                            {"progress":0, "economy":7, "reputation":-3},
                            ],
                        "3": [
                            "3) Hire someone to make green walls on your house",
                            '''The proposal stated it was buildings and
not houses? Someone could argue that a house is a
building. Anyways your enthusiasm is embodied
and people take notice and want to do the same.  
[Environment + 15] [Infrastructure + 10] [Economy - 15] [Goal + 2]''',
                            {"progress":2, "environment":15, "infrastructure":10, "economy":-15},
                            ],
                    }
                ),
                Event('''There is now a proposal to install solar panels on buildings.
This would increase the amount of clean energy and reduce
electricity bills. As well as increase jobs for installation.
But has high maintenance and cleaning costs, as well as
installation may causes problems on older buildings. ''',
                    {
                        "1": [
                            "1) Protest against installing solar panels!",
                            '''Solar panels are expensive and not worth it!
Some people may not have enough space either and it takes 
time to maintain and clean them. The protest does not 
attract much attention as solar panels are still quite
reasonable.
[Infrastructure + 2] [Economy - 3] [Environment + 5] [Goal + 1]''',
                            {"progress":1, "infrastructure":5, "economy":-3, "environment":2},
                            ],
                        "2": [
                            "2) Get someone to install solar panels",
                            '''You got some solar panels installed and saw that 
your electricity bills got cut in half! You also decide
to spread the good news.
[Environment + 7] [Reputation + 2] [Infrastructure + 3] [Economy + 2] [Goal + 2]''',
                            {"progress":2, "economy":2, "reputation":2, "infrastructure":3, "environment":7},
                            ],
                        "3": [
                            "3) I am too broke to install them.",
                            '''Eventually you will be afford them one day.
But while you sulk, people are installing them and saving
on energy costs.
[Environment + 7] [Infrastructure + 4] [Economy - 1] [Goal + 2]''',
                            {"progress":2, "environment":7, "infrastructure":4, "economy":-1},
                            ],
                    }
                ),
                Event('''A huge proposal is declared, the Environmentalist
plans to redesign the city such that roads are moved underground
many people are conflicted and some are excited.
                      ''',
                    {
                        "1": [
                            "1) Go for it!!! [Consume 30 Economy]",
                            '''Seeing the amount of support from the people,
the Environmentalist initiates the most ambitious project. 
This creates many jobs but requires an immense amount of 
time and capitial. 
[Infrastructure + 15] [Economy - 30] [Environment + 25] [Goal + 4]''',
                            {"progress":4, "infrastructure":15, "economy":-30, "environment":25},
                            ],
                        "2": [
                            "2) Do it slowly and carefully [Consume 15 Economy]",
                            ''' The Environmentalist makes note of the expenses
requirements and attempts to roll out the project
while keeping expenses as low as possible and 
maintaining a reasonable working pace.

[Infrastructure + 7] [Economy - 15] [Environment + 10] [Goal + 2]''',
                            {"progress":2, "infrastructure":7, "economy":-15, "environment":10},
                            ],
                        "3": [
                            "3) Wait we don't have that much money! [Consume 5 Economy]",
                            '''The project will start extremely slowly,
chipping away at a project is the better way than
to do nothing at all.
[Infrastructure + 2] [Economy - 5] [Environment + 2] [Goal + 1]''',
                            {"progress":1, "infrastructure":2, "economy":-5, "environment":2},
                            ],
                    }
                ),

            ],
            
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
            # story on rule
            [['''As the dictator assumes power, the nation quickly witnesses 
the consolidation of their control. Propaganda machines are put to 
work, and military presence in the streets becomes a common sight.
While crime rates plummet due to the iron-fisted rule, public trust 
erodes, and civil liberties are curtailed. The leader's authoritarian 
approach gains them a reputation for ruthlessness. 
[Law Enforcement +15, Public Welfare -7, Economy +4, Education -2, Reputation -25]''',
             {"law": 15, "welfare": -7, "economy": 4, "education": -2, "reputation": -25}], # year 1

             ['''The dictator's regime faces resistance from citizens who 
yearn for freedom. Protests and dissenting voices emerge, leading 
to a harsh crackdown. Law enforcement and military are mobilized 
to suppress opposition, resulting in a further deterioration of 
civil liberties and an even worse reputation on the international 
stage. The economy stagnates due to the stifling atmosphere. 
[Law Enforcement +5, Public Welfare -4, Economy -1, Reputation -5, Infrastructure -6]''',
             {"law": 5, "welfare": -4, "economy": -1, "reputation": -5, "infrastructure": -6}], # year 2

            ['''The nation faces a new crisis as the dictator declares 
war on a neighboring country, citing territorial disputes and 
ideological differences as the cause. The declaration of war 
brings international condemnation, further isolating the 
nation. Military spending escalates, diverting resources 
from essential services. The economy suffers due to the 
strain of war and international sanctions, exacerbating 
poverty and unemployment. Domestic protests persist, 
despite the regime's heavy-handed tactics, as citizens 
bear the burden of conflict. 
[Law Enforcement +9, Public Welfare -5, Economy -7, Reputation -9, Infrastructure -3, Environment -3]''',
              {"law": 9, "welfare": -5, "economy": -7, "reputation": -9, "infrastructure": -3, "environment": -3}],
             # year 3

            ['''The nation bore witness to the profound and devastating 
toll of armed conflict. Profound suffering inflicted on 
the nation. Resources dwindled, the economy plummeted, 
and a refugee crisis emerged. Environmental damage 
from military activities became evident, and 
international isolation deepened with stricter 
sanctions. Protests against the war grew, as citizens 
passionately called for peace.
[Law Enforcement +9, Public Welfare -7, Economy -9, Reputation -5, Infrastructure -5, Environment -7]''',
              {"law": 9, "welfare": -7, "economy": -9, "reputation": -5, "infrastructure": -5, "environment": -7}],
             # year 4

             ['''The nation grappled with the enduring legacy of the 
devastating conflict. The war had left economic ruins, 
scarred the environment, and traumatized the population. 
Eroded civil liberties fueled a longing for normalcy. 
International relations reached an all-time low. 
While the dictator clung to power, their legacy was 
one of turmoil, isolation, and the profound toll of war, 
casting a long shadow over the nation's future and the 
daunting challenges of rebuilding and recovery ahead.
[Law Enforcement +9, Public Welfare -9, Economy -10, Reputation -10, Infrastructure -7, Environment -7]''',
              {"law": 9, "welfare": -9, "economy": -10, "reputation": -10, "infrastructure": -7, "environment": -7}]],
            # year 5
            # goals
            [],
            # events
            [],
            
        )
    )

    return candidate_list

def bad_ending(stat_name):
    if stat_name == "confusion":
        print('''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Citizen are unable to vote and retain a candidate's rule for a certain amount of time.
Some developments are made, but none are able to see the goals through the end. There
is no consistency and thus the lost souls become more lost, who contradict the candidates
they vote for.
                     
                        Defeated by Indecision 
                        [Ending 1 of 16]''')
    elif stat_name == "education":
        print('''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Education is dropping below positive values, the country moves towards misinformation
and increasing conspiracy theories with no grounds. The lost souls are fighting a war
between each other and contemplating reality. Nobody is able to believe anymore else
and the country can no longer be run properly.
                     
                        Defeated by the Uneducated 
                        [Ending 2 of 16]''')
    elif stat_name == "reputation":
        print('''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Reputation is dropping below positive values, the country moves towards lack of trust
toward any leader in this country. Even other countries do not like the leadership
here. One country has decided to assimilate your country into theirs to minimize chaos.
The lost souls who wanted to adopt a new identity for themselves had to use a existing
country's identity just to survive.
                     
                        Defeated by Bad Actors 
                        [Ending 3 of 16]''')
    elif stat_name == "infrastructure":
        print('''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Infrastructure is dropping below positive values, the country moves towards traffic 
jams from endless potholes and cracking roads. Buildings are falling apart and 
electricity and sewage systems are neglected. The lost souls who looked for a new
place to live would be better off starting from scratch than repairing anything else.
                     
                        Defeated by Instability
                        [Ending 4 of 16]''')
    elif stat_name == "economy":
        print('''!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Economy is dropping below positive values, the country encounters a massive economic
depression. Nothing the government does to simulate the economy works. Nobody wants to
hire workers and nobody wants to work. The lost souls who seeked opportunity are now
worried about losing everything.
                     
                        Defeated by Depression
                        [Ending 5 of 16]''')
    elif stat_name == "environment":
        print('''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Environment is dropping below positive values, the country suffers massive heatwaves 
in the summer and extremely frozen temperatures in the winter. Wildfires pop up like 
cockroaches and winters destroy the power grid. The lost souls who wanted to live with
the land are now burned/frostbitten from the results of their actions.

                        Defeated by Mother Nature
                        [Ending 6 of 16]''')
    elif stat_name == "welfare":
        print('''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Public Welfare is dropping below positive values, the country caused a pandemic
from the lack of health within the country. People may be unable to afford basic
needs and live off trash, the healthcare is horrible or the cities are infested
and dirty. The lost souls who wanted to live long lives and prosper are now
contracting dieases and illness and starving.

                        Defeated by the Unhealthy
                        [Ending 7 of 16]''')
    elif stat_name == "law":
        print('''
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

Law Enforcement is dropping below positive values, the country is plunged into
chaos. Where crimes are being commited in broad daylight and everyone is living
for survival of the fittest. Even powerful criminal groups, such as the mafia
are struggling. The lost souls who wanted order and control of their lives are
forced to be anti-social hunters and gatherers.

                        Defeated by Lawlessness 
                        [Ending 8 of 16]''')

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
    while len(running_ids) < 3:
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
        if first_lowest_appearance[1] == -1:
            first_lowest_appearance[0] = candidate_list[i].times_appeared
            first_lowest_appearance[1] = i
        elif second_lowest_appearance[1] == -1:
            second_lowest_appearance[0] = candidate_list[i].times_appeared
            second_lowest_appearance[1] = i

        # check if appeared less
        elif candidate_list[i].times_appeared < first_lowest_appearance[0]:
            first_lowest_appearance[0] = candidate_list[i].times_appeared
            first_lowest_appearance[1] = i
        elif candidate_list[i].times_appeared < second_lowest_appearance[0]:
            second_lowest_appearance[0] = candidate_list[i].times_appeared
            second_lowest_appearance[1] = i

    # increase appearance
    current_candidate.times_appeared = highest_appearance
    candidate_list[first_lowest_appearance[1]].times_appeared += 1
    candidate_list[second_lowest_appearance[1]].times_appeared += 1

    list_of_ids = [current_candidate.id, first_lowest_appearance[1], second_lowest_appearance[1]]
    running_candidates = []
    # randomize order
    while len(list_of_ids) > 0:
        index = random.randint(0, len(list_of_ids) - 1)
        id = list_of_ids[index]
        running_candidates.append(candidate_list[id])
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

    print_whitespace()

    return votes


def doElection(current_candidate, candidate_list):
    print("*************************** VOTE YOUR LEADER *****************************")
    display_list = []
    if year == 1:
        display_list = get_three_random_candidates(candidate_list)
    else:
        display_list = get_semi_random_candidates(current_candidate, candidate_list)
    
    display_candidates(display_list[0], display_list[1], display_list[2])
    votes = candidate_vote(display_list[0], display_list[1], display_list[2])
    for candidate, vote_count in votes.items():
        if vote_count == max(votes.values()):
            print(f"{candidate.name} has won the election with {vote_count} votes!\n")
            candidate.electionsWon += 1
            return candidate

def print_whitespace():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")


def main():
    global year
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

    input("\t\t\t\t\t\tPress Enter to Continue\n")
    candidate_list = initialize_candidates()
    country = initialize_country()

    game_start = True
    while game_start:
        if year % 3 == 1:
            leader = doElection(country.current_candidate, candidate_list)
            country.current_candidate = leader
            leader.updateStory(country)
            country.updateCountryFromLeaderStat(leader.stats)
        else:
            print("[YEAR:", year, "]")
            country.printCountryStats()
            leader.play_event(country)

            negative_stat = country.check_stat()
            if year > 18:
                bad_ending("confusion")
                game_start = False
            elif (negative_stat != "") and (leader.id != 6):
                bad_ending(negative_stat)
                game_start = False
            elif leader.check_goal():
                game_start = False

        # INC YEAR
        year += 1



main()
