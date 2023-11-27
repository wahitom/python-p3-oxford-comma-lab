def oxford_comma(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        list_items = []
        list_items = ' and '.join(items)
        return list_items
    else:
        # add the items to the item list except the last one 
        joined_item = ", ".join(items[:-1])

        #Add and just before the last item
        oxford_string = f"{joined_item}, and {items[-1]}"

        return oxford_string
    


oxford_comma(["fiddleheads", "okra", "kohlrabi"])
