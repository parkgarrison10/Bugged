class Bug:
    def __init__(self, id, description, project, priority, date_of_entry, resolved):
        self.id = id
        self.description = description
        self.project = project
        self.priority = priority
        self.date_of_entry = date_of_entry
        self.resolved = resolved