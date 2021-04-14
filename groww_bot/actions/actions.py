# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3
import random
import pandas as pd
from fuzzywuzzy import process
import math
# import shlex
import subprocess
# from mycredentials import apikey
import datetime
from rasa_sdk.events import ReminderScheduled
from dateutil import parser


def get_most_matched_cell_info(query, choices, limit=4):
    results = process.extract(query, choices, limit=limit)
    return results


class ConnectionToDatabase:
    def create_connection(db_file):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn


conn = ConnectionToDatabase.create_connection("./database/groww_faqs_db")
df = pd.read_sql_query(f"select * from groww_faqs", conn)


class ActionOnDatabase:
    def select_category_by_slot(conn, slot_name, slot_value):

        matched_supercategory = get_most_matched_cell_info(
            slot_value, df.superCategory)[0][0]

        categories = df.loc[df['superCategory'] ==
                            matched_supercategory, 'category'].unique().tolist()
        for i, category in enumerate(categories):
            categories[i] = category.split("_")[-1]

        if categories:
            if matched_supercategory == "Stocks":
                categories[categories.index("DASHBOARD")] = "HOLDINGS"
            if matched_supercategory == "Mutual Funds":
                categories[categories.index("DASHBOARD")] = "MY INVESTMENTS"
            if matched_supercategory == "FDs":
                categories[categories.index("TO")] = "HOW TO"
                categories[categories.index("ABOUT")] = "ABOUT FDS"
        return categories

    def select_question_tags_by_slot(conn, slot_name, slot_value):
        if slot_value == "HOLDINGS":
            slot_value = "sx_dashboard"
        matched_category = get_most_matched_cell_info(
            slot_value, df.category)[0][0]

        questionTags = df.loc[df['category'] ==
                              matched_category, 'questionTags'].unique().tolist()

        return questionTags

    def select_question_by_questiontag_slot(conn, slot_name, slot_value):
        matched_question_tag = get_most_matched_cell_info(
            slot_value, df.questionTags)[0][0]

        questions = df.loc[df['questionTags'] ==
                           matched_question_tag, 'questionTitle'].unique().tolist()

        return questions

    def get_answertext_for_question(question):
        matched_question_title = get_most_matched_cell_info(
            question, df.questionTitle)[0][0]

        answer = df.loc[df['questionTitle'] ==
                        matched_question_title, 'answerText'].item()
        print(answer)
        # print(answer.isna().values[0])
        # answer.isna().item() == True:
        if answer == "":
            answerText = df.loc[df['questionTitle'] ==
                                matched_question_title, 'answerHtml'].item()
        else:
            answerText = df.loc[df['questionTitle'] ==
                                matched_question_title, 'answerText'].item()
        print(answerText)
        return answerText


class ActionQuerySuperCategory(Action):

    def name(self) -> Text:
        return "action_query_superCategory"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        slot_value = tracker.get_slot("superCategory")
        slot_name = "superCategory"
        print(f"name: {slot_name} value:{slot_value}")
        query_result_categories = ActionOnDatabase.select_category_by_slot(
            conn, slot_name, slot_value)

        buttons = []
        for category in query_result_categories:
            payload = category
            if category == "HOLDINGS":
                payload = "SX_DASHBOARD"
            buttons.append({"title": category, "payload": category})

        dispatcher.utter_message(text="Choose a category", buttons=buttons)

        # dispatcher.utter_message(text=str(query_results))

        return []


class ActionQueryCategory(Action):

    def name(self) -> Text:
        return "action_query_category"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        slot_value = tracker.get_slot("category")
        slot_name = "category"
        print(f"name: {slot_name} value:{slot_value}")

        query_result_question_tags = ActionOnDatabase.select_question_tags_by_slot(
            conn, slot_name, slot_value)

        buttons = []
        for questionTag in query_result_question_tags:
            buttons.append({"title": questionTag, "payload": questionTag})

        dispatcher.utter_message(text="Pick one among below", buttons=buttons)

        # dispatcher.utter_message(text=str(query_results))

        return []


class ActionQueryQuestionTags(Action):

    def name(self) -> Text:
        return "action_query_question_tags"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        slot_value = tracker.get_slot("questionTags")
        slot_name = "questionTags"
        print(f"name: {slot_name} value:{slot_value}")

        query_result_questions = ActionOnDatabase.select_question_by_questiontag_slot(
            conn, slot_name, slot_value)

        buttons = []
        for question in query_result_questions:
            buttons.append({"title": question, "payload": question})

        dispatcher.utter_message(
            text="Select your question please", buttons=buttons)

        # dispatcher.utter_message(text=str(query_results))

        return []


class ActionQueryQuestion(Action):

    def name(self) -> Text:
        return "action_query_question"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_question = str((tracker.latest_message)['text'])
        print(user_question)
        answer_text = ActionOnDatabase.get_answertext_for_question(
            user_question)
        dispatcher.utter_message(
            text=answer_text)

        # dispatcher.utter_message(text=str(query_results))

        return []


class ActionUpdateDatabase(Action):

    def name(self) -> Text:
        return "action_update_database"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print("updating db")

        # cmd = f'''curl -F apikey="{apikey}" -F dbowner="amoghaks" -F dbname="faqsdbtest" https://api.dbhub.io/v1/download --output ./database/faqsdbtest ; fuser -k 5055/tcp ; fuser -k 5005/tcp; sleep 2s; . /home/amogh/.local/share/virtualenvs/rasaproject_2-o3mr33AT/bin/activate ; rasa run -m models --enable-api --cors "*" --debug; sleep 5s ; rasa run actions'''
        # args = shlex.split(cmd)
        # process = subprocess.Popen(
        #     args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        # stdout, stderr = process.communicate()

        subprocess.call(['sh', './updatedb.sh'])
        print("db updated")

        dispatcher.utter_message(
            text=f"""Hi admin, Database updated successfully🙂
            \n You can continue working""")

        return []


# class ActionUpdateDatabaseStatus(Action):

#     def name(self) -> Text:
#         return "action_update_database_status"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(
#             text=f"""Hi admin, Database updated successfully🙂
#             \n You can continue working""")

#         return []

class ActionSetReminder(Action):
    """Schedules a reminder, supplied with the last message's entities."""

    def name(self) -> Text:
        return "action_schedule_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        entity_value = tracker.latest_message['entities'][0]['value']
        entity_text = tracker.latest_message['entities'][0]['text']
        # print(tracker.latest_message['entities'])

        dispatcher.utter_message(f"I will remind you {entity_text}.")

        # date = datetime.datetime.now() + datetime.timedelta(seconds=5)
        # print(date)
        # print(entity_value)
        # print(type(entity_value))
        # print(type(date))

        datetest = parser.parse(entity_value)
        print(f"processed time : {datetest}")

        entities = tracker.latest_message.get("entities")

        reminder = ReminderScheduled(
            "EXTERNAL_reminder",
            trigger_date_time=datetest,
            entities=entities,
            name="my_reminder",
            kill_on_user_message=False,
        )

        return [reminder]


class ActionReactToReminder(Action):
    """Reminds the user to checkout the cart."""

    def name(self) -> Text:
        return "action_react_to_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        # name = next(tracker.get_slot("time"), "someone")
        dispatcher.utter_message(f"Hey, Reminding you to checkout your cart!")

        return []
