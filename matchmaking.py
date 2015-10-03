from earth_distance import get_earth_distance
from datetime import date

matchrank = 0

def decode_json_response():
	pass

def location_rank(loc_ref, loc_host, matchrank):
	distance = get_earth_distance(str(loc_ref),str(loc_host))

	if distance<10:
		matchrank+=5
	elif distance<25:
		matchrank+=3
	elif distance<50:
		matchrank+=1
	else:
		matchrank = 0 # nogo condition
		

	return matchrank

def gender_preference_rank(gender_ref, gender_host, genderpref_ref, genderpref_host, matchrank):
	
	#make sure everything is string
	gender_ref = str(gender_ref)
	gender_host = str(gender_host)
	genderpref_ref = str(genderpref_ref)
	genderpref_host = str(genderpref_host)

	if gender_ref == gender_host:
		matchrank+=1 # no problems here

	elif gender_ref != gender_host and genderpref_ref == "anyone" and gernderpref_ref == "anyone":
		matchrank+=1 # no problems here

	else: 
		matchrank = 0 # nogo condition
		

	return matchrank


def age_rank(usr1_dob, usr2_dob, matchrank):

	# TODO
	# convert date of birth to month, year, day
	# format is "dd.mm.yyyy"
	usr1_dob = str(usr1_dob).split('.')
	usr2_dob = str(usr2_dob).split('.')


	today = date.today()
	usr1_age = today.year - int(usr1_dob[2])
	usr2_age = today.year - int(usr2_dob[2])

	age_host = usr1_age
	age_ref = usr2_age

	print(age_host)
	print(age_ref)

	if age_host > age_ref * 0.9 and age_host < age_ref * 1.1: #+-10%
		matchrank+=5

	elif age_host > age_ref * 0.8 and age_host < age_ref * 1.2: #+-20%
		matchrank+=3

	elif age_host > age_ref * 0.6 and age_host < age_ref * 1.6: #+-30%
		matchrank+=1
	else:
		matchrank = 0 # nogo condition
		

	return matchrank

def language_rank(languages_ref, languages_host, matchrank):
	''' takes python list of languages for ref and host'''
	lanrank = 0
	language_ref = str(language_ref).lower()
	language_host = str(language_host).lower()


	for language in languages_ref:
		language = str(language).lower()
		if language in languages_host:
			lanrank+=1


	if lanrank < 1:
		matchrank = 0 # nogo condition

	else: matchrank += lanrank

	return matchrank


if __name__ == '__main__':

	print('---- testing age rank ----')
	usr1_dob = "12.04.1950"
	usr2_dob = "10.07.1960"
	matchrank = 0
	matchrank=age_rank(usr1_dob,usr2_dob,matchrank)
	print(usr1_dob)
	print(usr2_dob)
	print("matchrank: %i" %matchrank)

	usr1_dob = "12.04.1990"
	usr2_dob = "10.07.1970"
	matchrank = 0
	matchrank=age_rank(usr1_dob,usr2_dob,matchrank)
	print(usr1_dob)
	print(usr2_dob)
	print("matchrank: %i" %matchrank)