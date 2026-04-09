# =================================================================
# PROJECT: Data-Driven Testing (DDT)
# DESCRIPTION: Executing Selenium tests using inputs from a CSV file.
# DELIVERABLE: Python script that reads data, runs tests, and logs results.
# =================================================================

import csv
import time

# --- MOCK DATA (Simulating a CSV File) ---
# In a real scenario, you would have a 'test_data.csv' file.
test_data_csv = [
    ["username", "password", "expected_result"],
    ["aditya_01", "pass123", "Login_Success"],
    ["user_test", "wrong_pass", "Login_Failed"],
    ["admin_user", "admin@123", "Login_Success"]
]

def run_selenium_test(user, pwd, expected):
    """Simulates Selenium WebDriver actions."""
    print(f"🤖 Selenium: Opening Browser...")
    print(f"🔗 Navigating to: https://example-login.com")
    print(f"⌨️ Entering Username: {user}")
    print(f"⌨️ Entering Password: {pwd}")
    print(f"🖱️ Clicking Login Button...")
    
    # Simulating actual verification logic
    time.sleep(0.5)
    actual_result = "Login_Success" if "123" in pwd else "Login_Failed"
    
    status = "PASS ✅" if actual_result == expected else "FAIL ❌"
    return status

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print("TASK 9: DATA-DRIVEN TESTING SYSTEM")
    print("-" * 45)
    
    results_log = []

    # 1. Reading from (Simulated) CSV
    print("📁 Reading input data from CSV file...")
    header = test_data_csv[0]
    data_rows = test_data_csv[1:]

    # 2. Iterating through multiple input sets
    for index, row in enumerate(data_rows, start=1):
        username, password, expected = row
        print(f"\n--- Running Test Set #{index} ---")
        
        # Execute Test
        test_status = run_selenium_test(username, password, expected)
        
        # 3. Logging Results
        log_entry = f"Test #{index} | User: {username} | Result: {test_status}"
        results_log.append(log_entry)

    # Final Report
    print("\n" + "="*45)
    print("📊 FINAL TEST EXECUTION LOG")
    print("="*45)
    for log in results_log:
        print(log)
    print("-" * 45)
    print("DELIVERABLE: Data-Driven Script Complete.")
