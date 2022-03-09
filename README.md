# stalk-bot 


# kasper NOTES

# builden van workspace: IMPORTANT: enkel in root van je ros workspace (bij ons {....}/STALK-BOT)   
colcon build 
# bij grote projecten kan het handig zijn om de package enkel te laten builden als de rest niet veranderd is
colcon build --packages-select <package_name>

# elke terminal voor het runnen van ros commandos (bv: ros2 run ... ...) 
. install/setup.bash

# grafische voorstelling van nodes en topics
rqt_graph

# terminal print van data gecast door <TOPIC>
ros2 topic echo <TOPIC>

# aanmaken van een nieuwe package
ros2 pkg create --build-type ament_python <package_name>