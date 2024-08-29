i = 1
while i <= 5:
	print("Code Runned "+ str(i) + " times")
	i += 1
	

#----------------------------------------------

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_limit > guess_count:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
     print("You Lose")
else:
    print("You Win")