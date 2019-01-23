import cgi
import cgitb
import athletemodel
import yate

cgitb.enable()

form_data = cgi.FieldStorage()
athleteId = form_data['which_athlete'].value
athlete = athletemodel.get_athlete_from_id(athleteId)

print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
print(yate.header("Athlete: " + athlete['Name'] + " DOB: " +
                  athlete['DOB'] + "."))
print(yate.para("The top times for this athlete are: "))
print(yate.u_list(athlete['top3']))
print(yate.include_footer({"Home": "/index.html", "Select another athlete": "generate_list.py"}))
