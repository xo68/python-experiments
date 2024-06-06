# REST API in Python using requests library
# https://pypi.org/project/requests/
# $pip install requests

import requests

# URL & AUTHENTICATION
URL = "*****"
USER = "*****"
PASSWORD = "*****"

# PROJECT, CAMPAIGN & ITERATION IN SCOPE
PROJECT_NAME = "*****"
PROJECT_ID = 12
CAMPAIGN_ID = 30
ITERATION_NAME = "********"
ITERATION_ID = 18

# API CALLS TO BE USED
GET_PROJECT = URL + "/api/rest/latest/projects/"
GET_PROJECTS = URL + "/api/rest/latest/projects?type=STANDARD"
GET_CAMPAIGNS = URL + "/api/rest/latest/campaigns/"
GET_ITERATIONS = URL + "/api/rest/latest/iterations/"


# Validate if a connection can be made
def try_connection():
    print(f"URL:[{URL}]")
    r = requests.get(URL, auth=(USER, PASSWORD))
    if r.status_code == 200:
        print("Connection Succesfull")
        r.close()
        return True
    else:
        print("Connection Failed")
        return False


# Display all projects and projects ID
def display_all_projects():
    r = requests.get(GET_PROJECTS, auth=(USER, PASSWORD))
    data = r.json()
    for p in data["_embedded"]["projects"]:
        print(f"Project id:{p['id']} = {p['name']}")


# Display one project based on project ID
def display_project(project_id):
    r = requests.get(GET_PROJECT + str(project_id), auth=(USER, PASSWORD))
    print(r.text)


# Display all campaigns for a project ID
def display_campaigns(project_id):
    r = requests.get(
        GET_PROJECT + str(project_id) + "/campaigns",
        auth=(USER, PASSWORD),
    )
    data = r.json()
    for p in data["_embedded"]["campaigns"]:
        print(f"Campaigns id:{p['id']} = {p['name']}")


# Return list of campaigns ID for a project ID
def get_campaigns(project_id):
    r = requests.get(
        GET_PROJECT + str(project_id) + "/campaigns",
        auth=(USER, PASSWORD),
    )
    data = r.json()
    print(data)
    campaigns = []
    for p in data["_embedded"]["campaigns"]:
        campaigns.append(p["id"])
    if campaigns:
        return campaigns
    else:
        return None


# Display a campaign based on campaign ID
def display_campaign(campaign_id):
    r = requests.get(
        GET_CAMPAIGNS + str(campaign_id),
        auth=(USER, PASSWORD),
    )
    print(r.text)


# Display an iteration
def display_iteration(iter_id):
    r = requests.get(
        GET_ITERATIONS + str(iter_id) + "?fields=*",
        auth=(USER, PASSWORD),
    )
    print(r.text)


# Display a test plan within an iteration
def display_testplan(iter_id):
    r = requests.get(
        GET_ITERATIONS + str(iter_id) + "/test-plan",
        auth=(USER, PASSWORD),
    )
    print(r.text)


if __name__ == "__main__":
    connection = try_connection()
    if connection:
        # This will list the test cases and statusses
        display_testplan(ITERATION_ID)

        # display_iteration(ITERATION_ID)
        # display_campaign(CAMPAIGN_ID)
        # c = get_campaigns(PROJECT_ID)
        # display_campaigns(PROJECT_ID)
        # display_project(PROJECT_ID)
        # display_all_projects()
