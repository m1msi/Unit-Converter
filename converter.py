print("Choose your category\n")
print("1. Length")
print("2. Temperature")
print("3. Weight")
print("4. Time")
print("5. Area")
print("6. Volume")
print("7. Exit\n")

x = int(input("Enter category number \n"))

# Length
if x == 1:
    print("Select your unit")
    print("1. Milimeters")
    print("2. Centimeters")
    print("3. Meters")
    print("4. Kilometers")
    l = int(input("Enter unit number \n"))
    print("Select your unit to convert to")
    if l == 1:
        print("1. Centimeters")
        print("2. Meters")
        print("3. Kilometers")
        l1 = int(input("Enter unit number \n"))
        if l1 == 1:
            print("Enter value in Milimeters")
            mm = float(input())
            cm = mm / 10
            print("Value in Centimeters is", cm)
        if l1 == 2:
            print("Enter value in Milimeters")
            mm = float(input())
            m = mm / 1000
            print("Value in Meters is", m)
        if l1 == 3:
            print("Enter value in Milimeters")
            mm = float(input())
            km = mm / 1000000
            print("Value in Kilometers is", km)
    if l == 2:
        print("1. Milimeters")
        print("2. Meters")
        print("3. Kilometers")
        l1 = int(input("Enter unit number \n"))
        if l1 == 1:
            print("Enter value in Centimeters")
            cm = float(input())
            mm = cm * 10
            print("Value in Milimeters is", mm)
        if l1 == 2:
            print("Enter value in Centimeters")
            cm = float(input())
            m = cm / 100
            print("Value in Meters is", m)
        if l1 == 3:
            print("Enter value in Centimeters")
            cm = float(input())
            km = cm / 100000
            print("Value in Kilometers is", km)
    if l == 3:
        print("1. Milimeters")
        print("2. Centimeters")
        print("3. Kilometers")
        l1 = int(input("Enter unit number \n"))
        if l1 == 1:
            print("Enter value in Meters")
            m = float(input())
            mm = m * 1000
            print("Value in Milimeters is", mm)
        if l1 == 2:
            print("Enter value in Meters")
            m = float(input())
            cm = m * 100
            print("Value in Centimeters is", cm)
        if l1 == 3:
            print("Enter value in Meters")
            m = float(input())
            km = m / 1000
            print("Value in Kilometers is", km)
    if l == 4:
        print("1. Milimeters")
        print("2. Centimeters")
        print("3. Meters")
        l1 = int(input("Enter unit number \n"))
        if l1 == 1:
            print("Enter value in Kilometers")
            km = float(input())
            mm = km * 1000000
            print("Value in Milimeters is", mm)
        if l1 == 2:
            print("Enter value in Kilometers")
            km = float(input())
            cm = km * 100000
            print("Value in Centimeters is", cm)
        if l1 == 3:
            print("Enter value in Kilometers")
            km = float(input())
            m = km * 1000
            print("Value in Meters is", m)

# Temperature
elif x == 2:
    print("Select your unit")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    t = int(input("Enter unit number \n"))
    if t == 1:
        print("Select your unit to convert to")
        print("1. Fahrenheit")
        print("2. Kelvin")
        t1 = int(input("Enter unit number \n"))
        if t1 == 1:
            print("Enter value in Celsius")
            c = float(input())
            f = (c * 9/5) + 32
            print("Value in Fahrenheit is", f)
        if t1 == 2:
            print("Enter value in Celsius")
            c = float(input())
            k = c + 273.15
            print("Value in Kelvin is", k)
    if t == 2:
        print("Select your unit to convert to")
        print("1. Celsius")
        print("2. Kelvin")
        t1 = int(input("Enter unit number \n"))
        if t1 == 1:
            print("Enter value in Fahrenheit")
            f = float(input())
            c = (f - 32) * 5/9
            print("Value in Celsius is", c)
        if t1 == 2:
            print("Enter value in Fahrenheit")
            f = float(input())
            k = (f - 32) * 5/9 + 273.15
            print("Value in Kelvin is", k)
    if t == 3:
        print("Select your unit to convert to")
        print("1. Celsius")
        print("2. Fahrenheit")
        t1 = int(input("Enter unit number \n"))
        if t1 == 1:
            print("Enter value in Kelvin")
            k = float(input())
            c = k - 273.15
            print("Value in Celsius is", c)
        if t1 == 2:
            print("Enter value in Kelvin")
            k = float(input())
            f = (k - 273.15) * 9/5 + 32
            print("Value in Fahrenheit is", f)

# Weight
elif x == 3:
    print("Select your unit")
    print("1. Miligrams")
    print("2. Grams")
    print("3. Kilograms")
    print("4. Tonnes")
    w = int(input("Enter unit number \n"))
    if w == 1:
        print("Select your unit to convert to")
        print("1. Grams")
        print("2. Kilograms")
        print("3. Tonnes")
        w1 = int(input("Enter unit number \n"))
        if w1 == 1:
            print("Enter value in Miligrams")
            mg = float(input())
            g = mg / 1000
            print("Value in Grams is", g)
        if w1 == 2:
            print("Enter value in Miligrams")
            mg = float(input())
            kg = mg / 1000000
            print("Value in Kilograms is", kg)
        if w1 == 3:
            print("Enter value in Miligrams")
            mg = float(input())
            t = mg / 1000000000
            print("Value in Tonnes is", t)
    if w == 2:
        print("Select your unit to convert to")
        print("1. Miligrams")
        print("2. Kilograms")
        print("3. Tonnes")
        w1 = int(input("Enter unit number \n"))
        if w1 == 1:
            print("Enter value in Grams")
            g = float(input())
            mg = g * 1000
            print("Value in Miligrams is", mg)
        if w1 == 2:
            print("Enter value in Grams")
            g = float(input())
            kg = g / 1000
            print("Value in Kilograms is", kg)
        if w1 == 3:
            print("Enter value in Grams")
            g = float(input())
            t = g / 1000000
            print("Value in Tonnes is", t)
    if w == 3:
        print("Select your unit to convert to")
        print("1. Miligrams")
        print("2. Grams")
        print("3. Tonnes")
        w1 = int(input("Enter unit number \n"))
        if w1 == 1:
            print("Enter value in Kilograms")
            kg = float(input())
            mg = kg * 1000000
            print("Value in Miligrams is", mg)
        if w1 == 2:
            print("Enter value in Kilograms")
            kg = float(input())
            g = kg * 1000
            print("Value in Grams is", g)
        if w1 == 3:
            print("Enter value in Kilograms")
            kg = float(input())
            t = kg / 1000
            print("Value in Tonnes is", t)
    if w == 4:
        print("Select your unit to convert to")
        print("1. Miligrams")
        print("2. Grams")
        print("3. Kilograms")
        w1 = int(input("Enter unit number \n"))
        if w1 == 1:
            print("Enter value in Tonnes")
            t = float(input())
            mg = t * 1000000000
            print("Value in Miligrams is", mg)
        if w1 == 2:
            print("Enter value in Tonnes")
            t = float(input())
            g = t * 1000000
            print("Value in Grams is", g)
        if w1 == 3:
            print("Enter value in Tonnes")
            t = float(input())
            kg = t * 1000
            print("Value in Kilograms is", kg)

# Time
elif x == 4:
    print("Select your unit")
    print("1. Seconds")
    print("2. Minutes")
    print("3. Hours")
    print("4. Days")
    print("5. Years")
    tm = int(input("Enter unit number \n"))
    if tm == 1:
        print("Select your unit to convert to")
        print("1. Minutes")
        print("2. Hours")
        print("3. Days")
        print("4. Years")
        tm1 = int(input("Enter unit number \n"))
        if tm1 == 1:
            print("Enter value in Seconds")
            s = float(input())
            m = s / 60
            print("Value in Minutes is", m)
        if tm1 == 2:
            print("Enter value in Seconds")
            s = float(input())
            h = s / 3600
            print("Value in Hours is", h)
        if tm1 == 3:
            print("Enter value in Seconds")
            s = float(input())
            d = s / 86400
            print("Value in Days is", d)
        if tm1 == 4:
            print("Enter value in Seconds")
            s = float(input())
            y = s / 31536000
            print("Value in Years is", y)

# Area
elif x == 5:
    print("Select your unit")
    print("1. Square Millimeters")
    print("2. Square Centimeters")
    print("3. Square Meters")
    print("4. Square Kilometers")
    a = int(input("Enter unit number \n"))
    if a == 1:
        print("Select your unit to convert to")
        print("1. Square Centimeters")
        print("2. Square Meters")
        print("3. Square Kilometers")
        a1 = int(input("Enter unit number \n"))
        if a1 == 1:
            print("Enter value in Square Millimeters")
            mm2 = float(input())
            cm2 = mm2 / 100
            print("Value in Square Centimeters is", cm2)
        if a1 == 2:
            print("Enter value in Square Millimeters")
            mm2 = float(input())
            m2 = mm2 / 1000000
            print("Value in Square Meters is", m2)
        if a1 == 3:
            print("Enter value in Square Millimeters")
            mm2 = float(input())
            km2 = mm2 / 1000000000000
            print("Value in Square Kilometers is", km2)

# Volume
elif x == 6:
    print("Select your unit")
    print("1. Cubic Millimeters")
    print("2. Cubic Centimeters")
    print("3. Liters")
    print("4. Cubic Meters")
    print("5. Cubic Kilometers")
    v = int(input("Enter unit number \n"))
    if v == 1:
        print("Select your unit to convert to")
        print("1. Cubic Centimeters")
        print("2. Liters")
        print("3. Cubic Meters")
        print("4. Cubic Kilometers")
        v1 = int(input("Enter unit number \n"))
        if v1 == 1:
            print("Enter value in Cubic Millimeters")
            mm3 = float(input())
            cm3 = mm3 / 1000
            print("Value in Cubic Centimeters is", cm3)
        if v1 == 2:
            print("Enter value in Cubic Millimeters")
            mm3 = float(input())
            l = mm3 / 1000000
            print("Value in Liters is", l)
        if v1 == 3:
            print("Enter value in Cubic Millimeters")
            mm3 = float(input())
            m3 = mm3 / 1000000000
            print("Value in Cubic Meters is", m3)
        if v1 == 4:
            print("Enter value in Cubic Millimeters")
            mm3 = float(input())
            km3 = mm3 / 1000000000000000000
            print("Value in Cubic Kilometers is", km3)

elif x == 7:
    print("Exiting converter. Goodbye!")