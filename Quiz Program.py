import numpy as np
from numpy.random import choice
import pandas as pd
import pandasql as ps
import random
from datetime import date
import datetime
import matplotlib.pyplot as plt
import os
from IPython.display import display, HTML

#sets are deduped and unordered, making them good for comparisons of distinct values...
#...(and just obtaining distinct values from a list)

#review all while loops to see if they can be smaller (as with title and topic selections)

def initialise_files(folder):

    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Initialised {folder}")
        print()

    if not os.path.exists(f"{folder}Red Dwarf_q_a.csv"):
        pd.DataFrame(
        [[1, 'In which episode does the crew originally get wiped out?', 'The End', 'Series I'],
         [2, 'In which episode does Lister see that there will be twin boys on Red Dwarf?', 'Future Echoes', 'Series I'],
         [3, 'In which episode does Lister attempt to become a catering officer?', 'Balance of Power', 'Series I'],
         [4, 'In which episode does Rimmer recover a pod containing a "Quagaar warrior"?', 'Waiting for God', 'Series I'],
         [5, 'In which episode does Lister become ill, causing his hallucinations to manifest physically?', 'Confidence and Paranoia', 'Series I'],
         [6, 'In which episode does Rimmer move in with a duplicate hologram of himself?', 'Me2', 'Series I'],
         [7, 'In which episode do the crew discover an android looking after three skeletons on the Nova 5?', 'Kryten', 'Series II'],
         [8, 'In which episode do the crew take part in a total immersion video game?', 'Better Than Life', 'Series II'],
         [9, 'Which episode features Lise Yates?', 'Thanks for the Memory', 'Series II'],
         [10, 'In which episode do the crew travel back in time to before the crew were wiped out?', 'Stasis Leak', 'Series II'],
         [11, 'In which episode is the Red Dwarf taken over by the backup computer?', 'Queeg', 'Series II'],
         [12, 'In which episode does Lister become pregnant thanks to a female version of himself?', 'Parallel Universe', 'Series II'],
         [13, 'In which episode do Rimmer and Kryten form a double act?', 'Backwards', 'Series III'],
         [14, 'In which episode is Lister forced to eat dog food?', 'Marooned', 'Series III'],
         [15, 'In which episode is Lister attacked by a killer kebab?', 'Polymorph', 'Series III'],
         [16, 'In which episode does Lister almost blow up Red Dwarf by getting snacks?', 'Bodyswap', 'Series III'],
         [17, "In which episode do the crew steal Hitler's briefcase?", 'Timeslides', 'Series III'],
         [18, 'In which episode does Divadroid try to replace Kryten with Hudson 10?', 'The Last Day', 'Series III'],
         [19, "In which episode does Kryten go for a date at Parrot's?", 'Camille', 'Series IV'],
         [20, 'In which episode does Kryten briefly become human?', 'DNA', 'Series IV'],
         [21, 'In which episode does Rimmer get imprisoned for 1,169 counts of manslaughter?', 'Justice', 'Series IV'],
         [22, 'In which episode does Lister play pool with planets?', 'White Hole', 'Series IV'],
         [23, 'In which episode does Ace Rimmer make his first appearance?', 'Dimension Jump', 'Series IV'],
         [24, 'In which episode does Rimmer help Elvis, Einstein and Pythagoras defeat the Nazis?', 'Meltdown', 'Series IV'],
         [25, 'In which episode does Rimmer use a mindpatch?', 'Holoship', 'Series V'],
         [26, 'In which episode do Lister and Kryten almost get wiped from reality?', 'The Inquisitor', 'Series V'],
         [27, 'In which episode does Lister get attacked by a "taranshula" that is actually Kryten\'s hand?', 'Terrorform', 'Series V'],
         [28, 'In which episode does Lister learn to crochet?', 'Quarantine', 'Series V'],
         [29, 'In which episode does Lister get remote controlled by an evil version of the crew?', 'Demons and Angels', 'Series V'],
         [30, 'In which episode do the crew encounter the despair squid?', 'Back To Reality', 'Series V'],
         [31, 'In which episode does Kryten get put in the garbage compactor?', 'Psirens', 'Series VI'],
         [32, 'In which episode does Rimmer gain a hard light drive?', 'Legion', 'Series VI'],
         [33, 'In which episode does Kryten become a Sheriff?', 'Gunmen of the Apocalypse', 'Series VI'],
         [34, 'In which episode does Lister marry a Gelf?', 'Polymorph II - Emohawk', 'Series VI'],
         [35, 'In which episode does Rimmer get some Chinese worry balls?', 'Rimmerworld', 'Series VI'],
         [36, 'In which episode do the crew come into conflict with their future selves?', 'Out of Time', 'Series VI'],
         [37, 'In which episode do the crew help assassinate JFK?', 'Tikka to Ride', 'Series VII'],
         [38, 'In which episode does Ace Rimmer return to train his replacement?', 'Stoke Me a Clipper', 'Series VII'],
         [39, "In which episode does Lister discover he's his own father?", 'Ouroboros', 'Series VII'],
         [40, 'In which episode do the crew go crawling through the Starbug vents?', 'Duct Soup', 'Series VII'],
         [41, "In which episode does Lister learn that he's been missing Rimmer?", 'Blue', 'Series VII'],
         [42, "In which episode does Lister's desire for ketchup destroy Kryten's head?", 'Beyond a Joke', 'Series VII'],
         [43, 'In which episode does Lister lose his arm to a virus?', 'Epideme', 'Series VII'],
         [44, 'In which episode do the crew track down the nanobots?', 'Nanarchy', 'Series VII'],
         [45, 'In which episode do the crew arrive on the resurrected Red Dwarf?', 'Back in the Red: Part 1', 'Series VIII'],
         [46, 'In which episode does Rimmer use confidential files to try and become an officer?', 'Back in the Red: Part 2', 'Series VIII'],
         [47, 'In which episode are the crew given a two-year prison sentence?', 'Back in the Red: Part 3', 'Series VIII'],
         [48, 'In which episode do the crew discover a computer that can see the future?', 'Cassandra', 'Series VIII'],
         [49, 'In which episode does Kryten launch a TV station?', 'Krytie TV', 'Series VIII'],
         [50, 'In which episode are Lister and Rimmer sent to the hole?', 'Pete: Part 1', 'Series VIII'],
         [51, 'In which episode do the crew accidentally create a dinosaur?', 'Pete: Part 2', 'Series VIII'],
         [52, 'In which episode does a chameleonic virus nearly destroy the Red Dwarf?', 'Only the Good', 'Series VIII'],
         [53, "In which episode does Rimmer convince his brother he's a Space Corps captain?", 'Trojan', 'Series X'],
         [54, 'In which episode does Lister receive video messages from his "father"?', 'Fathers and Suns', 'Series X'],
         [55, 'In which episode do the crew meet Jesus?', 'Lemons', 'Series X'],
         [56, 'In which episode does Lister get strapped to a groinal exploder?', 'Entangled', 'Series X'],
         [57, 'In which episode does Lister learn he may have been a father?', 'Dear Dave', 'Series X'],
         [58, 'In which episode does Rimmer discover he was adopted?', 'The Beginning', 'Series X'],
         [59, 'In which episode do evil simulants attempt a "Hackneyed old cliche"?', 'Twentica', 'Series XI'],
         [60, 'In which episode do the crew discover a crash caused by a Karma drive?', 'Samsara', 'Series XI'],
         [61, "In which episode do the crew perform a time heist on Lister's kidneys?", 'Give and Take', 'Series XI'],
         [62, 'In which episode does a bio-printed captain promote Rimmer?', 'Officer Rimmer', 'Series XI'],
         [63, 'In which episode do the crew discover a very successful android?', 'Krysis', 'Series XI'],
         [64, 'In which episode does Cat get pregnant?', 'Can of Worms', 'Series XI'],
         [65, 'In which episode does Lister jam with robot Hitler?', 'Cured', 'Series XII'],
         [66, "In which episode do the crew all learn what it's like to be androids?", 'Siliconia', 'Series XII'],
         [67, 'In which episode do the crew get jailed for criticising?', 'Timewave', 'Series XII'],
         [68, 'In which episode do Rimmer and Kryten run for Machine President?', 'Mechocracy', 'Series XII'],
         [69, 'In which episode does Lister pay the price for capitalism?', 'M-Corp', 'Series XII'],
         [70, 'In which episode does Rimmer search for a better universe?', 'Skipper', 'Series XII']],
         columns = ["QID", "Question", "Answer", "Topic"]).to_csv(f"{folder}Red Dwarf_q_a.csv",index=False)

        print(f"Initialised {folder}Red Dwarf_q_a.csv")
        print()

    if not os.path.exists(f"{folder}Peep Show_q_a.csv"):
        peep_show_q_a = pd.DataFrame(
        [[1, 'In which episode does Mark get bullied by children?', 'Warring Factions', 'Series 1'],
         [2, 'In which episode does Jeremy gurn at his JLB interview?', 'The Interview', 'Series 1'],
         [3, 'In which episode does Mark meet Valerie at a party?', 'On the Pull', 'Series 1'],
         [4, 'In which episode does Mark develop feelings for Alan Johnson?', 'Mark Makes a Friend', 'Series 1'],
         [5, 'In which episode does Jeremy work at a music studio?', 'Dream Job', 'Series 1'],
         [6, 'In which episode does Mark first kiss Sophie?', 'Funeral', 'Series 1'],
         [7, 'In which episode do the flatmates attend Rainbow Rhythms?', 'Dance Class', 'Series 2'],
         [8, 'In which episode does Mark staple a sausage to a door?', 'Jeremy Makes It', 'Series 2'],
         [9, 'In which episode is the flatmates\' "picnic" ruined by cameras?', 'Local Hero', 'Series 2'],
         [10, 'In which episode does Mark stalk a shop assistant?', 'University Challenge', 'Series 2'],
         [11, 'In which episode do Mark and Sophie watch Das Boot?', 'The Man Show', 'Series 2'],
         [12, 'In which episode does Jeremy help Nancy with her visa?', 'Wedding', 'Series 2'],
         [13, "In which episode does Mark have to use a lady's voice?", 'Mugging', 'Series 3'],
         [14, 'In which episode do Jeremy and Hans start to set up a pub?', 'Sectioning', 'Series 3'],
         [15, 'In which episode is Mark almost forced to poo in a paper bag?', 'Shrooming', 'Series 3'],
         [16, "In which episode does Jeremy meet Mark's sister?", 'Sisterning', 'Series 3'],
         [17, 'In which episode do the flatmates go to a gay club?', 'Jurying', 'Series 3'],
         [18, 'In which episode do the flatmates get lost on the moors?', 'Quantocking', 'Series 3'],
         [19, 'In which episode does Mark behead a pheasant?', "Sophie's Parents", 'Series 4'],
         [20, 'In which episode does Mark get an angry lapdance?', 'Conference', 'Series 4'],
         [21, 'In which episode does someone poo in a pool?', 'Gym', 'Series 4'],
         [22, 'In which episode do the flatmates visit a safari park?', 'Handyman', 'Series 4'],
         [23, 'In which episode do the flatmates burn a dead dog?', 'Holiday', 'Series 4'],
         [24, 'In which episode does Jeremy pee himself in church?', 'The Wedding', 'Series 4'],
         [25, 'In which episode do the flatmates go on a double date?', 'Burgling', 'Series 5'],
         [26, 'In which episode does Barnie join the band?', 'Spin War', 'Series 5'],
         [27, 'In which episode does Saz move into the flat?', 'Jeremy Broke', 'Series 5'],
         [28, 'In which episode does Gunny appear?', "Jeremy's Mummy", 'Series 5'],
         [29, 'In which episode does Mark smash a crystal skull?', "Jeremy's Manager", 'Series 5'],
         [30, 'In which episode does Mark go LARPing?', "Mark's Women", 'Series 5'],
         [31, 'In which episode does Mark relaunch the satire boom?', 'Jeremy at JLB', 'Series 6'],
         [32, 'In which episode does Mark provide the dips?', 'The Test', 'Series 6'],
         [33, "In which episode does Mark borrow Jen's laptop?", 'Jeremy in Love', 'Series 6'],
         [34, "In which episode does Mark start work at Amigo's", 'The Affair', 'Series 6'],
         [35, 'In which episode do the flatmates have a party?', 'The Party', 'Series 6'],
         [36, 'In which episode does Sophie go into labour?', 'Das Boot', 'Series 6']],
         columns = ["QID", "Question", "Answer", "Topic"]).to_csv(f"{folder}Peep Show_q_a.csv",index=False)

        print(f"Initialised {folder}Peep Show_q_a.csv")
        print()

def add_accents(word):

    accents_dict = {'a1': 'ā', 'a2': 'á', 'a3': 'ǎ', 'a4': 'à', 'e1': 'ē', 'e2': 'é', 'e3': 'ě', 'e4': 'è',
                    'i1': 'ī', 'i2': 'í', 'i3': 'ǐ', 'i4': 'ì', 'o1': 'ō', 'o2': 'ó', 'o3': 'ǒ', 'o4': 'ò',
                    'u1': 'ū', 'u2': 'ú', 'u3': 'ǔ', 'u4': 'ù', 'u5': 'ǖ', 'u6': 'ǘ', 'u7': 'ǚ', 'u8': 'ǜ'}

    for input_string in accents_dict:
        if input_string in word:
            word = word.replace(input_string, accents_dict[input_string])

    return word

def topic_selection(q_a_filepath, sentence, exemption):

    quiz_data = pd.read_csv(f"{q_a_filepath}")

    topic_list = list(dict.fromkeys(quiz_data["Topic"].tolist()))
    topic_num_dict = {i:topic_list[i] for i in range(0, len(topic_list))}
    topic_lower_dict = {z.lower():z for z in topic_list}

    topic_list_series = pd.DataFrame(topic_list, columns=["Topics"])
    display(HTML(topic_list_series.to_html()))

    topic_choice_input = input(f'''
    {sentence}
    ''').lower()

    while True:
        try:
            topic_choice_input = int(topic_choice_input)
            try:
                topic_choice = topic_num_dict[topic_choice_input]
            except:
                topic_choice_input = input(f'''
                Sorry I didn't understand that
                {sentence}
                ''').lower()
                continue
            break
        except:
            if topic_choice_input in topic_lower_dict:
                topic_choice = topic_lower_dict[topic_choice_input]
                break
            elif topic_choice_input == exemption:
                topic_choice = topic_choice_input
                break
            else:
                topic_choice_input = input(f'''
                Sorry I didn't understand that
                {sentence}
                ''').lower()
                continue

    if exemption == "new" and topic_choice == "new":
        topic_choice = input(f'''
        New Topic:
        ''')

    return topic_choice

def import_records(folder, verb):

    global q_a_filepath
    global q_a_filepath_suffix
    global records_filepath

    # quizzes = pd.read_csv(f"{folder}quizzes.csv")

    filenames = next(os.walk(folder), (None, None, []))[2]

    quizzes = pd.DataFrame([{
        'quiz_title'       : x.replace('_q_a.csv',''),
        'quiz_title_lower' : x.replace('_q_a.csv','').lower(),
        'q_a_filepath'     : x.replace('.csv',''),
        'records_filepath' : x.replace('_q_a.csv','_records.csv'),
    } for x in filenames if x[-8:] == '_q_a.csv'])

    # JS 23.04.22 reading the q_a files in the directory could be used to create quizzes (df)
    # This would need to include:
    #   1. quiz_title - q_a_filepath.replace('_q_a',''): 'Red Dwarf'
    #   q_a files (e.g. red_dwarf_q_a) should be remade in capital case (e.g. Red Dwarf_q_a)
    #   2. quiz_title_lower - quiz_title.lower(): 'red dwarf'
    #   3. q_a_filepath - taken straight from q_a file: 'Red Dwarf_q_a'
    #   4. records_filepath - q_a_filepath.replace('_q_a','_records'): 'Red Dwarf_records'

    quizzes_idx = quizzes.set_index("quiz_title")
    quiz_titles = quizzes["quiz_title"].to_list()

    quiz_titles_series = pd.DataFrame(quiz_titles, columns=["Quizzes"])
    quiz_titles_lower = list(quizzes["quiz_title_lower"])

    display(HTML(quiz_titles_series.to_html()))

    quiz_choice_lower = input(f'''
    Which quiz would you like to {verb}? (Enter name)
    ''').lower()

    while quiz_choice_lower not in quiz_titles_lower:

        quiz_choice_lower = input(f'''
        Sorry, that quiz is not available
        Enter a title from the list
        ''').lower()

        continue
    else:
        pass

    quizzes_cut = quizzes_idx[quizzes_idx["quiz_title_lower"] == quiz_choice_lower]
    quizzes_cut_lower_idx = quizzes_cut.set_index("quiz_title_lower")

    quizzes_q_a_dict = quizzes_cut_lower_idx.to_dict()["q_a_filepath"]
    quizzes_records_dict = quizzes_cut_lower_idx.to_dict()["records_filepath"]

    q_a_filepath_suffix = quizzes_q_a_dict[quiz_choice_lower]
    q_a_filepath = f"{folder}{q_a_filepath_suffix}.csv"
    records_filepath_suffix = quizzes_records_dict[quiz_choice_lower]
    records_filepath = f"{folder}{records_filepath_suffix}.csv"
    #print(records_filepath)

    if os.path.exists(records_filepath):
        records = pd.read_csv(records_filepath)
    else:
        records = pd.DataFrame([{
            'answer_time'         : None,
            'name'                : None,
            'quiz_start_time'     : None,
            'subset_choice'       : None,
            'question_list_count' : None,
            'quiz_length'         : None,
            'topic'               : None,
            'question_no'         : None,
            'QID'                 : None,
            'question'            : None,
            'answer'              : None,
            'user_answer'         : None,
            'result'              : None,
        }])

    return records, quizzes, quiz_choice_lower

def get_final_question_list(quiz_data, records, name, quiz_length):

    records = records[records["name"] == name]

    last_records = pd.concat([records[records["QID"] == QID].tail(1) for QID in quiz_data['QID']])
    recent_records = pd.concat([records[records["QID"] == QID].tail(10) for QID in quiz_data['QID']])

    scores = ps.sqldf(f"""

        WITH counts AS (

            SELECT
                quiz_data."QID",
                quiz_data."Question",
                quiz_data."Answer",
                quiz_data."Topic",

                records.name,
                last_records.result AS last_result,

                COUNT(CASE WHEN recent_records.result IN ('incorrect','pass') THEN 1 ELSE NULL END) AS recent_incorrect_pass,
                COUNT(CASE WHEN recent_records.result = 'correct' THEN 1 ELSE NULL END) AS recent_correct,
                COUNT(*) AS recent_total_asked,

                COUNT(CASE WHEN records.result IN ('incorrect','pass') THEN 1 ELSE NULL END) AS incorrect_pass,
                COUNT(CASE WHEN records.result = 'correct' THEN 1 ELSE NULL END) AS correct,
                COUNT(*) AS total_asked

            FROM quiz_data

            LEFT JOIN records ON quiz_data."QID" = records."QID"
            LEFT JOIN recent_records ON quiz_data."QID" = recent_records."QID"
            LEFT JOIN last_records ON quiz_data."QID" = last_records."QID"

            GROUP BY 1,2,3,4,5,6

            ORDER BY 1 ASC

        ),

        rates AS (

            SELECT
                *,

                recent_incorrect_pass / recent_total_asked AS recent_incorrect_pass_rate,
                incorrect_pass / total_asked AS incorrect_pass_rate

            FROM counts

        ),

        ask_chances AS (

            SELECT
                *,

                CASE WHEN total_asked = 0
                     THEN 1000000
                     WHEN last_result IN ('incorrect','pass')
                     THEN 100000
                     WHEN total_asked < 3 OR recent_total_asked = 0
                     THEN 0.05 * (incorrect_pass_rate * incorrect_pass_rate) + 50
                     WHEN total_asked >= 3 AND incorrect_pass_rate > 0 AND recent_total_asked > 0
                     THEN 0.05 * (incorrect_pass_rate * incorrect_pass_rate) + 10
                     WHEN total_asked >= 3 AND incorrect_pass_rate = 0 AND recent_total_asked > 0
                     THEN 10
                     ELSE 10
                     END AS ask_chances

            FROM rates

        )

        SELECT
            *,
            ask_chances / SUM(ask_chances) OVER () AS ask_chances_pct

        FROM ask_chances

    """)

    scores.to_csv('C:/Documents/Python Programs (csv)/scores.csv', index=False)

    final_question_list = list(choice(scores['QID'],
                                      quiz_length,
                                      p = scores['ask_chances_pct'],
                                      replace = False))

    return final_question_list

def play_quiz(folder, name):

    global records
    global topic

    records, quizzes, quiz_choice_lower = import_records(folder, "play")

    play_loops = 0
    play_again = ""

    while play_again not in ["no","n"]:

        if play_loops == 0 or play_again in ["yes","y",""]:

            ##############################################################################################

            quiz_data = pd.read_csv(f"{q_a_filepath}")

            topic_choice = topic_selection(q_a_filepath, "Select a topic (name/no.) or enter all:", "all")

            if topic_choice != 'all':
                quiz_data = quiz_data[quiz_data["Topic"].str.lower() == str(topic_choice).lower()]

            print(quiz_data)

            quiz_data_question_dict = quiz_data.set_index('QID').to_dict()["Question"]
            quiz_data_answer_dict = quiz_data.set_index('QID').to_dict()["Answer"]
            quiz_data_topic_dict = quiz_data.set_index('QID').to_dict()["Topic"]

            question_list_count = quiz_data.shape[0]

            quiz_length_menu = f"How many questions would you like on {topic_choice}? (1-{question_list_count})"

            while True:
                try:
                    quiz_length = int(input(f'''
                    {quiz_length_menu}
                    '''))
                except ValueError or quiz_length < 1 or quiz_length > question_list_count:
                    quiz_length_menu = f'''Sorry, I didn't understand that
                    How many questions would you like on {topic_choice}? (1-{question_list_count})'''
                    continue
                if quiz_length < 1 or quiz_length > question_list_count:
                    quiz_length_menu = f'''Sorry, the quiz must include 1 to {question_list_count} questions
                    How many questions would you like on {topic_choice}?'''
                    continue
                else:
                    print(f'''
                    Excellent! Running {quiz_length} questions''')
                    break

            quiz_start_time = datetime.datetime.now().strftime("%d-%m-%Y %H.%M.%S")

            score = 0
            passes = 0
            incorrect = 0

            final_question_list = get_final_question_list(quiz_data, records, name, quiz_length)

            #########################################################################################################
            # loop through asking and marking each question
            #########################################################################################################

            question_no = 0

            incorrect_pass_table = []

            for QID in final_question_list:

                question = quiz_data_question_dict[QID]
                answer = quiz_data_answer_dict[QID]
                topic = quiz_data_topic_dict[QID]

                if isinstance(answer, int):
                    answer_lower = answer
                else:
                    answer_lower = answer.lower()

                question_no += 1

                user_answer = add_accents(input(f'''
                {question_no} of {quiz_length}:
                {question}

                '''))

                if isinstance(answer, int):
                    try:
                        user_answer_lower = int(user_answer)
                    except:
                        user_answer_lower = user_answer
                else:
                    user_answer_lower = user_answer.lower()

                answer_time = datetime.datetime.now().strftime("%d-%m-%Y %H.%M.%S")

                if user_answer_lower == answer_lower:
                    print('''
                    Correct!''')
                    result = "correct"
                    score += 1
                elif user_answer_lower == "pass":
                    print(f'''
                    Pass. The answer is {answer}''')
                    result = "pass"
                    passes += 1
                else:
                    print(f'''
                    Incorrect. The answer is {answer}''')
                    result = "incorrect"
                    incorrect += 1

                ##############################################################################
                # Initialise records with first result if non-existent -- or append new result
                ##############################################################################

                new_row = {
                    'answer_time'         : answer_time,
                    'name'                : name,
                    'quiz_start_time'     : quiz_start_time,
                    'topic_choice'        : topic_choice,
                    'question_list_count' : question_list_count,
                    'quiz_length'         : quiz_length,
                    'topic'               : topic,
                    'question_no'         : question_no,
                    'QID'                 : QID,
                    'question'            : question,
                    'answer'              : answer,
                    'user_answer'         : user_answer,
                    'result'              : result,
                }

                if 'records' in globals():
                    records = records.to_dict(orient='records')
                    records.append(new_row)
                    records = pd.DataFrame(records)
                else:
                    records = pd.DataFrame([new_row])
                    records.to_csv(f"{records_filepath}",index=False)

                if result in ["incorrect","pass"]:
                    incorrect_pass_row = [question_no, question, answer, result]
                    incorrect_pass_table.append(incorrect_pass_row)

            ######################################################################################
            # Give quiz results -- offer to play again -- write records or skip if quiz not played
            ######################################################################################

            incorrect_pass_df = pd.DataFrame(incorrect_pass_table, columns = ["#","Question","Answer", "Result"])
            incorrect_pass_df = incorrect_pass_df.set_index("#")

            passes_and_incorrect = f"You had {passes} passes and {incorrect} incorrect answers"

            if score == quiz_length:
                print(f'''
                Amazing! You got all {quiz_length} questions right!
                I know what you\'ve been watching during lockdown ;)''')
            elif score/quiz_length > 0.6:
                print(f'''
                Well done! You scored {score} out of {quiz_length} points!
                {passes_and_incorrect}''')
                display(HTML(incorrect_pass_df.to_html()))
            elif score/quiz_length > 0.3:
                print(f'''
                Could have been worse! You scored {score} out of {quiz_length} points!
                {passes_and_incorrect}''')
                display(HTML(incorrect_pass_df.to_html()))
            else:
                print(f'''
                Better luck next time! This time you only scored {score} out of {quiz_length} points!
                {passes_and_incorrect}''')
                display(HTML(incorrect_pass_df.to_html()))

            play_loops += 1

            records.to_csv(f"{records_filepath}",index=False)

            play_again = input(f'''
            Would you like to play again? (Yes/No or Enter for yes)
            ''').lower()

            ##############################################################################################

        else:
            play_again = input(f'''
            Sorry, I didn't understand that
            Would you like to play again?
            ''').lower()
    else:
        records.to_csv(f"{records_filepath}",index=False)

def add_question(new_q_a_filepath, outer_function, records_filepath, folder):

    if outer_function == "edit":
        quiz_data = pd.read_csv(q_a_filepath)
#         print(quiz_data)
#         display(HTML(quiz_data.to_html()))

    questions_so_far = 0
    another_question_lower = ""

    add_question_menu = "Would you like to add another question? (Yes/No or Enter for Yes)"

    while another_question_lower not in ["no","n"]:

        if questions_so_far == 0 or another_question_lower in ["yes","y",""]:

            if outer_function == "new" and questions_so_far == 0:
                new_QID = 1
            else:
                if os.path.exists(records_filepath):
                    new_QID = max(quiz_data['QID'].tolist() + pd.read_csv(records_filepath)['QID'].tolist()) + 1
                else:
                    new_QID = max(quiz_data['QID'].tolist()) + 1

            new_question = add_accents(input(f'''
            Question:
            '''))

            new_answer = add_accents(input(f'''
            Answer:
            '''))

            if questions_so_far == 0 and outer_function == "new":
                new_topic = add_accents(input(f'''
                New Topic:
                '''))
            else:
                new_topic = add_accents(topic_selection(
                    f"{folder}{new_q_a_filepath}.csv",
                    "Topic (select from list or enter new):",
                    "new"))

            new_quiz_data = {
                'QID'      : new_QID,
                'Question' : new_question,
                'Answer'   : new_answer,
                'Topic'    : new_topic,
            }

            if questions_so_far > 0 or outer_function != "new":
                quiz_data = pd.read_csv(f"{folder}{new_q_a_filepath}.csv").to_dict(orient='records')
                quiz_data.append(new_quiz_data)
            else:
                quiz_data = [new_quiz_data]

            quiz_data = pd.DataFrame(quiz_data)
#             print("indexed on QID")
            quiz_data.to_csv(f"{folder}{new_q_a_filepath}.csv",index=False)
#             print("written to csv")

            questions_so_far += 1
            display(HTML(quiz_data.to_html()))
            another_question_lower = input(f'''
            {add_question_menu}
            ''').lower()
        else:
            another_question_lower = input(f'''
            Sorry, I didn't understand that
            {add_question_menu}
            ''').lower()

    quiz_data.to_csv(f"{folder}{new_q_a_filepath}.csv",index=False)

def create_quiz(folder):

    new_quiz_title = add_accents(input(f'''
    What is the title of your new quiz?
    '''))

    new_q_a_filepath = f"{new_quiz_title}_q_a"
    new_records_filepath = f"{new_quiz_title}_records"

    add_question(new_q_a_filepath, "new", new_records_filepath, folder)

def edit_question(q_a_filepath):

    quiz_data = pd.read_csv(q_a_filepath)

    row_edit_menu = "Which row would you like to edit? (Enter QID)"
    field_edit_menu = "Would you like to modify the Question, Answer or Topic?"
    another_edit_menu = "Would you like to make another edit to this row? (Yes/No or Enter for No)"

    index_to_modify = input(f'''
    {row_edit_menu}
    ''')

    while True:
        try:
#             quiz_data.index.tolist().remove(index_to_modify)
            index_to_modify = int(index_to_modify)
            if index_to_modify in quiz_data.index.tolist():
                pass
            else:
                index_to_modify = input(f'''
                Sorry that wasn't possible
                {row_edit_menu}
                ''')
                continue
            row_to_edit = quiz_data[quiz_data.index == index_to_modify]
            row_to_edit = pd.DataFrame(row_to_edit, columns=["Question","Answer","Topic"])
            display(HTML(row_to_edit.to_html()))
            break
        except:
            index_to_modify = input(f'''
            Sorry that wasn't possible
            {row_edit_menu}
            ''')
            continue

    row_modifications_made = 0

    while row_modifications_made == 0 or another_row_modification_lower not in ["no","n",""]:

        if row_modifications_made == 0 or another_row_modification_lower in ["yes","y"]:

            column_to_modify = input(f'''
            {field_edit_menu}
            ''')

            while True:
                if column_to_modify.lower() in ["question","q"]:
                    column = "Question"
                    break
                elif column_to_modify.lower() in ["answer","a"]:
                    column = "Answer"
                    break
                elif column_to_modify.lower() in ["topic","t"]:
                    column = "Topic"
                    break
                else:
                    column_to_modify = input(f'''
                    Sorry, I didn't understand that
                    {field_edit_menu}
                    ''')
            else:
                pass

            if column in ["Question","Answer"]:
                quiz_data.loc[index_to_modify, column] = add_accents(input(f'''
                New {column}
                '''))
            else:
                quiz_data.loc[index_to_modify, column] = add_accents(topic_selection(q_a_filepath, "Select a topic (name/num) or enter new:", "new"))

            #print(quiz_data.loc[index_to_modify, column])

            row_to_edit = quiz_data[quiz_data.index == index_to_modify]

            row_to_edit = pd.DataFrame(row_to_edit, columns=["Question","Answer","Topic"])

            display(HTML(row_to_edit.to_html()))

            quiz_data.to_csv(q_a_filepath, index=False)

            row_modifications_made += 1

            another_row_modification_lower = input(f'''
            {another_edit_menu}
            ''').lower()

        elif another_row_modification_lower in ["no","n"]:
            break

        else:
            another_row_modification_lower = input(f'''
            Sorry I didn't understand that
            {another_edit_menu}
            ''').lower()

    else:
        display(HTML(quiz_data.to_html()))

def remove_question(q_a_filepath):

    quiz_data = pd.read_csv(q_a_filepath)

#     display(HTML(quiz_data.to_html()))

    index_to_remove = input(f'''
    Which question would you like to remove? (Enter row no.)
    ''')

    while True:
        try:
            quiz_data = quiz_data[quiz_data.index != int(index_to_remove)]
            quiz_data.to_csv(q_a_filepath, index=False)
            display(HTML(quiz_data.to_html()))
            print(f'''
            {index_to_remove} removed''')
            break
        except:
            index_to_remove = input(f'''
            Sorry that wasn't possible
            Which question would you like to remove? (Enter row no.)
            ''')
            continue

def edit_quiz(folder):

    records, quizzes, quiz_choice_lower = import_records(folder, "edit")

    quiz_data = pd.read_csv(q_a_filepath)

    display(HTML(quiz_data.to_html()))

    edit_menu = None

    while edit_menu not in ["back","b"]:

        if edit_menu in ["add","a"]:
            add_question(q_a_filepath_suffix, "edit", records_filepath, folder)
        elif edit_menu in ["edit","ed","e"]:
            edit_question(q_a_filepath)
        elif edit_menu in ["remove","r"]:
            remove_question(q_a_filepath)
        elif edit_menu is not None:
            print(f'''
            Sorry, I didn't understand that''')
#         elif edit_menu == "view":
#             display(HTML(pd.read_csv(q_a_filepath).to_html()))

        edit_menu = input(f'''
        "Would you like to add, edit, or remove questions? (Enter back to return)"
        ''').lower()

def plot_records(folder, name):

    records, quizzes, quiz_choice_lower = import_records(folder, "view")

    if True:
        try:
            my_records = records[records["name"] == name]
        except (UnboundLocalError, NameError):
            print('''
            Records do not exist''')
        else:
            my_records = records[records["name"] == name]

            x_values = list(dict.fromkeys(my_records["topic"]))
            quiz_title_series = quizzes[quizzes["quiz_title_lower"] == quiz_choice_lower]["quiz_title"]
            chosen_quiz = list(dict.fromkeys(quiz_title_series))[0]
            #chosen_quiz = chosen_quiz[0]
            if len(my_records) < 1:
                print('''
                Records do not exist''')
            else:
                print(f'''
                Here is {name}'s all-time summary for {chosen_quiz}:''')

                x_values = list(dict.fromkeys(my_records["topic"]))
                x_pos = np.arange(len(x_values))

                bar_width = 0.30
                bar_offset = 0

                for z in ["correct","incorrect","pass"]:

                    y_values = []

                    for x in x_values:
                        my_correct_records = my_records[my_records["result"] == z]
                        my_correct_subject_records = my_correct_records[my_correct_records["topic"] == x]
                        my_correct_subject_records_topic = my_correct_subject_records["topic"]
                        y = 0 + len(my_correct_subject_records_topic)
                        y_values.append(y)

                    print(y_values)
                    plt.bar(x_pos+bar_offset, y_values, width=bar_width, align='edge', alpha=0.5)
                    bar_offset = bar_offset + bar_width

                plt.xlabel("Topic")
                plt.ylabel("Answers")
                plt.xticks(x_pos, x_values)
                plt.title("Correct/Incorrect/Passed answers by topic")
                #plt.legend((rects1[0], rects2[0]), ('Men', 'Women'))
                plt.show()
#                 plt.bar(my_correct_records, height, width=0.8, bottom=None, \*, align='center', data=None, \*\*kwargs)

# alphabetise the x_value list before using in the loop to produce the y_value lists

# give appropriate colours to each series

# add a legend - may require modifying loops so that each set of y_values has a different name, as with (rects1[0], rects2[0])
# "plt.bar(..."" may need assigning to a variable to, with one for each series going into the legend function

def greeting():

    folder = "C:/Documents/Python Programs (csv)/"

    initialise_files(folder)

    name = add_accents(input('''
    Hi! What's your name?
    ''')).title()

    print(f'''
    Hello {name}!''')

    menu = None

    while menu not in ["exit","ex"]:

        if menu in ["play","p"]:
            play_quiz(folder, name)
        elif menu in ["view records","view","v"]:
            plot_records(folder, name)
        elif menu in ["create new","create","c"]:
            create_quiz(folder)
        elif menu in ["edit","ed"]:
            edit_quiz(folder)
        elif menu is not None:
            print(f'''
            Sorry, I didn't understand that''')

        menu = input(f'''
        "Would you like to play, view records, create new, or edit? (Enter exit to quit)"
        ''').lower()

greeting()
