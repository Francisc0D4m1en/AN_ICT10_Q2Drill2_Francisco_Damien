from pyscript import document

grade_7 = {'Allison Burgers', 'Holly Block'}
grade_8 = {'Lux Embourg', 'Gabriel Bortoleto'}
grade_9 = {'Philip Pines', 'Iden Tificationcard'}
grade_10 = {'John French', 'Telly Vishon'}

def applicant_display(e):
    club = grade_7.union(grade_8, grade_9, grade_10) # Combines all the sets into one set.
    first_name = document.getElementById("user_input").value.strip()
    last_name = document.getElementById("user_input2").value.strip()
    full_name = f"{first_name} {last_name}".title()  # Joins both inputs and converts to title case.
    club.add(full_name)  # Adds the full name to the set.
    members = "<br>".join(club) # converts the set to a string for display purposes.
    document.getElementById("output").innerHTML = f"<h1>Club Members:</h1><br>{members}<br>Total Count: {len(club)}"  # Displays the updated set of club members and the total count.
    document.getElementById("output").style.display = "block"  # Shows the output div.