import requests, uuid, json


class TodoistRESTAPI:

    def __init__(self, api_token):
        self.api_token: str = api_token
        self.projects: dict = {}
        for project in self.GetAllProjectData():
            self.projects.update({project['name']: project['id']})
        # you can get API token here
        # https://todoist.com/prefs/integrations

    # Projects
    def GetAllProjectData(self):
        """
        :return list
        [{
            'id': Integer,
            'color': Integer,
            'name': String,
            'comment_count': Integer,
            'shared': Boolean,
            'favorite': Boolean,
            'sync_id': integer,
            'inbox_project': Boolean,
            'url': String
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

    # Sections
    def GetSectionId(self, project_id, section_name):
        section_data = self.GetAllSectionsData(project_id)
        for section in section_data:
            if section['name'] == section_name:
                return section['id']
        return 0

    def GetAllSectionsData(self, project_id):
        """
        :return list
        [{
            'id': Integer,
            'project_id': Integer,
            'order': Integer,
            'name': String
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
                "project_id": project_id,
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
    def GetActiveTasks(self, project_id, section_id=None, label_id=None, filter=None, lang=None, ids=None):
        return requests.get(
            "https://api.todoist.com/rest/v1/tasks",
            params={
                "project_id": project_id,
                "section_id": section_id,
                "label_id": label_id,
                "filter": filter,
                "lang": lang,
                "ids": ids
            },
            headers={
                "Authorization": "Bearer %s" % self.api_token
            }).json()

    def CreateNewTask(self, content, project_id=None, section_id=None, parent_id=None, order=None, label_ids=None,
                      priority=None, due_string=None, due_date=None, due_lang='en', assignee=None):
        """
        Please note that only one of the due_* fields can be used at the same time.
        (due_lang is a special case)
        :param content: String
        :param project_id: Integer
        :param section_id: Integer
        :param parent_id: Integer
        :param order: Integer
        :param label_ids: Array of Integers
        :param priority: Integer
        :param due_string: String
        :param due_date: String
        :param due_lang: String
        :param assignee: String
        """
        requests.post(
            "https://api.todoist.com/rest/v1/tasks",
            data=json.dumps({
                "content": content,
                "project_id": project_id,
                "section_id": section_id,
                "parent_id": parent_id,
                "order": order,
                "label_ids": label_ids,
                "priority": priority,
                "due_string": due_string,
                "due_date": due_date,
                "due_lang": due_lang,
                "assignee": assignee
            }),
            headers={
                "Content-Type": "application/json",
                "X-Request-Id": str(uuid.uuid4()),
                "Authorization": "Bearer %s" % self.api_token
            }).json()

    def GetSingleActiveTask(self, task_id):
        return requests.get(
            f"https://api.todoist.com/rest/v1/tasks/{task_id}",
            headers={
                "Authorization": "Bearer %s" % self.api_token
            }).json()

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
