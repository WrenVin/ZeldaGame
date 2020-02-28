import cx_Freeze
executables = [cx_Freeze.Executable('main.py')]
cx_Freeze.setup(
    name='ZeldaGame',
    options = {'build_exe': {'packages':['pygame'],
                            'include_files':['EasyMap.txt', 'HardMap.txt', 'ModerateMap.txt', 'snd/background.mp3', 'snd/victory.mp3', 'snd/walk.mp3', 'img/character.png', 'img/grass.png', 'img/Overworld.png', 'img/sword.png']}},
    executables = executables
                            )