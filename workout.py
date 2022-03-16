import random
from colorama import init, Fore, Back, Style

init(autoreset = True)

compoundreps = ['10 reps x 4 = strength','12 reps x 4 = hypertrophy', '15 reps x 4 = endurance']
isoreps = ['10 reps x 3 = strength','12 reps x 3 = hypertrophy', '15 reps x 3 = endurance']

chest = [
	'plate loaded flat',
	'plate loaded incline',
	'flat bench dumbbells',
	'flat bench barbell',
	'incline bench dumbbells',
	'incline bench barbell',
	'machine flies',
	'cable flies',
	'****machine press****']

tricep = [
	'skullcrusher ss closegripbench',
	'v-bar pushdowns',
	'rope pulldowns',
	'rope pushaways']

back = [
	'plate loaded dual arm row',
	'lat pulldowns',
	'seated row',
	'plate loaded lat pulldowns',
	'plate loaded rows',
	'machine row']

bicep = [
	'hammer curls',
	'rope hammer curls',
	'ez bar curls',
	'plated loaded curls',
	'***zyzz cable curls***']

shoulders = [
	'plate loaded overhead press',
	'seated overhead dumbbell',
	'machine overhead press turned wrist']

shoulderiso = [
	'cable one arm raise',
	'cable two arm raise',
	'ezbar front raises',
	'one arms shoulder press dumbbell',
	'arnold press']

class getworkout():
	def __init__(self, compound, compoundreps, iso, isoreps):
		self.compound = compound
		self.compoundreps = compoundreps
		self.iso = iso
		self.isoreps = isoreps


print(Style.BRIGHT + '\nWelcome to your workout exercise randomizer!')
print('\nPlease enter "1" for Chest and Triceps, "2" for Back and Biceps, or "3" for Shoulders.')
input123 = int(input())

if input123 == 1:
	w1 = getworkout(random.sample(chest,k=3), random.sample(compoundreps,k=3), random.sample(tricep,k=3), random.sample(isoreps,k=3))
	print(Fore.MAGENTA + '\n-----CHEST-----')
	for x in range(3):
		print(Fore.MAGENTA + "{} {}".format(w1.compound[x].ljust(35," "), w1.compoundreps[x]))
	print(Fore.CYAN + '\n-----TRICEP-----')
	for x in range(3):
		print(Fore.CYAN + "{} {}".format(w1.iso[x].ljust(35," "), w1.isoreps[x]))

if input123 == 2:
	w2 = getworkout(random.sample(back,k=3), random.sample(compoundreps,k=3), random.sample(bicep,k=3), random.sample(isoreps,k=3))
	print(Fore.GREEN + '\n-----BACK-----')
	for x in range(3):
		print(Fore.GREEN + "{} {}".format(w2.compound[x].ljust(35," "), w2.compoundreps[x]))
	print(Fore.YELLOW + '\n-----BICEP-----')
	for x in range(3):
		print(Fore.YELLOW + "{} {}".format(w2.iso[x].ljust(35," "), w2.isoreps[x]))

if input123 == 3:
	w3 = getworkout(random.sample(shoulders,k=3), random.sample(compoundreps,k=3), random.sample(shoulderiso,k=3), random.sample(isoreps,k=3))
	print(Fore.BLUE + '\n-----SHOULDERS-----')
	for x in range(3):
		print(Fore.BLUE + "{} {}".format(w3.compound[x].ljust(35," "), w3.compoundreps[x]))
	print(Fore.RED + '\n-----SHOULDER ISOLATION-----')
	for x in range(3):
		print(Fore.RED + "{} {}".format(w3.iso[x].ljust(35," "), w3.isoreps[x]))
print('\n\n')


