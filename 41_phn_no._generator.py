def get_phn(country,area,first,last):
    return f"+{country} {area}-{first}-{last}"

phone_num = get_phn(country=91,area=741,first=1526,last=234)

print(phone_num)