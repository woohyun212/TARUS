import requests, uuid, json


class TodoistAPI:

    def __init__(self, api_token):
        self.api_token: str = api_token
        self.projects: dict = {}
        for project in self.GetAllProjectData():
            self.projects.update({project['name']: str(project['id'])})
        # you can get API token here
        # https://todoist.com/prefs/integrations

    # Projects
    def GetAllProjectData(self):
        """
        :return list
        [{
            'id': int,
            'color': int,
            'name': str,
            'comment_count': int,
            'shared': bool,
            'favorite': bool,
            'sync_id': int,
            'inbox_project': bool,
            'url': str
        }]
        """
        return requests.get(
            "https://api.todoist.com/rest/v1/projects",
            headers={
                "Authorization": "Bearer %s" % self.api_token}
        ).json()

    def LoadProjects(self):
        for project in self.GetAllProjectData():
            self.projects.update({project['name']: str(project['id'])})

    def GetSingleProjectData(self, project_id):
        return requests.get(
            "https://api.todoist.com/rest/v1/projects/" + project_id,
            headers={
                "Authorization": "Bearer %s" % self.api_token
            }).json()

    def CreateNewProject(self, project_name):
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

    def UpdateProjectName(self, project_id, project_name):
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

    def DeleteProject(self, project_id):
        requests.delete(
            f"https://api.todoist.com/rest/v1/projects/{project_id}",
            headers={
                "Authorization": "Bearer %s" % self.api_token
            })
        self.LoadProjects()

    def GetAllCollaborators(self, project_id):
        requests.get(
            f"https://api.todoist.com/rest/v1/projects/{project_id}/collaborators",
            headers={
                "Authorization": "Bearer %s" % self.api_token
            }).json()

    def GetProjectId(self, project_name: str):
        return self.projects[project_name]

    # Sections
    def GetAllSectionsData(self, project_id):
        """
        :return list
        [{
            'id': int,
            'project_id': int,
            'order': int,
            'name': str
        }]
        """
        return requests.get(
            f"https://api.todoist.com/rest/v1/sections?project_id={project_id}",
            headers={
                "Authorization": "Bearer %s" % self.api_token
            }).json()

    def CreateNewSection(self, project_id: int, section_name):
        requests.post(
            "https://api.todoist.com/rest/v1/sections",
            data=json.dumps({
                "project_id": str(project_id),
                "name": section_name
            }),
            headers={
                "Content-Type": "application/json",
                "X-Request-Id": str(uuid.uuid4()),
                "Authorization": "Bearer %s" % self.api_token
            }).json()

    def GetSingleSectionData(self, section_id):
        return requests.get(
            f"https://api.todoist.com/rest/v1/sections/{section_id}",
            headers={
                "Authorization": "Bearer %s" % self.api_token
            }).json()

    def UpdateSection(self, section_id, section_name):
        requests.post(
            f"https://api.todoist.com/rest/v1/sections/{section_id}",
            data=json.dumps({"name": section_name}),
            headers={
                "Content-Type": "application/json",
                "X-Request-Id": str(uuid.uuid4()),
                "Authorization": "Bearer %s" % self.api_token
            })

    def DeleteSection(self, section_id):
        requests.delete(
            f"https://api.todoist.com/rest/v1/sections/{section_id}",
            headers={
                "Authorization": "Bearer %s" % self.api_token
            })

    # Tasks
    def GetActiveTasks(self, project_id, section_id=None):
        return requests.get(
            "https://api.todoist.com/rest/v1/tasks",
            params={
                "project_id": project_id,
                "section_id": section_id
            },
            headers={
                "Authorization": "Bearer %s" % self.api_token
            }).json()

    def CreateNewTask(self, content, due_string, due_lang, priority):
        requests.post(
            "https://api.todoist.com/rest/v1/tasks",
            data=json.dumps({
                "content": "Buy Milk",
                "due_string": "tomorrow at 12:00",
                "due_lang": "kr",
                "priority": 4
            }),
            headers={
                "Content-Type": "application/json",
                "X-Request-Id": str(uuid.uuid4()),
                "Authorization": "Bearer %s" % self.api_token
            }).json()

    def GetSingleActiveTask(self):
        pass

    def UpdateTask(self):
        pass

    def CloseTask(self):
        pass

    def ReopenTask(self):
        pass

    def DeleteTask(self):
        pass


if __name__ == "__main__":
    pass
