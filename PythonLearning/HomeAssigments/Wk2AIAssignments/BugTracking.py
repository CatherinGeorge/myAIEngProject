class BugTracker:
    def __init__(self):
        # Dictionary to store bugs: {bug_id: {description, severity, status}}
        self.bugs = {}

    def add_bug(self, bug_id, description, severity):
        # Add a new bug with status "Open"
        if bug_id in self.bugs:
            print(f"Bug ID {bug_id} already exists.")
        else:
            self.bugs[bug_id] = {
                "description": description,
                "severity": severity,
                "status": "Open"
            }
            print(f"Bug {bug_id} added successfully.")

    def update_status(self, bug_id, new_status):
        # Update the status of a given bug
        if bug_id in self.bugs:
            old_status = self.bugs[bug_id]["status"]
            self.bugs[bug_id]["status"] = new_status
            print(f"Bug {bug_id} status updated: {old_status} → {new_status}")
        else:
            print(f"Bug ID {bug_id} not found.")

    def list_all_bugs(self):
        # Print all bugs in a readable format
        if not self.bugs:
            print("No bugs found.")
        else:
            print("\nAll Bug Records:")
            print("-" * 50)
            for bug_id, details in self.bugs.items():
                print(f"Bug ID: {bug_id}")
                print(f"Description: {details['description']}")
                print(f"Severity: {details['severity']}")
                print(f"Status: {details['status']}")
                print("-" * 50)


if __name__ == "__main__":
    # Create BugTracker object
    tracker = BugTracker()

    # Add at least three bugs
    tracker.add_bug(101, "Login button not working", "High")
    tracker.add_bug(102, "Page crashes on refresh", "Medium")
    tracker.add_bug(103, "Typo in footer text", "Low")

    # Update statuses
    tracker.update_status(101, "In Progress")
    tracker.update_status(102, "Closed")

    # Display all bug records
    tracker.list_all_bugs()
