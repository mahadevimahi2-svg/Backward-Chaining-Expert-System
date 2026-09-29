facts = {"CGPA_Above_7", "Attendance_Above_75",
         "Completed_Projects", "Coding_Skills"}

rules = [
    ("R1", ["CGPA_Above_7", "Attendance_Above_75"], "GoodAcademicPerformance"),
    ("R2", ["Completed_Projects", "Coding_Skills"], "ReadyForInterviews"),
    ("R3", ["GoodAcademicPerformance", "ReadyForInterviews"], "EligibleForPlacement"),
    ("R4", ["Low_Coding_Score"], "NeedsExtraPractice"),
]

def prove(goal, depth=0):
    pad = "  " * depth
    print(f"{pad}Goal: {goal}")
    if goal in facts:
        print(f"{pad}-> '{goal}' is a known FACT")
        return True
    for name, conditions, conclusion in rules:
        if conclusion == goal:
            print(f"{pad}Trying {name}: IF {' AND '.join(conditions)} THEN {conclusion}")
            if all(prove(c, depth + 1) for c in conditions):
                print(f"{pad}-> '{goal}' PROVED using {name}")
                return True
    print(f"{pad}-> '{goal}' cannot be proved")
    return False

goal = "EligibleForPlacement"
print("Facts:", sorted(facts), "\n")
result = prove(goal)
print("\nFinal Conclusion:",
      f"The student IS {goal}." if result else f"The student is NOT {goal}.")