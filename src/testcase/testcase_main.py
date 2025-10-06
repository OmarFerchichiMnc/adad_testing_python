from datetime import datetime
import inspect
import json
import logging
import os


class TestCase:
    def __init__(self, id, description, ticket_id, status="ready"):
        self.id = id
        self.description = description
        self.ticket_id = ticket_id
        self.status = status
        self.execution = "failed"   # default before running
        self.testpoints = []        # list to store test points in this case

    def add_testpoint(self, testpoint):
        """Add a TestPoint object to this test case, skipping None values."""
        if testpoint is not None:
            self.testpoints.append(testpoint)
        else:
            logging.warning(f"⚠️ Tried to add None as a TestPoint in TestCase {self.id}")

    def run(self, driver=None):
        """Run all test points inside this test case and update execution."""
        all_passed = True

        for i, tp in enumerate(self.testpoints):
            if tp is None:
                logging.error(f"❌ TestPoint at index {i} is None!")
                all_passed = False
                continue

            try:
                logging.info(f"▶️ Running TestPoint {tp.id}: {tp.description}")
                tp.run(driver)
                if tp.execution != "passed":
                    all_passed = False
            except AssertionError:
                all_passed = False
            except Exception as e:
                logging.error(f"❌ Error in TestPoint {tp.id}: {e}", exc_info=True)
                all_passed = False

        self.execution = "passed" if all_passed else "failed"
        self.export_to_json()
        assert all_passed, f"❌ TestCase {self.id} has failing test points!"
        print(f"✅ TestCase {self.id} execution: {self.execution}")
        return self

    def export_to_json(self):
        """Export this TestCase and its TestPoints to JSON with timestamp and file name"""
        try:
            os.makedirs("reports", exist_ok=True)

            # Use TestCase ID for filename instead of caller file
            safe_id = str(self.id).replace(" ", "_")
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = os.path.join("reports", f"TestCase_{safe_id}_{timestamp}.json")

            # Prepare JSON data
            data = {
                "id": self.id,
                "description": self.description,
                "ticket_id": self.ticket_id,
                "status": self.status,
                "execution": self.execution,
                "testpoints": []
            }

            for i, tp in enumerate(self.testpoints):
                if tp is None:
                    logging.error(f"❌ Skipping None TestPoint at index {i} in export")
                    continue
                data["testpoints"].append({
                    "id": getattr(tp, "id", None),
                    "description": getattr(tp, "description", None),
                    "ticket_id": getattr(tp, "ticket_id", None),
                    "status": getattr(tp, "status", None),
                    "execution": getattr(tp, "execution", None)
                })

            with open(filename, "w") as f:
                json.dump(data, f, indent=4)

            print(f"✅ TestCase report generated: {filename}")
            return filename

        except Exception as e:
            logging.error("❌ Error while exporting TestCase to JSON", exc_info=True)
            raise

