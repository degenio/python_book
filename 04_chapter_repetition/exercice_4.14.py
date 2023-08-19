montant_remis = int(input('Enter the amount given: '))
montant_total = int(input('Enter the total amount: '))
change = montant_remis - montant_total

# Calculate the number of each denomination
cp_vingt = change // 20
cp_dix = (change % 20) // 10
cp_cinq = (change % 10) // 5
cp_un = change - cp_vingt * 20 - cp_dix * 10 - cp_cinq * 5

# Display the breakdown of change
print('Twenties: {}, Tens: {}, Fives: {}, Ones: {}'.format(
    cp_vingt, cp_dix, cp_cinq, cp_un))
