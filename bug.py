class Bug:
    def __init__(self, id, description, project, priority, entry_date, resolved):
        self.id = id                                # unique identifier for each bug 
        self.description = description              # description of the bug
        self.project = project                      # what project the bug is present in 
        self.priority = priority                    # the priority of removing the bug (low, medium, high)
        self.entry_date = entry_date                # date and time that the bug was added to the tracker
        self.resolved = resolved                    # integer flag storing whether or not the bug has been removed/resolved