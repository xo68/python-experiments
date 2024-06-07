# REST API in Python using requests library
# https://pypi.org/project/requests/
# $pip install requests

import requests

# URLS
URL = "*****"
GET_PROJECT = URL + "/api/rest/latest/projects/"
GET_PROJECTS = URL + "/api/rest/latest/projects"
GET_CAMPAIGNS = URL + "/api/rest/latest/campaigns/"
GET_ITERATIONS = URL + "/api/rest/latest/iterations/"

# Project & Credentials
PROJECT_NAME = "*****"
USER = "*****"
PASSWORD = "*****"


# Validate if a connection can be made
def try_connection():
    r = requests.get(URL, auth=(USER, PASSWORD))
    if r.status_code == 200:
        return True
    return False


# Return campaign status
# [None | Underfined | Planned | In Progress | Finished | Archived]
def get_campaign_status(campaign_id):
    r = requests.get(GET_CAMPAIGNS + str(campaign_id), auth=(USER, PASSWORD))
    if r.status_code == 200:
        cmp = r.json()
        return cmp["status"]
    return None


# Return a dict of CAMPAIGN_ID : CAMPAIGN_NAME
def get_all_campaigns(project_id):
    r = requests.get(
        GET_PROJECT + str(project_id) + "/campaigns", auth=(USER, PASSWORD)
    )
    if r.status_code == 200:
        cmp = r.json()
        if "_embedded" in cmp.keys():
            cmp_dict = {}
            for c in cmp["_embedded"]["campaigns"]:
                cmp_dict[c["id"]] = c["name"]
            return cmp_dict
    return None


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


# Return project ID based on project name
def get_project_id(project_name):
    r = requests.get(
        GET_PROJECTS + "?projectName=" + project_name,
        auth=(USER, PASSWORD),
    )
    if r.status_code == 200:
        cmp = r.json()
        return cmp["id"]
    return None


if __name__ == "__main__":

    if not try_connection():
        print("Connection Error !")
        exit()

    if not (project_id := get_project_id(PROJECT_NAME)):
        print(f"Project '{PROJECT_NAME}' Not Found !")
        exit()
    print(f"Project ID {project_id} is {PROJECT_NAME}")

    if list_campaigns := get_all_campaigns(project_id):
        print(f"Total Campaigns is {len(list_campaigns)}")
        for cmp in list_campaigns:
            print(f"Campaign ID:{cmp} = {list_campaigns[cmp]}")
            print(f"> Status={get_campaign_status(cmp)}")
