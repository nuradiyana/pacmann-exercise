nik_1 = 1571011709860003
nik_2 = 2404075109910009


def remove_region_from_nik(value):
    nik = str(value)

    return nik[6:len(nik)]


def extract_birth_date_from_nik(value):
    date = value[0:2]

    if int(date) >= 41:
        return f"{int(date) - 40}-{value[2:4]}-{value[4:6]}"

    return f"{date}-{value[2:4]}-{value[4:6]}"


def get_month(month):
    if 1 < month > 12:
        return "Invalid month number"

    months = {
        1: "Januari",
        2: "Februari",
        3: "Maret",
        4: "April",
        5: "Mei",
        6: "Juni",
        7: "Juli",
        8: "Agustus",
        9: "September",
        10: "Oktober",
        11: "November",
        12: "Desember"
    }

    return months[month]


def is_male(value):
    try:
        date = int(value)

        if 1 <= date <= 31:
            return True
    except ValueError:
        print('Invalid birth date')
        exit(1)


def is_female(value):
    try:
        date = int(value)

        if 41 <= date <= 71:
            return True
    except ValueError:
        print('Invalid birth date')
        exit(1)


def get_gender(value):
    if is_male(value):
        return 'Male'
    elif is_female(value):
        return 'Female'
    else:
        return 'Invalid gender'


print(f"- NIK 1 : {nik_1}")
print(f"- NIK 2 : {nik_2}")
print("-" * 30)

nik_1_without_region = remove_region_from_nik(nik_1)
nik_2_without_region = remove_region_from_nik(nik_2)

full_birth_date_1 = extract_birth_date_from_nik(nik_1_without_region)
full_birth_date_2 = extract_birth_date_from_nik(nik_2_without_region)

print("Date of Birth")
print(f"- NIK 1 : {full_birth_date_1}")
print(f"- NIK 2 : {full_birth_date_2}")
print("-" * 30)

print("Gender")
print(f"- NIK 1 : {get_gender(nik_1_without_region[0:2])}")
print(f"- NIK 2 : {get_gender(nik_2_without_region[0:2])}")
print("-" * 30)

gender_1 = get_gender(nik_1_without_region[0:2])
gender_2 = get_gender(nik_2_without_region[0:2])
same_gender = "Yes" if gender_1 == gender_2 else "No"
print("Do they have similar gender?")
print(f"{same_gender}")
print("-" * 30)

month_1 = full_birth_date_1[3:5]
month_2 = full_birth_date_2[3:5]

print("Do they have similar month of birth?")
if month_1 == month_2:
    print(f"Yes, it is on {get_month(int(month_1))}")
else:
    print(f"No, NIK 1 is on {get_month(int(month_1))} and NIK 2 is on {get_month(int(month_2))}")

print("-" * 30)
