import os

if __name__ == '__main__':
    os.system(r"taskkill /f /im Spotify.exe")
    #Plz add Spotify.exe into Register or PATH https://docs.microsoft.com/en-us/windows/win32/shell/app-registration
    os.system("start Spotify.exe")
