import shelve

# bit = ["bacon","lettuce","tomato","bread"]
# beans_on_toast = ["beans","bread"]
# scrambled_eggs = ["eggs","butter","milk"]
#soup = ["tin of soup"]
# pasta = ["pasta","cheese"]

with shelve.open('recipes', writeback=True) as recipes:
    # recipes["bit"]= bit
    # recipes["beans on toast"]= beans_on_toast
    # recipes["scrambled eggs"]= scrambled_eggs
    #recipes["soup"]= soup
    # recipes["pasta"]= pasta



    # recipes["bit"].append("butter") # note that these are not doing what they should be doing
    # recipes["pasta"].append("tomato")   #hence we'll comment these and see other way to do it

    # temp_list= recipes["bit"]
    # temp_list.append('butter')
    # recipes["bit"] = temp_list  #see, not butter has been added to the "bit"
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes['pasta'] = temp_list    #see, not tomato has been added to the "pasta"

#pow that they are added, we can comment the above code

    recipes['soup'].append("Krouton")       #this works ONLY WHEN "WRITEBACK=TRUE" is there in the open statement
    for snack in recipes:
        print(snack,recipes[snack])
