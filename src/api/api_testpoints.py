import sys
from pathlib import Path

# Add project root to sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.navigation.dashboard.dashboard_navigation import TestPointNavigateDashboard
from src.testpoint.testpoint_main import TestPoint



class TestPointGetUsers(TestPoint):
    def __init__(self, base_url):
        def func():
            import requests
            response = requests.get(f"{base_url}/users")
            print("Status code:", response.status_code)
            print("Response body:", response.text)
            assert response.status_code == 200
            assert isinstance(response.json(), list)
            return response.json()

        # Assign metadata separately
        tp_id = "TP001"
        tp_description = f"Get all users from {base_url}"
        tkt_id= f"ADAD-0000"
        tp_status=f"ready"
        tp_execution = ""

        # Pass metadata and function to base class
        super().__init__(id=tp_id, description=tp_description, func=func, ticket_id= tkt_id , status = tp_status, execution =tp_execution)  



if __name__ == "__main__":
    t1=TestPointNavigateDashboard()
    result=t1.run()
    print("API response:", result)
