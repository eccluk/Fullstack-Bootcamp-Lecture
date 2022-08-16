
# We've
print("""We have 3 Banks onboarded:
    - Lloyds
    - Barclays
    - Starling
""")
Banks = ["Lloyds", "Barclays", "Starling"]
selectBank = input("Enter Bank Name: ")

for b in Banks:
    if selectBank == b:
        print("Yes, you can open an account with us")
        break
else:
    print(f"Sorry, we don't operate {selectBank} Bank")
