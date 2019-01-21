import json
import athletemodel
import yate
import sys
import cgitb

cgitb.enable()

names = athletemodel.get_names_from_store()
print(yate.start_response('application/json'))
print(json.dumps(sorted(names)))
athletes = athletemodel.get_from_store()
print(json.dumps(athletes))
