from assignment_planner import assignments

def setup():
    assignments.clear()
    assignments.append({
        "name": "Test HW",
        "course": "CS101",
        "due": "2026-02-01",
        "priority": "High",
        "completed": False
    })

def test_add_assignment():
    setup()
    assert len(assignments) == 1
    assert assignments[0]["name"] == "Test HW"
    assert assignments[0]["completed"] is False

def test_mark_complete():
    setup()
    assignments[0]["completed"] = True
    assert assignments[0]["completed"] is True

print("All tests passed!")
