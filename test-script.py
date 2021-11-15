import script as cal

def test_all(x,y):
    if cal.add(x,y)==x+y and cal.subtract(x,y)==x-y and cal.multiply(x,y)==x*y and cal.divide(x,y)==x/y:
        return True
    else:
        return False

test_all(12,23)
test_all(-12,23)
test_all(12,-23)
test_all(-12,-23)