import todoist
api_key = 'ad9122af2b70ed7b892f3cc04210cfe094f21780'
api = todoist.TodoistAPI(api_key)
api.sync()
full_name = api.state['user']['full_name']
print(api.state)

