i = 1
while i <= 5:
    print(i)
    i = i + 1
print("done")


i = 1
while i <= 5:
    print("*" * i)
    i = i + 1
print("done")

secret_number = 10
guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
    guess = int(input("guess: "))
    guess_count += 1
    if guess == secret_number:
        print("you won")
        break
else:
    print('sorry try again')
