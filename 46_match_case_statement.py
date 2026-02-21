# match case statement(switch) = a alternative to use many elif statements
#                                execute some code if avalue matches a "case"
#                                benefits : clearer and syntax is more readable

def day_of_week(day):
    match day:
        case "sunday":return "its sunday funday holiday"
        case "saturday":return "its funday holiday"
        case _: return "week day , no holiday"
        # _ => wild card
print(day_of_week("tuesday")) 