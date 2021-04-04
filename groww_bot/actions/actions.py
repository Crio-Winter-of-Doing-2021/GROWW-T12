# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import pandas as pd
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# def superCategoryCommon(,):
#     buttons = []
#     for category in new_list_category:
#         if category=='DASHBOARD': category='Holdings'
#         category_val= category
#         buttons.append( {"title": category,"payload": category})


# SUPER CATEGORIES
class ActionSuperCategoryStocks(Action):

    def name(self) -> Text:
        return "action_super_category_stocks"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        df = pd.read_csv('./groww_faqs_utf-8.csv')
        super_category = 'Stocks'
        df_scope = df.loc[df['superCategory'] == super_category]
        list_category = df_scope.category.unique()
        new_list_category = {x.replace('SX_', '') for x in list_category}

        buttons = []
        for category in new_list_category:
            if category=='DASHBOARD': category='Holdings'
            category_val= category
            buttons.append( {"title": category,"payload": category})

        dispatcher.utter_message(text="Choose a category",buttons=buttons)

        return []

class ActionSuperCategoryMutualFunds(Action):

    def name(self) -> Text:
        return "action_super_category_mutual_funds"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        df = pd.read_csv('./groww_faqs_utf-8.csv')
        super_category = 'Mutual Funds'
        df_scope = df.loc[df['superCategory'] == super_category]
        list_category = df_scope.category.unique()
        new_list_category = {x.replace('MF_', '') for x in list_category}

        buttons = []
        for category in new_list_category:
            if category=='DASHBOARD': category='My investments'
            category_val= category
            buttons.append( {"title": category,"payload": category})

        dispatcher.utter_message(text="Choose a category",buttons=buttons)

        return []

def commonCategory(val):
    df = pd.read_csv('./groww_faqs_utf-8.csv')
    df_scope = df.loc[df['category'] == val]
    list_questionTags = df_scope.questionTags.unique()
    buttons = []
    for questionTag in list_questionTags:
        buttons.append( {"title": questionTag,"payload": questionTag})
    return buttons

# CATEGORIES
class ActionCategorySXDashboard(Action):

    def name(self) -> Text:
        return "action_category_sx_dashboard"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        df = pd.read_csv('./groww_faqs_utf-8.csv')
        my_val = 'SX_DASHBOARD'
        df_scope = df.loc[df['category'] == my_val]
        list_questionTags = df_scope.questionTags.unique()

        buttons = []
        for questionTag in list_questionTags:
            title = questionTag
            # as there is both category 'Holdings' & questionTag 'Holdings' in Stocks
            if questionTag=='Holdings': questionTag='Holdings questionTag'
            buttons.append( {"title": title,"payload": questionTag})
        dispatcher.utter_message(text="Please select a sub category",buttons=buttons)

        return []

class ActionCategoryIPO(Action):

    def name(self) -> Text:
        return "action_category_ipo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        my_val = 'SX_IPO'

        buttons = commonCategory(my_val)
        dispatcher.utter_message(text="Please select a sub category",buttons=buttons)

        return []

class ActionCategoryMyInvestments(Action):

    def name(self) -> Text:
        return "action_category_my_investments"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        my_val = 'MF_DASHBOARD'

        buttons = commonCategory(my_val)
        dispatcher.utter_message(text="Please select a sub category",buttons=buttons)

        return []

def commonQuestionTag(val):
    df = pd.read_csv('./groww_faqs_utf-8.csv')
    df_scope = df.loc[df['questionTags'] == val]
    list_questions = df_scope.questionTitle
    buttons = []
    for question in list_questions:
        buttons.append( {"title": question,"payload": question})
    return buttons

# QUESTION TAGS
class ActionQuestionTagIntradayPositions(Action):

    def name(self) -> Text:
        return "action_questionTag_intraday_positions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        df = pd.read_csv('./groww_faqs_utf-8.csv')
        my_val = 'Intraday Positions'
        df_scope = df.loc[df['questionTags'] == my_val]
        list_questions = df_scope.questionTitle
        buttons = []
        for question in list_questions:
            buttons.append( {"title": question,"payload": question})
        dispatcher.utter_message(text="Choose your question",buttons=buttons)

        return []
    
class ActionQuestionTagHoldings(Action):

    def name(self) -> Text:
        return "action_questionTag_holdings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = commonQuestionTag("Holdings")
        dispatcher.utter_message(text="Choose your question",buttons=buttons)

        return []

class ActionQuestionTagBeforeApplying(Action):

    def name(self) -> Text:
        return "action_questionTag_before_applying"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = commonQuestionTag("Before Applying")
        dispatcher.utter_message(text="Choose your question",buttons=buttons)

        return []

class ActionQuestionTagApplying(Action):

    def name(self) -> Text:
        return "action_questionTag_applying"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = commonQuestionTag("Applying")
        dispatcher.utter_message(text="Choose your question",buttons=buttons)

        return []

class ActionQuestionTagDeliveryPositions(Action):

    def name(self) -> Text:
        return "action_questionTag_delivery_positions"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="this will have DP related questions")

        return []

# Questions
class ActionQuestionMyIssueIsNotListedHere(Action):

    def name(self) -> Text:
        return "action-question-my-issue-is-not-listed-here"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        buttons = []
        buttons.append( {"title": "RAISE A TICKET","payload": "https://groww.in/user/help/tickets/create"})
        answer = "You can try searching for your issue. Alternatively you can raise a ticket with us. Our Customer Support champs will help you out in no time!"
        dispatcher.utter_message(text=answer,buttons=buttons)

        return []

class ActionQuestionWhatHappensIfIdontExitMyPosition(Action):

    def name(self) -> Text:
        return "action-question-what-happens-if-i-dont-exit-my-position"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        df = pd.read_csv('./groww_faqs_utf-8.csv','a')
        my_val = 'what-happens-if-i-dont-exit-my-position-1'
        df_scope = df.loc[df['questionId'] == my_val]
        answer = df_scope.iloc[0]['answerText']
        dispatcher.utter_message(text=answer)

        return []