from assignment_planner import assignments

def test_add_assignment():
    assignments.clear()

    assignment = {
        "name": "Test HW",
        "course": "CS101",
        "due": "2026-02-01",
        "priority": "High",
        "completed": False
    }

    assignments.append(assignment)

    assert len(assignments) == 1
    assert assignments[0]["name"] == "Test HW"
    assert assignments[0]["completed"] is False

def test_mark_complete():
    assignments[0]["completed"] = True
    assert assignments[0]["completed"] is True

print("All tests passed!")
