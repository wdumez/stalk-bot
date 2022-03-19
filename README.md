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


### Creating new branches

The `main` branch contains only large releases of our code. If this was a big software project the main branch would be like the final release (v1.0, v1.1, ...). **Never branch from `main`!**

The `dev` branch contains smaller releases that eventually get bundled into a bigger release into main. This is like an internal release that is not yet ready to show to the public.

**All code committed to these two branches should work! (aside from unintentional bugs) so make sure to test your code before committing to them.**

Let's say you wanted to work on a new feature about testing the wheels. Here's what you should do:
1. Create a new branch **from `dev` or any other branch besides `main`**.
   You can do this in VS Code by pressing `ctrl+shift+P` and searching for `Git: Create Branch From...`
2. Give this branch a short but descriptive name. For example: `wheels` or something like that.
3. Make all your changes to this branch, and commit your code often but not constantly (see presentation).
4. When your feature is done, test all your code to make sure everything works and there are no obvious bugs.
5. Merge your new branch **into `dev`**. Do not merge it into `main`! (see merging branches)
6. (Optional) delete your `wheels` branch.
   
This way, the `main` branch will always be older than any other branch and it will be easier to see which branches contain which commits. The only time main will get updated, is when `dev` is merged into it.

### Merging branches

**Merging branch A into branch B** means that branch B will get updated to include changes that were made to A, **and not the other way around**. Let's say I had a branch named `wheels` that I wanted to merge into `dev`. I would do the following:

1. Make sure there are no uncommitted changes in `wheels`.
2. **Switch your active branch to `dev` and pull any changes from the repository**. VS Code: choose your branch in the bottom left corner of your screen and press the icon to the right of it.
3. `ctrl+shift+P` and search for `Git: Merge Branch...`
4. Select the `wheels` branch.
5. If the changes made in `wheels` do not conflict with the changes in `dev`, you're done.
6. If there are conflicts, then these are called merge conflicts and you will have to manually solve them by going into each conflicted file and choosing which changes to accept ('current changes' would be `dev`, while 'incoming changes' would be `wheels`). If you would like a mix of both changes in a file, you will have to edit it manually to include both the changes.
   Merge conflicts can be avoided by making good commits.

Now any commits I had made to `wheels` will be included in `dev`, and not the other way around. 

Also note that you can merge other branches into your branch at any time. For example, if someone else made a change to a file that you would also like, simply merge their branch into yours.