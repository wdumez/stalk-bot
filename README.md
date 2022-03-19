# stalk-bot 

## kasper NOTES

### builden van workspace: IMPORTANT: enkel in root van je ros workspace (bij ons {....}/STALK-BOT)

`colcon build` 

### bij grote projecten kan het handig zijn om de package enkel te laten builden als de rest niet veranderd is

`colcon build --packages-select <package_name>`

### elke terminal voor het runnen van ros commandos (bv: ros2 run ... ...) moet je de workspace sources waar de packages zijn die je gebruikt

`. install/setup.bash`

### grafische voorstelling van nodes en topics

`rqt_graph`

### terminal print van data gecast door <TOPIC>

`ros2 topic echo <TOPIC>`

### aanmaken van een nieuwe package

`ros2 pkg create --build-type ament_python <package_name>`

## Github workflow

The `main` branch contains only large releases of our code. If this was a big software project like google chrome, the main branch be like the final release (v1.0, v1.1, ...).

The `dev` branch contains smaller releases that eventually get bundled into a bigger release into main. This is like an internal release not yet ready to show to the public.

**All code committed to these two branches should work! (aside from unintentional bugs) so make sure to test your code before committing to them.**

Let's say you wanted to work on a new feature 