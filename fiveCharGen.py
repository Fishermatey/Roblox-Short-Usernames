import requests, random, string, time

#------------#

names =  1000 # Amount of usernames to save
length =  5 # Length of usernames

#------------#


def randomword(length):
    letters = string.ascii_lowercase
    numbers = string.digits
    num_count = random.randint(1, 1)  # Randomly choose 1 or 2 for the number of digits
    username = ''.join(random.choice(letters) for _ in range(length - num_count))
    username += ''.join(random.choice(numbers) for _ in range(num_count))
    return ''.join(random.sample(username, len(username)))  # Shuffle the username

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	GRAY = '\033[90m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	

Found = 0
while Found < names:
	try:
		user = randomword(length)
		Data = requests.get(f'https://auth.roblox.com/v1/usernames/validate?request.username={user}&request.birthday=1337-04-20')
		
		if int(Data.json()['code']) == 0:
			Found += 1
			print(f"{bcolors.OKBLUE}[{Found}/{names}] [+] Found Username: {user} {bcolors.ENDC}")
			
			with open('valid.txt','a') as f:
				f.write(f"{user}\n")
		else:
			print(f'{bcolors.FAIL}[-] {user} {bcolors.ENDC}')
				
	except Exception as e:
		print('Error:', e)

	time.sleep(50/1000)

print(f"{bcolors.OKBLUE}[!] Finished {bcolors.ENDC}")
