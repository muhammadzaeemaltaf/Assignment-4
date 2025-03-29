"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.

Note that the user should type in a planet with 
the first letter as uppercase, and you do not need
to handle the case where a user types in something 
other than one of the planets (that is not Earth). 
"""


# Mars Weight

"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""
gravity_factors = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}


def main():
   
    earth_weight = float(input("Enter your weight on Earth: "))
    planet = input("Enter a planet: ").strip().title()

    planet_weight = earth_weight * gravity_factors[planet]
    rounded_weight = round(planet_weight, 2)

    print(f"Your weight on {planet} would be {rounded_weight}")

if __name__ == "__main__":
    main()