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

    # NEW: starting from Minutes
    if tm == 2:
        print("Select your unit to convert to")
        print("1. Seconds")
        print("2. Hours")
        print("3. Days")
        print("4. Years")
        tm1 = int(input("Enter unit number \n"))

        if tm1 == 1:
            print("Enter value in Minutes")
            m = float(input())
            s = m * 60
            print("Value in Seconds is", s)
        if tm1 == 2:
            print("Enter value in Minutes")
            m = float(input())
            h = m / 60
            print("Value in Hours is", h)
        if tm1 == 3:
            print("Enter value in Minutes")
            m = float(input())
            d = m / 1440
            print("Value in Days is", d)
        if tm1 == 4:
            print("Enter value in Minutes")
            m = float(input())
            y = m / 525600
            print("Value in Years is", y)

    # NEW: starting from Hours
    if tm == 3:
        print("Select your unit to convert to")
        print("1. Seconds")
        print("2. Minutes")
        print("3. Days")
        print("4. Years")
        tm1 = int(input("Enter unit number \n"))

        if tm1 == 1:
            print("Enter value in Hours")
            h = float(input())
            s = h * 3600
            print("Value in Seconds is", s)
        if tm1 == 2:
            print("Enter value in Hours")
            h = float(input())
            m = h * 60
            print("Value in Minutes is", m)
        if tm1 == 3:
            print("Enter value in Hours")
            h = float(input())
            d = h / 24
            print("Value in Days is", d)
        if tm1 == 4:
            print("Enter value in Hours")
            h = float(input())
            y = h / 8760
            print("Value in Years is", y)

    # NEW: starting from Days
    if tm == 4:
        print("Select your unit to convert to")
        print("1. Seconds")
        print("2. Minutes")
        print("3. Hours")
        print("4. Years")
        tm1 = int(input("Enter unit number \n"))

        if tm1 == 1:
            print("Enter value in Days")
            d = float(input())
            s = d * 86400
            print("Value in Seconds is", s)
        if tm1 == 2:
            print("Enter value in Days")
            d = float(input())
            m = d * 1440
            print("Value in Minutes is", m)
        if tm1 == 3:
            print("Enter value in Days")
            d = float(input())
            h = d * 24
            print("Value in Hours is", h)
        if tm1 == 4:
            print("Enter value in Days")
            d = float(input())
            y = d / 365
            print("Value in Years is", y)

    # NEW: starting from Years
    if tm == 5:
        print("Select your unit to convert to")
        print("1. Seconds")
        print("2. Minutes")
        print("3. Hours")
        print("4. Days")
        tm1 = int(input("Enter unit number \n"))

        if tm1 == 1:
            print("Enter value in Years")
            y = float(input())
            s = y * 31536000
            print("Value in Seconds is", s)
        if tm1 == 2:
            print("Enter value in Years")
            y = float(input())
            m = y * 525600
            print("Value in Minutes is", m)
        if tm1 == 3:
            print("Enter value in Years")
            y = float(input())
            h = y * 8760
            print("Value in Hours is", h)
        if tm1 == 4:
            print("Enter value in Years")
            y = float(input())
            d = y * 365
            print("Value in Days is", d)

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

    # NEW: starting from Square Centimeters
    if a == 2:
        print("Select your unit to convert to")
        print("1. Square Millimeters")
        print("2. Square Meters")
        print("3. Square Kilometers")
        a1 = int(input("Enter unit number \n"))

        if a1 == 1:
            print("Enter value in Square Centimeters")
            cm2 = float(input())
            mm2 = cm2 * 100
            print("Value in Square Millimeters is", mm2)
        if a1 == 2:
            print("Enter value in Square Centimeters")
            cm2 = float(input())
            m2 = cm2 / 10000
            print("Value in Square Meters is", m2)
        if a1 == 3:
            print("Enter value in Square Centimeters")
            cm2 = float(input())
            km2 = cm2 / 10000000000
            print("Value in Square Kilometers is", km2)

    # NEW: starting from Square Meters
    if a == 3:
        print("Select your unit to convert to")
        print("1. Square Millimeters")
        print("2. Square Centimeters")
        print("3. Square Kilometers")
        a1 = int(input("Enter unit number \n"))

        if a1 == 1:
            print("Enter value in Square Meters")
            m2 = float(input())
            mm2 = m2 * 1000000
            print("Value in Square Millimeters is", mm2)
        if a1 == 2:
            print("Enter value in Square Meters")
            m2 = float(input())
            cm2 = m2 * 10000
            print("Value in Square Centimeters is", cm2)
        if a1 == 3:
            print("Enter value in Square Meters")
            m2 = float(input())
            km2 = m2 / 1000000
            print("Value in Square Kilometers is", km2)

    # NEW: starting from Square Kilometers
    if a == 4:
        print("Select your unit to convert to")
        print("1. Square Millimeters")
        print("2. Square Centimeters")
        print("3. Square Meters")
        a1 = int(input("Enter unit number \n"))

        if a1 == 1:
            print("Enter value in Square Kilometers")
            km2 = float(input())
            mm2 = km2 * 1000000000000
            print("Value in Square Millimeters is", mm2)
        if a1 == 2:
            print("Enter value in Square Kilometers")
            km2 = float(input())
            cm2 = km2 * 10000000000
            print("Value in Square Centimeters is", cm2)
        if a1 == 3:
            print("Enter value in Square Kilometers")
            km2 = float(input())
            m2 = km2 * 1000000
            print("Value in Square Meters is", m2)

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

    # NEW: starting from Cubic Centimeters
    if v == 2:
        print("Select your unit to convert to")
        print("1. Cubic Millimeters")
        print("2. Liters")
        print("3. Cubic Meters")
        print("4. Cubic Kilometers")
        v1 = int(input("Enter unit number \n"))

        if v1 == 1:
            print("Enter value in Cubic Centimeters")
            cm3 = float(input())
            mm3 = cm3 * 1000
            print("Value in Cubic Millimeters is", mm3)
        if v1 == 2:
            print("Enter value in Cubic Centimeters")
            cm3 = float(input())
            l = cm3 / 1000
            print("Value in Liters is", l)
        if v1 == 3:
            print("Enter value in Cubic Centimeters")
            cm3 = float(input())
            m3 = cm3 / 1000000
            print("Value in Cubic Meters is", m3)
        if v1 == 4:
            print("Enter value in Cubic Centimeters")
            cm3 = float(input())
            km3 = cm3 / 1000000000000000
            print("Value in Cubic Kilometers is", km3)

    # NEW: starting from Liters
    if v == 3:
        print("Select your unit to convert to")
        print("1. Cubic Millimeters")
        print("2. Cubic Centimeters")
        print("3. Cubic Meters")
        print("4. Cubic Kilometers")
        v1 = int(input("Enter unit number \n"))

        if v1 == 1:
            print("Enter value in Liters")
            l = float(input())
            mm3 = l * 1000000
            print("Value in Cubic Millimeters is", mm3)
        if v1 == 2:
            print("Enter value in Liters")
            l = float(input())
            cm3 = l * 1000
            print("Value in Cubic Centimeters is", cm3)
        if v1 == 3:
            print("Enter value in Liters")
            l = float(input())
            m3 = l / 1000
            print("Value in Cubic Meters is", m3)
        if v1 == 4:
            print("Enter value in Liters")
            l = float(input())
            km3 = l / 1000000000000
            print("Value in Cubic Kilometers is", km3)

    # NEW: starting from Cubic Meters
    if v == 4:
        print("Select your unit to convert to")
        print("1. Cubic Millimeters")
        print("2. Cubic Centimeters")
        print("3. Liters")
        print("4. Cubic Kilometers")
        v1 = int(input("Enter unit number \n"))

        if v1 == 1:
            print("Enter value in Cubic Meters")
            m3 = float(input())
            mm3 = m3 * 1000000000
            print("Value in Cubic Millimeters is", mm3)
        if v1 == 2:
            print("Enter value in Cubic Meters")
            m3 = float(input())
            cm3 = m3 * 1000000
            print("Value in Cubic Centimeters is", cm3)
        if v1 == 3:
            print("Enter value in Cubic Meters")
            m3 = float(input())
            l = m3 * 1000
            print("Value in Liters is", l)
        if v1 == 4:
            print("Enter value in Cubic Meters")
            m3 = float(input())
            km3 = m3 / 1000000000
            print("Value in Cubic Kilometers is", km3)

    # NEW: starting from Cubic Kilometers
    if v == 5:
        print("Select your unit to convert to")
        print("1. Cubic Millimeters")
        print("2. Cubic Centimeters")
        print("3. Liters")
        print("4. Cubic Meters")
        v1 = int(input("Enter unit number \n"))

        if v1 == 1:
            print("Enter value in Cubic Kilometers")
            km3 = float(input())
            mm3 = km3 * 1000000000000000000
            print("Value in Cubic Millimeters is", mm3)
        if v1 == 2:
            print("Enter value in Cubic Kilometers")
            km3 = float(input())
            cm3 = km3 * 1000000000000000
            print("Value in Cubic Centimeters is", cm3)
        if v1 == 3:
            print("Enter value in Cubic Kilometers")
            km3 = float(input())
            l = km3 * 1000000000000
            print("Value in Liters is", l)
        if v1 == 4:
            print("Enter value in Cubic Kilometers")
            km3 = float(input())
            m3 = km3 * 1000000000
            print("Value in Cubic Meters is", m3)

elif x == 7:
    print("Exiting converter. Goodbye!")
