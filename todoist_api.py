import requests, uuid, json


class TodoistAPI:
    def __init__(self, api_token):  # Project Method
        self.api_token = api_token
        self.projects = {}
        self.LoadProjects()
        # you can get API token here
        # https://todoist.com/prefs/integrations

    def LoadProjects(self):
        for project in self.GetAllProjectData():
            self.projects.update({project['name']: str(project['id'])})

    def GetAllProjectData(self):  # Project Method
        """

        :return: list
        """
        return requests.get(
            "https://api.todoist.com/rest/v1/projects",
            headers={
                "Authorization": "Bearer %s" % self.api_token}
        ).json()

    def GetSingleProjectData(self, project_id):  # Project Method
        """

        :type project_id: str
        """
        return requests.get(
            "https://api.todoist.com/rest/v1/projects/" + project_id,
            headers={
                "Authorization": "Bearer %s" % self.api_token
            }).json()

    def CreateNewProject(self, project_name):  # Project Method
        """

        :type project_name: str
        """
        requests.post(
            "https://api.todoist.com/rest/v1/projects",
            data=json.dumps({
                "name": project_name
            }),
            headers={
                "Content-Type": "application/json",
                "X-Request-Id": str(uuid.uuid4()),
                "Authorization": "Bearer %s" % self.api_token
            }).json()
        self.LoadProjects()

    def UpdateProjectName(self, project_id, project_name):  # Project Method
        requests.post(
            f"https://api.todoist.com/rest/v1/projects/{project_id}",
            data=json.dumps({
                "name": project_name
            }),
            headers={
                "Content-Type": "application/json",
                "X-Request-Id": str(uuid.uuid4()),
                "Authorization": "Bearer %s" % self.api_token
            })
        self.LoadProjects()

    def DeleteProject(self, project_id):  # Project Method
        requests.delete(
            f"https://api.todoist.com/rest/v1/projects/{project_id}",
            headers={
                "Authorization": "Bearer %s" % self.api_token
            })
        self.LoadProjects()

    def GetAllCollaborators(self):  # Project Method
        requests.get(
            "https://api.todoist.com/rest/v1/projects/2203306141/collaborators",
            headers={
                "Authorization": "Bearer %s" % self.api_token
            }).json()

    def GetProjectId(self, project_name):  # Project Method
        return self.projects[project_name]
