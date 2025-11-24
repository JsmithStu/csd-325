# city_functions.py

def city_country(city, country, population=None, language=None):
    """
    Return a formatted location string.

    Examples:
    - 'Santiago, Chile'
    - 'Santiago, Chile - population 5000000'
    - 'Santiago, Chile - population 5000000, Spanish'
    """
    formatted_city = city.title()
    formatted_country = country.title()

    location = f"{formatted_city}, {formatted_country}"

    if population is not None:
        location += f" - population {population}"

    if language is not None:
        location += f", {language.title()}"

    return location


# Final required calls:
# 1) City, Country
print(city_country('santiago', 'chile'))

# 2) City, Country, Population
print(city_country('tokyo', 'japan', 14000000))

# 3) City, Country, Population, Language
print(city_country('berlin', 'germany', 3600000, 'german'))
