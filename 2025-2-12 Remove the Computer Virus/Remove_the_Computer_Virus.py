import re
def remove_virus(s):
    files = s[10:].split(", ")
    regex = r"(?<!anti)(?<!^not)(?:virus|malware)"
    clean_files = [s for s in files if not re.search(regex,s)]
    return f"PC Files: {", ".join(clean_files) if clean_files else "Empty"}"

#Test case
assert remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg")  == "PC Files: spotifysetup.exe, dog.jpg", "remove_virus doens't work correctly"
assert remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ") == "PC Files: antivirus.exe, cat.pdf", "remove_virus doens't work correctly"
assert remove_virus("PC Files: notvirus.exe, funnycat.gif") == "PC Files: notvirus.exe, funnycat.gif", "remove_virus doens't work correctly"