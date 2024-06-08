# REST API in Python using requests library
# https://pypi.org/project/requests/
# $pip install requests

# SQUASH
# Project (Root)
# |-> Campaigns
# |--> Iterations -> TestPlans -> TestCases
# |---> TestSuite(Optional) -> TestPlans -> TestCases

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
PASSWORD = "******"


# Validate if a connection can be made
def try_connection():
    r = requests.get(URL, auth=(USER, PASSWORD))
    if r.status_code == 200:
        return True
    return False


# Return the campaign status
# [None | Undefined | Planned | In Progress | Finished | Archived]
def get_campaign_status(campaign_id):
    r = requests.get(GET_CAMPAIGNS + str(campaign_id), auth=(USER, PASSWORD))
    if r.status_code == 200:
        return r.json()["status"]
    return None


# Return the target end date of an iteration
def get_iteration_end_date(iteration_id):
    r = requests.get(GET_ITERATIONS + str(iteration_id), auth=(USER, PASSWORD))
    if r.status_code == 200:
        iteration = r.json()
        if "scheduled_end_date" in iteration:
            return iteration["scheduled_end_date"]
    return None


# Return a dict() of CAMPAIGN_ID:CAMPAIGN_NAME for a project
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


# Return project ID based on project name
def get_project_id(project_name):
    r = requests.get(
        GET_PROJECTS + "?projectName=" + project_name,
        auth=(USER, PASSWORD),
    )
    if r.status_code == 200:
        return r.json()["id"]
    return None


# Return the list of defects for a campaign
def get_defects_from_campaign(campaign_id):
    r = requests.get(
        GET_CAMPAIGNS + str(campaign_id) + "/issues",
        auth=(USER, PASSWORD),
    )
    if r.status_code == 200:
        defects = set()
        cmp = r.json()
        if "_embedded" in cmp.keys():
            for d in cmp["_embedded"]["issues"]:
                defects.add(d["url"])
            return defects
    return None


# Return the list of test cases & status for an iteration
def get_test_plans_from_iteration(iteration_id):
    r = requests.get(
        GET_ITERATIONS + str(iteration_id) + "/test-plan",
        auth=(USER, PASSWORD),
    )
    if r.status_code == 200:
        test_plans = r.json()
        test_cases = []
        if "_embedded" in test_plans.keys():
            for tc in test_plans["_embedded"]["test-plan"]:
                # Only store the last execution
                test_cases.append(
                    [tc["referenced_test_case"]["name"], tc["execution_status"]]
                )
            return test_cases
    return None


# Return a dict() of iteration ID:NAME for a campaign
def get_iterations_from_campaign(campaign_id):
    r = requests.get(
        GET_CAMPAIGNS + str(campaign_id) + "/iterations",
        auth=(USER, PASSWORD),
    )
    if r.status_code == 200:
        iterations = r.json()
        if "_embedded" in iterations.keys():
            it_dict = dict()
            for iteration in iterations["_embedded"]["iterations"]:
                it_dict[iteration["id"]] = iteration["name"]
            return it_dict
    return None


def display_defects(campaign_id):
    if defects := get_defects_from_campaign(campaign_id):
        print(f"|==> Total Defects = {len(defects)}")
        for d in defects:
            print(f"| Defect URL = {d}")


def display_iterations(campaign_id):
    if iterations := get_iterations_from_campaign(campaign_id):
        print(f"|==> Total Iterations = {len(iterations)}")
        for it in iterations:
            print(
                f"  Iteration ID:{it} = '{iterations[it]}'; Target EndDate = {get_iteration_end_date(it)}"
            )
            if test_cases := get_test_plans_from_iteration(it):
                print(f"  {len(test_cases)} Test Cases:")
                for tc in test_cases:
                    print(f"  >> Test Case: {tc}")


if __name__ == "__main__":
    if not try_connection():
        print("Connection Error !")
        exit()
    if not (project_id := get_project_id(PROJECT_NAME)):
        print(f"Project '{PROJECT_NAME}' Not Found !")
        exit()
    print(f"Project ID:{project_id} = {PROJECT_NAME}")
    if list_campaigns := get_all_campaigns(project_id):
        print(f"Total Campaigns = {len(list_campaigns)}")
        for cmp in list_campaigns:
            print(f"\n[Campaign ID = {cmp}; Name = {list_campaigns[cmp]}]")
            print(f"| STATUS = {get_campaign_status(cmp)}")
            display_defects(cmp)
            display_iterations(cmp)
