import json

class TestPoint:
    all_tests = []

    def __init__(self, id, description, func, ticket_id, status, execution="failed"):
        self.id = id
        self.description = description
        self.func = func
        self.ticket_id = ticket_id
        self.status = status
        self.execution = execution
        TestPoint.all_tests.append(self)

    def run(self, driver=None):
        print(f"Running TestPoint {self.id}: {self.description}")
        try:
            if driver:
                self.func(driver)
            else:
                self.func(driver)
            self.execution = "passed"
        except AssertionError as e:
            self.execution = "failed"
            print(f"❌ Assertion failed in {self.id}: {e}")
        except Exception as e:
            self.execution = "failed"
            print(f"❌ Error in {self.id}: {e}")
        return self
