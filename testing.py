# number_test = 1.5

# print(f"This one should be a plain integer {int(number_test)}")

# print(f"This one should be a float still {number_test}")

# number_test = int(number_test)

# print(f"This one should be a plain integer {number_test}")


# word1 = 'word 1'
# word2 = 'word 2'

# print("{:<5} other stuff here {:<35}".format(word1,word2))

# name1 = "Alice"
# name2 = "Bob"
# print("{:<20}{:<40}".format(name1, name2))


print(sum([1,2,3]))


        # 5. Check the customer's input
        if keep_ordering.isalpha():
                # Keep ordering, utilized starts with to allow for full words, i.e 'yes'
            if keep_ordering.lower().startswith("y"):
                place_order = True
                break
                # Exit the keep ordering question loop, utilized starts with to allow for full words, i.e 'no'
            elif keep_ordering.lower().startswith("n"):
                place_order = False
                print("\nThank you very much for visiting the veriety food truck!")
                break
                # Complete the order
                # Since the customer decided to stop ordering, thank them for
                # their order
                # Exit the keep ordering question loop
                
                #if they did not enter y or n (or the other entries that could be valid)
            else: 
                print("\nPlease Try again")