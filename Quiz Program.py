#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import random
from datetime import date
import datetime
import matplotlib.pyplot as plt
import os


#it works with the topics as integers and the user input integerised - done

#currently has a bug not allowing 0 to include all topics - done

#sets are deduped and unordered, making them good for comparisons of distinct values...
#...(and just obtaining distinct values from a list)

#quiz to play input needs validating to be in list - done
#topic input validated to be in list - done

#review all while loops to see if they can be smaller (as with title and topic selections)


# In[2]:


# new_row = ["Question","Answer","Topic"]

# new_row_series = pd.Series(new_row, index = records.columns)
# records = records.append(new_row_series, ignore_index=True)

# records.to_csv(f"{records_filepath}",index=False)
            
################################################################
    
# #print("overwriting old records")
# test = pd.DataFrame([["Question1","Answer1","Topic1"]], columns = ["Question","Answer","Topic"])
# #test.to_json("C:/Documents/Python Programs/")
# test.to_csv("C:/Documents/Python Programs/",index=False)


# In[3]:


def initialise_files():
    
    global filepath_prefix
    global quizzes
    global quizzes_idx
    global quiz_titles
    
    filepath_prefix = "C:/Documents/Python Programs/"
    
    if not os.path.exists(f"{filepath_prefix}"):
            os.makedirs(f"{filepath_prefix}")
    
    if True:
        try:
            quizzes = pd.read_csv(f"{filepath_prefix}quizzes.csv")
        except FileNotFoundError:
            
            quizzes = pd.DataFrame([["Red Dwarf", "red dwarf", "red_dwarf_q_a", "red_dwarf_records"],
                                    ["Peep Show", "peep show", "peep_show_q_a", "peep_show_records"]],
                            columns = ["quiz_title", "quiz_title_lower", "q_a_filepath", "records_filepath"])          
            quizzes.to_csv(f"{filepath_prefix}quizzes.csv",index=False)
            
            red_dwarf_q_a = pd.DataFrame(
            [['In which episode does the crew originally get wiped out?', 'The End', 'Series 1'],
             ['In which episode does Lister see that there will be twin boys on Red Dwarf?', 'Future Echoes', 'Series 1'],
             ['In which episode does Lister attempt to become a catering officer?', 'Balance of Power', 'Series 1'],
             ['In which episode does Rimmer recover a pod containing a "Quagaar warrior"?', 'Waiting for God', 'Series 1'],
             ['In which episode does Lister become ill, causing his hallucinations to manifest physically?', 'Confidence and Paranoia', 'Series 1'],
             ['In which episode does Rimmer move in with a duplicate hologram of himself?', 'Me2', 'Series 1'],
             ['In which episode do the crew discover an android looking after three skeletons on the Nova 5?', 'Kryten', 'Series 2'],
             ['In which episode do the crew take part in a total immersion video game?', 'Better Than Life', 'Series 2'],
             ['Which episode features Lise Yates?', 'Thanks for the Memory', 'Series 2'],
             ['In which episode do the crew travel back in time to before the crew were wiped out?', 'Stasis Leak', 'Series 2'],
             ['In which episode is the Red Dwarf taken over by the backup computer?', 'Queeg', 'Series 2'],
             ['In which episode does Lister become pregnant thanks to a female version of himself?', 'Parallel Universe', 'Series 2'],
             ['In which episode do Rimmer and Kryten form a double act?', 'Backwards', 'Series 3'],
             ['In which episode is Lister forced to eat dog food?', 'Marooned', 'Series 3'],
             ['In which episode is Lister attacked by a killer kebab?', 'Polymorph', 'Series 3'],
             ['In which episode does Lister almost blow up Red Dwarf by getting snacks?', 'Bodyswap', 'Series 3'],
             ["In which episode do the crew steal Hitler's briefcase?", 'Timeslides', 'Series 3'],
             ['In which episode does Divadroid try to replace Kryten with Hudson 10?', 'The Last Day', 'Series 3'],
             ["In which episode does Kryten go for a date at Parrot's?", 'Camille', 'Series 4'],
             ['In which episode does Kryten briefly become human?', 'DNA', 'Series 4'],
             ['In which episode does Rimmer get imprisoned for 1,169 counts of manslaughter?', 'Justice', 'Series 4'],
             ['In which episode does Lister play pool with planets?', 'White Hole', 'Series 4'],
             ['In which episode does Ace Rimmer make his first appearance?', 'Dimension Jump', 'Series 4'],
             ['In which episode does Rimmer help Elvis, Einstein and Pythagoras defeat the Nazis?', 'Meltdown', 'Series 4'],
             ['In which episode does Rimmer use a mindpatch?', 'Holoship', 'Series 5'],
             ['In which episode do Lister and Kryten almost get wiped from reality?', 'The Inquisitor', 'Series 5'],
             ['In which episode does Lister get attacked by a "taranshula" that is actually Kryten\'s hand?', 'Terrorform', 'Series 5'],
             ['In which episode does Lister learn to crochet?', 'Quarantine', 'Series 5'],
             ['In which episode does Lister get remote controlled by an evil version of the crew?', 'Demons and Angels', 'Series 5'],
             ['In which episode do the crew encounter the despair squid?', 'Back To Reality', 'Series 5'],
             ['In which episode does Kryten get put in the garbage compactor?', 'Psirens', 'Series 6'],
             ['In which episode does Rimmer gain a hard light drive?', 'Legion', 'Series 6'],
             ['In which episode does Kryten become a Sheriff?', 'Gunmen of the Apocalypse', 'Series 6'],
             ['In which episode does Lister marry a Gelf?', 'Polymorph II - Emohawk', 'Series 6'],
             ['In which episode does Rimmer get some Chinese worry balls?', 'Rimmerworld', 'Series 6'],
             ['In which episode do the crew come into conflict with their future selves?', 'Out of Time', 'Series 6']],
                    columns = ["Question", "Answer", "Topic"])            
            red_dwarf_q_a.to_csv(f"{filepath_prefix}red_dwarf_q_a.csv",index=False)
            
            peep_show_q_a = pd.DataFrame(
            [['In which episode does Mark get bullied by children?', 'Warring Factions', 'Series 1'],
             ['In which episode does Jeremy gurn at his JLB interview?', 'The Interview', 'Series 1'],
             ['In which episode does Mark meet Valerie at a party?', 'On the Pull', 'Series 1'],
             ['In which episode does Mark develop feelings for Alan Johnson?', 'Mark Makes a Friend', 'Series 1'],
             ['In which episode does Jeremy work at a music studio?', 'Dream Job', 'Series 1'],
             ['In which episode does Mark first kiss Sophie?', 'Funeral', 'Series 1'],
             ['In which episode do the flatmates attend Rainbow Rhythms?', 'Dance Class', 'Series 2'],
             ['In which episode does Mark staple a sausage to a door?', 'Jeremy Makes It', 'Series 2'],
             ['In which episode is the flatmates\' "picnic" ruined by cameras?', 'Local Hero', 'Series 2'],
             ['In which episode does Mark stalk a shop assistant?', 'University Challenge', 'Series 2'],
             ['In which episode do Mark and Sophie watch Das Boot?', 'The Man Show', 'Series 2'],
             ['In which episode does Jeremy help Nancy with her visa?', 'Wedding', 'Series 2'],
             ["In which episode does Mark have to use a lady's voice?", 'Mugging', 'Series 3'],
             ['In which episode do Jeremy and Hans start to set up a pub?', 'Sectioning', 'Series 3'],
             ['In which episode is Mark almost forced to poo in a paper bag?', 'Shrooming', 'Series 3'],
             ["In which episode does Jeremy meet Mark's sister?", 'Sisterning', 'Series 3'],
             ['In which episode do the flatmates go to a gay club?', 'Jurying', 'Series 3'],
             ['In which episode do the flatmates get lost on the moors?', 'Quantocking', 'Series 3'],
             ['In which episode does Mark behead a pheasant?', "Sophie's Parents", 'Series 4'],
             ['In which episode does Mark get an angry lapdance?', 'Conference', 'Series 4'],
             ['In which episode does someone poo in a pool?', 'Gym', 'Series 4'],
             ['In which episode do the flatmates visit a safari park?', 'Handyman', 'Series 4'],
             ['In which episode do the flatmates burn a dead dog?', 'Holiday', 'Series 4'],
             ['In which episode does Jeremy pee himself in church?', 'The Wedding', 'Series 4'],
             ['In which episode do the flatmates go on a double date?', 'Burgling', 'Series 5'],
             ['In which episode does Barnie join the band?', 'Spin War', 'Series 5'],
             ['In which episode does Saz move into the flat?', 'Jeremy Broke', 'Series 5'],
             ['In which episode does Gunny appear?', "Jeremy's Mummy", 'Series 5'],
             ['In which episode does Mark smash a crystal skull?', "Jeremy's Manager", 'Series 5'],
             ['In which episode does Mark go LARPing?', "Mark's Women", 'Series 5'],
             ['In which episode does Mark relaunch the satire boom?', 'Jeremy at JLB', 'Series 6'],
             ['In which episode does Mark provide the dips?', 'The Test', 'Series 6'],
             ["In which episode does Mark borrow Jen's laptop?", 'Jeremy in Love', 'Series 6'],
             ["In which episode does Mark start work at Amigo's", 'The Affair', 'Series 6'],
             ['In which episode do the flatmates have a party?', 'The Party', 'Series 6'],
             ['In which episode does Sophie go into labour?', 'Das Boot', 'Series 6']],
                    columns = ["Question", "Answer", "Topic"])
                
            peep_show_q_a.to_csv(f"{filepath_prefix}peep_show_q_a.csv",index=False)
            print('''
            Looks like you're new to the quiz! Generated Red Dwarf and Peep Show data files :)''')
        else:
            quizzes = pd.read_csv(f"{filepath_prefix}quizzes.csv")
        
        quizzes_idx = quizzes.set_index("quiz_title")
        quiz_titles = quizzes["quiz_title"].to_list()


# In[4]:


def import_records(z):
    
    global q_a_filepath
    global records_filepath
    global records
    global quizzes
    global quizzes_idx
    global quiz_titles
    
    quizzes = pd.read_csv(f"{filepath_prefix}quizzes.csv")
    quizzes_idx = quizzes.set_index("quiz_title")
    quiz_titles = quizzes["quiz_title"].to_list()
    
    verb = z
    
    print(f'''
    Which quiz would you like to {z}? (Enter name)
    ''')
    print(*quiz_titles, sep = "\n")
    quiz_choice_lower = input(f'''
    ''').lower()  
    
    while quiz_choice_lower not in list(quizzes["quiz_title_lower"]):
        print('''
        Sorry, that quiz is not available
        Enter a title from the list''')
        quiz_choice_lower = input(f'''
        ''').lower()
        continue
    else:
        pass

    quizzes_cut = quizzes_idx[quizzes_idx["quiz_title_lower"] == quiz_choice_lower]
    quizzes_cut_lower_idx = quizzes_cut.set_index("quiz_title_lower")

    quizzes_q_a_dict = quizzes_cut_lower_idx.to_dict()["q_a_filepath"]
    quizzes_records_dict = quizzes_cut_lower_idx.to_dict()["records_filepath"]

    q_a_filepath_suffix = quizzes_q_a_dict[quiz_choice_lower]
    q_a_filepath = f"{filepath_prefix}{q_a_filepath_suffix}.csv"
    records_filepath_suffix = quizzes_records_dict[quiz_choice_lower]
    records_filepath = f"{filepath_prefix}{records_filepath_suffix}.csv"
    #print(records_filepath)
    
    if True:
        try:
            records = pd.read_csv(f"{records_filepath}")
        except FileNotFoundError:
            #print("")
            if True:
                try:
                    del records
                    #print("deleting other records")
                except NameError:
                    pass
                    #print("no records exist yet, doing nothing")
        else:
            records = pd.read_csv(f"{records_filepath}")
            #print(records)
            #print("reading in old records")
            
    #print(records)


# In[5]:


def play_quiz(x):
    
    global records
    
    name_title = x
    
    verb = "play"
    
    import_records(verb)
    
    #print(f'''
    #I've just run import_records() in play_quiz() and here is the global records variable:
    #''')
    
    #print(records)
    
    quiz_data = pd.read_csv(f"{q_a_filepath}")
    quiz_data_idx = quiz_data.set_index("Question")

    #########################################################################
    # Give topic choice -- cut data accordingly -- create dicts/list/variable
    #########################################################################

    topic_list = list(quiz_data_idx["Topic"])

    topic_list = [str(i) for i in topic_list]
    topic_list = list(dict.fromkeys(topic_list))

    topic_list_lower = [str(i).lower() for i in topic_list]
    topic_list_lower = list(dict.fromkeys(topic_list_lower))

    print(f'''
    Which topic would you like to be quizzed on? (Enter name or 0 for all)
    ''')
    print(*topic_list, sep = "\n")
    subset_choice = input(f'''
    ''').lower()           

    while subset_choice not in topic_list_lower and subset_choice != "0":
        print('''
        Sorry, that topic is not available
        Enter a topic from the list or 0 for all''')
        subset_choice = input(f'''
        ''').lower()
        continue
    else:
        pass

    if subset_choice == "0":
        quiz_data_cut = quiz_data_idx
    else:
        if quiz_data_idx["Topic"].dtypes == "int64":
            quiz_data_cut = quiz_data_idx[quiz_data_idx["Topic"] == int(subset_choice)]
        else:
            quiz_data_cut = quiz_data_idx[quiz_data_idx["Topic"].str.lower() == subset_choice]

    quiz_data_answer_dict = quiz_data_cut.to_dict()["Answer"]
    quiz_data_topic_dict = quiz_data_cut.to_dict()["Topic"]
    question_list = list(quiz_data_answer_dict.keys())
    question_list_count = len(question_list)

    ############################################################################
    # Offer validated quiz length -- define quiz start time -- initialise scores
    ############################################################################

    print(f'''
    How many questions would you like? (1-{question_list_count})''')            

    while True:
        try:
            quiz_length = int(input(f'''
            '''))
        except ValueError or quiz_length < 1 or quiz_length > question_list_count:
            print('''
            Sorry, I didn't understand that''')
            continue
        if quiz_length < 1 or quiz_length > question_list_count:
            print(f'''
            Sorry, the quiz must include 1 to {question_list_count} questions''')
            continue
        else:
            print(f'''
            Excellent! Running {quiz_length} questions''')
            break            

    now = datetime.datetime.now()
    year = now.year
    month = f"{now.month:02d}"
    day = f"{now.day:02d}"
    hour = f"{now.hour:02d}"
    minute = f"{now.minute:02d}"
    second = f"{now.second:02d}"
    quiz_start_time = f"{day}-{month}-{year} {hour}.{minute}.{second}"

    score = 0
    passes = 0
    incorrect = 0

    ######################################################################
    # Run quiz for each question -- determine result and append to records
    ######################################################################

    for n in range(0,quiz_length):
        question = random.choice(question_list)
        del question_list[question_list.index(question)]
        answer = quiz_data_answer_dict[question]
        topic = quiz_data_topic_dict[question]
        
        if isinstance(answer, int):    
            answer_lower = answer
        else:
            answer_lower = answer.lower()
        
        question_no = n+1

        user_answer = input(f'''
        {question_no} of {quiz_length}:
        {question}

        ''')
        
        user_answer_lower = user_answer.lower()

        now_2 = datetime.datetime.now()
        year_2 = now_2.year
        month_2 = f"{now_2.month:02d}"
        day_2 = f"{now_2.day:02d}"
        hour_2 = f"{now_2.hour:02d}"
        minute_2 = f"{now_2.minute:02d}"
        second_2 = f"{now_2.second:02d}"
        answer_time = f"{day_2}-{month_2}-{year_2} {hour_2}.{minute_2}.{second_2}"

        if user_answer_lower == answer_lower:
            print('''
            Correct!''')
            result = "correct"
            score = score + 1
        elif user_answer_lower == "pass":
            print(f'''
            Pass. The answer is {answer}''')
            result = "pass"
            passes = passes + 1         
        else:
            print(f'''
            Incorrect. The answer is {answer}''')
            result = "incorrect"
            incorrect = incorrect + 1

        ##############################################################################
        # Initialise records with first result if non-existent -- or append new result
        ##############################################################################                    

        new_row = [answer_time, name_title, quiz_start_time, subset_choice, question_list_count, quiz_length, 
                   topic, question_no, question, answer, user_answer, result]

        if 'records' in globals():
            #print("appending new records to old")
            new_row_series = pd.Series(new_row, index = records.columns)
            records = records.append(new_row_series, ignore_index=True)
        else:
            #print("overwriting old records")
            records = pd.DataFrame([[answer_time, name_title, quiz_start_time, subset_choice, question_list_count,
            quiz_length, topic, question_no, question, answer, user_answer, result]],
            columns = ["answer_time", "name_title", "quiz_start_time", "subset_choice", "question_list_count",
            "quiz_length", "topic", "question_no", "question", "answer", "user_answer", "result"])
            records.to_csv(f"{records_filepath}",index=False)            

    ######################################################################################
    # Give quiz results -- offer to play again -- write records or skip if quiz not played
    ######################################################################################

    passes_and_incorrect = f"You had {passes} passes and {incorrect} incorrect answers"

    if score == quiz_length:
        print(f'''
        Amazing! You got all {quiz_length} questions right!
        I know what you\'ve been watching during lockdown ;)''')        
    elif score/quiz_length > 0.6:
        print(f'''
        Well done! You scored {score} out of {quiz_length} points!
        {passes_and_incorrect}''')
    elif score/quiz_length > 0.3:
        print(f'''
        Could have been worse! You scored {score} out of {quiz_length} points!
        {passes_and_incorrect}''')
    else:
        print(f'''
        Better luck next time! This time you only scored {score} out of {quiz_length} points!
        {passes_and_incorrect}''')
        
    records.to_csv(f"{records_filepath}",index=False)


# In[6]:


def create_quiz(y):
    
    quizzes = y
    
    new_quiz_title = input(f'''
    What is the title of your new quiz? 
    ''')

    new_quiz_title_lower = new_quiz_title.lower()
    new_quiz_title_lower_ = new_quiz_title_lower.replace(" ", "_")
    new_q_a_filepath = new_quiz_title_lower_ + "_q_a"
    new_records_filepath = new_quiz_title_lower_ + "_records"

    new_quiz_row = [new_quiz_title, new_quiz_title_lower, new_q_a_filepath, new_records_filepath]
    new_quiz_row_series = pd.Series(new_quiz_row, index = quizzes.columns)
    quizzes = quizzes.append(new_quiz_row_series, ignore_index=True)

    quizzes.to_csv(f"{filepath_prefix}quizzes.csv",index=False)

    #####################################################################################
    # Ask for first question -- initialise questions data -- loop through extra questions
    #####################################################################################

    questions_so_far = 0
    another_question_lower = ""

    while another_question_lower != "no" and another_question_lower != "n":
        if questions_so_far == 0 or another_question_lower == "yes" or another_question_lower == "y":
            new_question = input(f'''
            Question: 
            ''')
            new_answer = input(f'''
            Answer: 
            ''')
            new_topic = input(f'''
            Topic: 
            ''')
            if questions_so_far == 0:
                new_question_record = pd.DataFrame([[new_question, new_answer, new_topic]],
                              columns = ["Question", "Answer", "Topic"])
                questions = new_question_record
            else:
                new_question_record = [new_question, new_answer, new_topic]
                new_question_record_series = pd.Series(new_question_record, index = questions.columns)
                questions = questions.append(new_question_record_series, ignore_index=True)
            questions_so_far = questions_so_far + 1        
            another_question_lower = input(f'''
            Would you like to add another question? (Yes/No) ''').lower()  
        else:
            another_question_lower = input(f'''
            Sorry, I didn't understand that
            Would you like to add another question? (Yes/No) ''').lower()  
    else:
        questions.to_csv(f"{filepath_prefix}{new_q_a_filepath}.csv",index=False)


# In[7]:


def plot_records(x):
    
    name_title = x
    
    verb = "view"
    
    import_records(verb)
    
    if True:
        try:
            my_records = records[records["name_title"] == name_title]
        except (UnboundLocalError, NameError):
            print('''
            Records do not exist''')        
        else:
            my_records = records[records["name_title"] == name_title]
            if len(my_records) < 1:
                print('''
                Records do not exist''')
            else:
                print('''
                Here is your all-time summary:''')

                my_correct_records = my_records[my_records["result"] == "correct"]["topic"]
                plt.hist(my_correct_records)
                plt.xlabel("Topic")
                plt.ylabel("Questions")
                plt.title("Correct answers by topic")
                plt.show()

                my_incorrect_or_passed_records = my_records[my_records["result"] != "correct"]["topic"]
                plt.hist(my_incorrect_or_passed_records)
                plt.xlabel("Topic")
                plt.ylabel("Questions")
                plt.title("Incorrect or Passed answers by Topic")
                plt.show()


# In[8]:


def greeting():
    
    name = input("Hi! What\'s your name? ")
    name_title = name.title()
    print(f'''
    Hello {name_title}!''')
    
    initialise_files()
    
    menu = input(f'''
    Would you like to play, view records, create new, edit, or exit?
    ''').lower()
    
    while menu != "exit":
        if menu == "play":
            play_quiz(name_title)
            menu = input(f'''
            Would you like to play, view records, create new, edit, or exit?
            ''').lower()
        elif menu == "view records":
            plot_records(name_title)
            menu = input(f'''
            Would you like to play, view records, create new, edit, or exit?
            ''').lower()
        elif menu == "create new":
            create_quiz(quizzes)
            menu = input(f'''
            Would you like to play, view records, create new, edit, or exit?
            ''').lower()
        elif menu == "edit":
            print(f'''
            Feature not yet available''')
            menu = input(f'''
            Would you like to play, view records, create new, edit, or exit?
            ''').lower()
        else:
            print(f'''
            Sorry, I didn't understand that''')
            menu = input(f'''
            Would you like to play, view records, create new, edit, or exit?
            ''').lower()            
    else:
        pass


# In[ ]:


greeting()

