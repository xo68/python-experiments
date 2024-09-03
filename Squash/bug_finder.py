import re

import gitlab

# roup ID in scope
GROUP_ID = XXXXXXX

# FORMAT: ![alt text](img/markdown_logo.png "Title Text")
pattern = re.compile(r"!\[.*\]\(https?://.*[png|jpg|jpeg|gif|bmp].*\)", re.IGNORECASE)

gl = gitlab.Gitlab(url="https://gitlab.com", private_token="XXXXXXXX")
group = gl.groups.get(GROUP_ID)

# Use pagination
issues = group.issues.list(iterator=True, per_page=20, state="opened")

list_issues = []
for issue in issues:
    if pattern.findall(issue.description):
        list_issues.append((issue.id, issue.title, issue.description))

for issue in list_issues:
    # Format: (IssueID, Tittle, Description)
    print(f"{issue}")
