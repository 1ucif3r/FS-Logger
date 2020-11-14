import random

figlet_ansi_shadow = """

███████╗███████╗██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
██╔════╝██╔════╝██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
█████╗  ███████╗██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
██╔══╝  ╚════██║██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
██║     ███████║███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
╚═╝     ╚══════╝╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝                                                                                                                                                                 
"""

figlet_big = """
 ______    _____   _         ____     _____    _____   ______   _____  
|  ____|  / ____| | |       / __ \   / ____|  / ____| |  ____| |  __ \ 
| |__    | (___   | |      | |  | | | |  __  | |  __  | |__    | |__) |
|  __|    \___ \  | |      | |  | | | | |_ | | | |_ | |  __|   |  _  / 
| |       ____) | | |____  | |__| | | |__| | | |__| | | |____  | | \ \ 
|_|      |_____/  |______|  \____/   \_____|  \_____| |______| |_|  \_\                                                                        
"""

figlet_bloody = """

  █████▒ ██████  ██▓     ▒█████    ▄████   ▄████ ▓█████  ██▀███  
▓██   ▒▒██    ▒ ▓██▒    ▒██▒  ██▒ ██▒ ▀█▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
▒████ ░░ ▓██▄   ▒██░    ▒██░  ██▒▒██░▄▄▄░▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
░▓█▒  ░  ▒   ██▒▒██░    ▒██   ██░░▓█  ██▓░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
░▒█░   ▒██████▒▒░██████▒░ ████▓▒░░▒▓███▀▒░▒▓███▀▒░▒████▒░██▓ ▒██▒
 ▒ ░   ▒ ▒▓▒ ▒ ░░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
 ░     ░ ░▒  ░ ░░ ░ ▒  ░  ░ ▒ ▒░   ░   ░   ░   ░  ░ ░  ░  ░▒ ░ ▒░
 ░ ░   ░  ░  ░    ░ ░   ░ ░ ░ ▒  ░ ░   ░ ░ ░   ░    ░     ░░   ░ 
             ░      ░  ░    ░ ░        ░       ░    ░  ░   ░     
                                                                 
"""

figlet_doom = """
______  _____  _      _____  _____  _____  _____ ______ 
|  ___|/  ___|| |    |  _  ||  __ \|  __ \|  ___|| ___ \
| |_   \ `--. | |    | | | || |  \/| |  \/| |__  | |_/ /
|  _|   `--. \| |    | | | || | __ | | __ |  __| |    / 
| |    /\__/ /| |____\ \_/ /| |_\ \| |_\ \| |___ | |\ \ 
\_|    \____/ \_____/ \___/  \____/ \____/\____/ \_| \_|                                                       
"""

figlet_drpepper = """
 ___  ___  _    ___  ___   ___   ___  ___ 
| __>/ __>| |  | . |/  _> /  _> | __>| . \
| _> \__ \| |_ | | || <_/\| <_/\| _> |   /
|_|  <___/|___|`___'`____/`____/|___>|_\_\                                         
"""

figlet_ogre = """
   ___  __       __     ___    ___    ___    __    __  
  / __\/ _\     / /    /___\  / _ \  / _ \  /__\  /__\ 
 / _\  \ \     / /    //  // / /_\/ / /_\/ /_\   / \// 
/ /    _\ \   / /___ / \_// / /_\\ / /_\\ //__  / _  \ 
\/     \__/   \____/ \___/  \____/ \____/ \__/  \/ \_/                                                       
"""

figlet_slant = """
    ______   _____    __    ____    ______   ______    ______    ____ 
   / ____/  / ___/   / /   / __ \  / ____/  / ____/   / ____/   / __ \
  / /_      \__ \   / /   / / / / / / __   / / __    / __/     / /_/ /
 / __/     ___/ /  / /___/ /_/ / / /_/ /  / /_/ /   / /___    / _, _/ 
/_/       /____/  /_____/\____/  \____/   \____/   /_____/   /_/ |_|                                                                                                                                          
"""

figlet_small = """
 ___ ___ _    ___   ___  ___ ___ ___ 
| __/ __| |  / _ \ / __|/ __| __| _ \
| _|\__ \ |_| (_) | (_ | (_ | _||   /
|_| |___/____\___/ \___|\___|___|_|_\                                      
"""

figlet_smslant = """
   ____   ____   __   ____   _____  _____   ____   ___ 
  / __/  / __/  / /  / __ \ / ___/ / ___/  / __/  / _ \
 / _/   _\ \   / /__/ /_/ // (_ / / (_ /  / _/   / , _/
/_/    /___/  /____/\____/ \___/  \___/  /___/  /_/|_|                                                       
"""

figlet_standard = """

 _____ ____  _     ___   ____  ____ _____ ____  
|  ___/ ___|| |   / _ \ / ___|/ ___| ____|  _ \ 
| |_  \___ \| |  | | | | |  _| |  _|  _| | |_) |
|  _|  ___) | |__| |_| | |_| | |_| | |___|  _ < 
|_|   |____/|_____\___/ \____|\____|_____|_| \_\                                                 
"""													

figlet_Basic = """

d88888b .d8888. db       .d88b.   d888b   d888b  d88888b d8888b. 
88'     88'  YP 88      .8P  Y8. 88' Y8b 88' Y8b 88'     88  `8D 
88ooo   `8bo.   88      88    88 88      88      88ooooo 88oobY' 
88~~~     `Y8b. 88      88    88 88  ooo 88  ooo 88~~~~~ 88`8b   
88      db   8D 88booo. `8b  d8' 88. ~8~ 88. ~8~ 88.     88 `88. 
YP      `8888Y' Y88888P  `Y88P'   Y888P   Y888P  Y88888P 88   YD 
"""                                                                

figlet_alligator = """

::::::::::  ::::::::  :::         ::::::::   ::::::::   ::::::::  :::::::::: :::::::::  
:+:        :+:    :+: :+:        :+:    :+: :+:    :+: :+:    :+: :+:        :+:    :+: 
+:+        +:+        +:+        +:+    +:+ +:+        +:+        +:+        +:+    +:+ 
:#::+::#   +#++:++#++ +#+        +#+    +:+ :#:        :#:        +#++:++#   +#++:++#:  
+#+               +#+ +#+        +#+    +#+ +#+   +#+# +#+   +#+# +#+        +#+    +#+ 
#+#        #+#    #+# #+#        #+#    #+# #+#    #+# #+#    #+# #+#        #+#    #+# 
###         ########  ##########  ########   ########   ########  ########## ###    ### 
"""

figlet_speed = """

________________________ _______ ____________________________________ 
___  ____/__  ___/___  / __  __ \__  ____/__  ____/___  ____/___  __ \
__  /_    _____ \ __  /  _  / / /_  / __  _  / __  __  __/   __  /_/ /
_  __/    ____/ / _  /___/ /_/ / / /_/ /  / /_/ /  _  /___   _  _, _/ 
/_/       /____/  /_____/\____/  \____/   \____/   /_____/   /_/ |_|  
"""

figlet_stronger = """

._______.________.___    ._______  ._____  ._____  ._______.______  
:_ ____/|    ___/|   |   : .___  \ :_ ___\ :_ ___\ : .____/: __   \ 
|   _/  |___    \|   |   | :   |  ||   |___|   |___| : _/\ |  \____|
|   |   |       /|   |/\ |     :  ||   /  ||   /  ||   /  \|   :  \ 
|_. |   |__:___/ |   /  \ \_. ___/ |. __  ||. __  ||_.: __/|   |___\
  :/       :     |______/   :/      :/ |. | :/ |. |   :/   |___|    
  :                         :       :   :/  :   :/                  
                                        :       :                   
"""

def get_banner():
    return random.choice([figlet_ansi_shadow, figlet_big, figlet_doom, figlet_drpepper, figlet_ogre, figlet_slant, figlet_small, figlet_smslant, figlet_standard, figlet_Basic, figlet_alligator, figlet_speed, figlet_stronger])