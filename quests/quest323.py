"""
Write a function convert_temp(temp, from_scale, to_scale) converting temperature from one scale to another. Return converted temp value.

Round converted temp value to an integer(!).

Reading: http://en.wikipedia.org/wiki/Conversion_of_units_of_temperature
"""
def K_to_K(kelvin):
    return kelvin

def C_to_K(celsius):
    kelvin = celsius + 273.15
    return kelvin

def K_to_C(kelvin):
    celsius = kelvin - 273.15
    return celsius

def F_to_K(fahrenheit):
    kelvin = 5/9 * (fahrenheit + 459.67)
    return kelvin

def K_to_F(kelvin):
    fahrenheit = 9/5 * kelvin -  459.67
    return fahrenheit

def R_to_K(rankine):
    kelvin = 5/9 * rankine
    return kelvin

def K_to_R(kelvin):
    rankine = kelvin * 9/5
    return rankine

def De_to_K(delisle):
    kelvin = 373.15 - delisle * 2/3
    return kelvindef K_to_K(kelvin):
    return kelvin

def C_to_K(celsius):
    kelvin = celsius + 273.15
    return kelvin

def K_to_C(kelvin):
    celsius = kelvin - 273.15
    return celsius

def F_to_K(fahrenheit):
    kelvin = 5/9 * (fahrenheit + 459.67)
    return kelvin

def K_to_F(kelvin):
    fahrenheit = 9/5 * kelvin -  459.67
    return fahrenheit

def R_to_K(rankine):
    kelvin = 5/9 * rankine
    return kelvin

def K_to_R(kelvin):
    rankine = kelvin * 9/5
    return rankine

def De_to_K(delisle):
    kelvin = 373.15 - delisle * 2/3
    return kelvin

def K_to_De(kelvin):
    delisle = (373.15 - kelvin) * 3/2
    return delisle

def N_to_K(newton):
    kelvin = 273.15 + 100/33 * newton
    return kelvin

def K_to_N(kelvin):
    newton = (kelvin - 273.15) * 33/100
    return newton

def Re_to_K(reaumur):
    kelvin = 273.15 + 5/4 * reaumur
    return kelvin

def K_to_Re(kelvin):
    reaumur = (kelvin - 273.15) * 4/5
    return reaumur

def Ro_to_K(romer):
    kelvin = 273.15 + 40/21 * (romer - 7.5)
    return kelvin

def K_to_Ro(kelvin):
    romer = (kelvin - 273.15) * 21/40 + 7.5
    return romer

def convert_temp(temp, from_scale, to_scale):
    TO_KELVIN = {
        'C': C_to_K,
        'K': K_to_K,
        'F': F_to_K,
        'N': N_to_K,
        'R': R_to_K,
        'Re': Re_to_K,
        'De': De_to_K,
        'Ro': Ro_to_K,
    }
    FROM_KELVIN = {
        'C': K_to_C,
        'K': K_to_K,
        'F': K_to_F,
        'N': K_to_N,
        'R': K_to_R,
        'Re': K_to_Re,
        'De': K_to_De,
        'Ro': K_to_Ro,

    }
    kelvin = TO_KELVIN.get(from_scale)(temp)
    other = FROM_KELVIN.get(to_scale)(kelvin)
    return round(other)

def K_to_De(kelvin):
    delisle = (373.15 - kelvin) * 3/2
    return delisle

def N_to_K(newton):
    kelvin = 273.15 + 100/33 * newton
    return kelvin

def K_to_N(kelvin):
    newton = (kelvin - 273.15) * 33/100
    return newton

def Re_to_K(reaumur):
    kelvin = 273.15 + 5/4 * reaumur
    return kelvin

def K_to_Re(kelvin):
    reaumur = (kelvin - 273.15) * 4/5
    return reaumur

def Ro_to_K(romer):
    kelvin = 273.15 + 40/21 * (romer - 7.5)
    return kelvin

def K_to_Ro(kelvin):
    romer = (kelvin - 273.15) * 21/40 + 7.5
    return romer

def convert_temp(temp, from_scale, to_scale):
    TO_KELVIN = {
        'C': C_to_K,
        'K': K_to_K,
        'F': F_to_K,
        'N': N_to_K,
        'R': R_to_K,
        'Re': Re_to_K,
        'De': De_to_K,
        'Ro': Ro_to_K,
    }
    FROM_KELVIN = {
        'C': K_to_C,
        'K': K_to_K,
        'F': K_to_F,
        'N': K_to_N,
        'R': K_to_R,
        'Re': K_to_Re,
        'De': K_to_De,
        'Ro': K_to_Ro,

    }
    kelvin = TO_KELVIN.get(from_scale)(temp)
    other = FROM_KELVIN.get(to_scale)(kelvin)
    return round(other)
