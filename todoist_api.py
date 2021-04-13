import requests, uuid, json


class TodoistAPI:
    def __init__(self, api_token):
        self.api_token = api_token

    # you can get API token here
    # https://todoist.com/prefs/integrations

    def CreateNewProject(self, project_name):
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

    def GetSingleProject(self):
        return requests.get(
            "https://api.todoist.com/rest/v1/projects",
            headers={
                "Authorization": "Bearer %s" % self.api_token}
        ).json()

    def GetAProject(self, project_id):
        """

        :type project_id: str
        """
        return requests.get(
            "https://api.todoist.com/rest/v1/projects/" + project_id,
            headers={
                "Authorization": "Bearer %s" % self.api_token
            }).json()


api = TodoistAPI(input("your API token : "))
