# -*- coding: utf-8 -*-

# initializing empty envelops
necessityEnvelop = 0  # NEC, необхідні витрати
freedomEnvelop = 0    # FFA, фінансова свобода
educationEnvelop = 0  # EDU, освіта
longTermEnvelop = 0   # LTSS, резерв та на великі покупки
playEnvelop = 0       # PLAY, розваги
giveEnvelop = 0       # GIVE, подарунки


# initializing percent rate
necRate = 0.55
ffaRate = 0.1
eduRate = 0.1
ltssRate = 0.1
playRate = 0.1
giveRate = 0.05


# initializing expected income, expected necessity and other amounts
expectedIncome = 1000


#invitation, greetings etc.
print ("""Hello.\n
We gonna fill your envelops by the money you input here!\n
Please input your amounts of money income and see the results.\n
Press Ctrl+c to exit script.
\n\n Enter the amount please:""", end=" ")
amount = int(input())


# final output
print(f"""At the end we have:\n
    Necessity Envelop has:                       {amount * necRate}\n
    Financial Freedom Envelop has:               {amount * ffaRate}\n
    Education Envelop has:                       {amount * eduRate}\n
    Long Term Saving for Spending Envelop has:   {amount * ltssRate}\n
    Play Envelop has:                            {amount * playRate}\n
    Give Envelop has:                            {amount * giveRate}\n
    _______________________________________________________________\n
    Thanks for using our software :)""")
