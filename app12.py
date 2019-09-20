high_income = False
good_income = True
if high_income and good_income:
    print('eligible for loan')
elif good_income:
    print('good income so eligible for loan')

high_income = False
good_income = True
if high_income or good_income:
        print('eligible for loan')

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print('eligible for loan')