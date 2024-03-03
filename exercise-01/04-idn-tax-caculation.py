def yearly_income(income) -> int:
    return int(income) * 12


def base_income_for_tax(status, dependency) -> int:
    PTKP = 54_000_000

    if status == 'single':
        return PTKP

    if int(dependency) == 0:
        return PTKP + 4_500_000
    elif int(dependency) == 1:
        return PTKP + (4_500_000 * 2)
    elif int(dependency) == 2:
        return PTKP + (4_500_000 * 3)
    else:
        return PTKP + (4_500_000 * 4)


def calculate_tax(amount_for_tax) -> int:
    if amount_for_tax <= 60_000_000:
        return amount_for_tax * 0.05
    elif 60_000_000 < amount_for_tax <= 250_000_000:
        return amount_for_tax * 0.15
    elif 250_000_000 < amount_for_tax <= 500_000_000:
        return amount_for_tax * 0.25
    elif 500_000_000 < amount_for_tax <= 5_000_000_000:
        return amount_for_tax * 0.30
    else:
        return amount_for_tax * 0.35


def is_valid_number(value) -> bool:
    """ Returns True if string is a number. """
    try:
        return int(value) > 0
    except ValueError:
        return True


def is_valid_status(value) -> bool:
    """ Returns True if is valid status. """
    try:
        return value == 'single' or value == 'married'
    except ValueError:
        return True


monthly_income = input("Masukan nilai penghasilan satu bulan : ")
if not is_valid_number(monthly_income):
    print("Not a valid input, please input number only")
    exit(1)

marital_status = input("Masukan status pernikahan, valid : married, single : ")
if not is_valid_status(marital_status):
    print("Not a valid input, please input only married or single")
    exit(1)

n_dependencies = input("Masukan jumlah tanggungan : ")
if not is_valid_number(monthly_income):
    print("Not a valid input, please input number only")
    exit(1)

yearly_income = yearly_income(monthly_income)
print("Penghasilan neto setahun:")
print(yearly_income)
print("\n")

ptkp = base_income_for_tax(marital_status, n_dependencies)
dependencies = n_dependencies if int(n_dependencies) <= 3 else 3
print(f"PTKP TK/{0 if marital_status == 'single' else dependencies}:")
print(ptkp)
print("\n")

income_for_tax = 0 if ptkp >= yearly_income else yearly_income - ptkp
print("Penghasilan Kena Pajak:")
print(income_for_tax)
print("\n")

tax_amount = calculate_tax(income_for_tax)
print("PPh 21 terutang setahun:")
print(tax_amount)
