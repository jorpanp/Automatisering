from workflow.full_workflow import fetch_data

def test_fetch_data():
    data = fetch_data()
    if data:
        print("😁Fetch_data is working!")
    else:
        print("🤣Fetch_data is not working")

test_fetch_data()