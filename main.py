from PyAuto_main import time_app

runs = 2
laps = []
apps = [
    ('C:/Program Files/Apache NetBeans/bin/netbeans64.exe', 'net beans2.png', 'Net Beans'),
    ('C:/Users/Omar/Documents/Microsoft VS Code/code.exe', 'VS.png', 'Visual Studio code'),
    ('C:/Users/Omar/AppData/Local/Microsoft/Teams/previous/Teams.exe', 'teams.png', 'Teams'),
    ('C:/Users/Omar/AppData/Local/Discord/app-1.0.9012/Discord.exe', 'discord.png', 'Discord'),
    ('C:/Users/Omar/AppData/Local/Programs/Messenger/Messenger.exe', 'messenger.png', 'Messenger'),
]

for app in apps:
    for _ in range(runs):
        lap = time_app(app[0], app[1])
        laps.append(lap)

    average = sum(laps) / runs
    print(laps)
    laps = []
    print(f'average load time for {app[2]} is: {average}')
