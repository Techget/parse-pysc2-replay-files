# Parse pysc2 replay files

Framework for inspecting actions and observatinos in StarCraftII replays.
Depends on [pysc2](https://github.com/deepmind/pysc2). Refer to [pysc2-replay](https://github.com/narhen/pysc2-replay)

# Misc

- Make use of StartCraft version 16.
- 'Main function' lies in `python3 transform_replay.py`
- This version extracts actions as well as action paramters from replay files. 
- To change the rule of filtering files, change the `_valid_replay` in `Parser` class in `transform_replay.py`
- Step_mul used is 10.
- To inspect infos that will be recorded in the extracted files, please have a look on `ObserverAgent.py`. And you can modify feature to be recorded according to `pysc2/pysc2/lib/features.py`(in PySC2 repo)
- It takes days to extract those data

# Example

This will execute a function `step` in `ObserverAgent.ObserverAgent` for each step in the replay.

    $ python3 transform_replay.py --replays ~/StarCraftII/Replays/ --agent ObserverAgent.ObserverAgent

Will put extracted files under `data/`

To inspect the extracted files, make use of `testLoadPickle.py`, remember to change the path variable in the file.

    $ python3 testLoadPickle.py