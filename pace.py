import sys
import string 
import math

# Truncate function
def truncate(number, digits):
	stepper = pow(10.0, digits)
	return (math.trunc(stepper * number) / stepper)

# App's core
args = sys.argv[1:]

if len(args) < 2:
	print "You need at least two input parameters. (distance [km] and time [00h00m00s])"

else:
	# Set distance
	distance = args[0]	
	
	# Manipulate time input
	str_args = ""
	time = str_args.join(args[1:])

	# Get the hours
	if time.find("h") > -1:
		i = 0
		hours = ""
		while time[i] != "h" and i < len(time):
			hours += time[i]
			i += 1

		i += 1

	else:
		try:
		    i
		except NameError:
		    i = 0

		hours = "0"

	# Get the minutes
	if time.find("m") > -1:
		minutes = ""
		while time[i] != "m" and i < len(time):
			minutes += time[i]
			i += 1

		i += 1

	else:
		try:
		    i
		except NameError:
		    i = 0

		minutes = "0"

	# Get the seconds
	if time.find("s") > -1:
		seconds = ""
		while time[i] != "s" and i < len(time):
			seconds += time[i]
			i += 1

	else:
		seconds = "0"

	# Convert time in seconds
	total_seconds = (int(hours) * 3600.0) + (int(minutes) * 60.0) + (int(seconds) * 1.0)
	
	
	avg_speed = ((int(distance) * 1000.0) / total_seconds) * 3.6
	pace =  (((total_seconds % 3600.0) / 60) / int(distance))
	pace = truncate((int(pace) + (pace - int(pace))* 60/100), 2)
	
	# Output results
	print "\n================================"
	print "Distance: \t" + distance + "km"
	print "--------------------------------"
	print "Time: \t\t" + hours + "h" + " " + minutes + "' " + seconds + '"'
	print "--------------------------------"
	print "PACE:\t\t",pace
	print "--------------------------------"
	print "AVG Speed:\t", "{:,.2f}km/h".format(avg_speed)
	print "================================"