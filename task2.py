# =================================================================
# PROJECT: API Testing System
# DESCRIPTION: Executing REST API tests with Status Code & Response validation.
# DELIVERABLE: A script showcasing API assertions and test collections.
# =================================================================

import json

class APITestSuite:
    def __init__(self):
        self.test_results = []

    def assert_equals(self, test_name, actual, expected):
        """Simulates Postman assertions (pm.expect)."""
        status = "PASS ✅" if actual == expected else "FAIL ❌"
        self.test_results.append(f"{test_name}: {status} (Expected: {expected}, Actual: {actual})")

    def run_api_tests(self):
        print("🚀 Starting API Test Collection (Simulating Postman/Newman)...")
        
        # --- TEST CASE 1: GET User Details ---
        print("\n[GET] /api/users/1")
        # Simulating a real API response
        mock_response = {
            "status_code": 200,
            "body": {"id": 1, "name": "Aditya Tripathi", "role": "Android Intern"}
        }
        
        # Postman-style Assertions
        self.assert_equals("Status Code is 200", mock_response["status_code"], 200)
        self.assert_equals("User ID matches", mock_response["body"]["id"], 1)
        self.assert_equals("Name is correct", mock_response["body"]["name"], "Aditya Tripathi")

        # --- TEST CASE 2: POST Create Resource ---
        print("\n[POST] /api/tasks")
        mock_post_response = {
            "status_code": 201,
            "body": {"message": "Task Created Successfully"}
        }
        
        self.assert_equals("Status Code is 201 (Created)", mock_post_response["status_code"], 201)
        self.assert_equals("Response message valid", mock_post_response["body"]["message"], "Task Created Successfully")

    def display_report(self):
        print("\n" + "="*50)
        print("📊 API TEST EXECUTION REPORT")
        print("="*50)
        for result in self.test_results:
            print(result)
        print("="*50)

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    suite = APITestSuite()
    suite.run_api_tests()
    suite.display_report()
    
    print("\n✅ Task 10 Complete: API Test Collection logic implemented.")
