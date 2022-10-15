lst_in = input().split()

def verify_data(x):
    try:
        return int(x)
    except ValueError:
        try:
            return float(x)
        except ValueError:
            return x

lst_out = list(map(verify_data, lst_in))

print(lst_out)
