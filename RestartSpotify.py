import os
import distutils.spawn

if __name__ == '__main__':
    os.system(r"taskkill /f /im Spotify.exe")
    if not distutils.spawn.find_executable("Spotify.exe"):
        SpotifyDirectory = os.path.expanduser("~") + r'\AppData\Roaming\Spotify'
        AddPathCommand = 'SET PATH=%PATH%;' + SpotifyDirectory
        os.system(AddPathCommand)

    #assert distutils.spawn.find_executable("Spotify.exe")
    #Plz add Spotify.exe into Register or PATH https://docs.microsoft.com/en-us/windows/win32/shell/app-registration

    os.system("start Spotify.exe")
