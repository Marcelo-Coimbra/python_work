print("Languages:\n\n\tPython;\n\tC;\n\tJavaScript.\n")
favorite_language = ' python'
print(favorite_language)
print(favorite_language.lstrip())
print(f'Minha língua favorita é {favorite_language.strip()}\n')

nostarch_url = 'https://nostarch.com'
site = nostarch_url.removeprefix('https://')
print(site + "\n")

universe_age = 14_000_000_000
print(universe_age)