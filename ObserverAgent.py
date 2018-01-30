#!/usr/bin/env python

import pickle
import numpy as np

from pysc2.lib import actions as sc_action

class ObserverAgent():

    def __init__(self):
        self.states = []

    def step(self, time_step, actions, info):

        state = {}

        state["minimap"] = {}

        state["minimap"]["height_map"] = time_step.observation["minimap"][0] / 256
        state["minimap"]["visibility"] = time_step.observation["minimap"][1] / 2
        state["minimap"]["creep"] = time_step.observation["minimap"][2]
        state["minimap"]["camera"] = time_step.observation["minimap"][3]
        #minimap.player_id = time_step.observation["minimap"][4]
        player_relative = time_step.observation["minimap"][5]
        state["minimap"]["own_units"] = (player_relative == 1).nonzero()
        state["minimap"]["neutral_units"] = (player_relative == 3).nonzero()
        state["minimap"]["enemy_units"] = (player_relative == 4).nonzero()
        state["minimap"]["selected"] = time_step.observation["minimap"][6]

        state["screen"] = {}

        state["screen"]["height_map"] = time_step.observation["screen"][0] / 256
        state["screen"]["visibility"] = time_step.observation["screen"][1] / 2
        state["screen"]["creep"] = time_step.observation["screen"][2]
        state["screen"]["power"] = time_step.observation["screen"][3]
        #state.screen.player_id = time_step.observation["player_id"][0]
        player_relative = time_step.observation["screen"][4]
        state["screen"]["own_units"] = (player_relative == 1).nonzero()
        state["screen"]["neutral_units"] = (player_relative == 3).nonzero()
        state["screen"]["enemy_units"] = (player_relative == 4).nonzero()

        # How to deal with this thing?
        unit_type = time_step.observation["screen"][5]

        state["screen"]["selected"] = time_step.observation["screen"][6]
        state["screen"]["hit_points"] = time_step.observation["screen"][7]
        state["screen"]["energy"] = time_step.observation["screen"][8]
        state["screen"]["shields"] = time_step.observation["screen"][9]
        state["screen"]["unit_density"] = time_step.observation["screen"][10]

        state["game_loop"] = time_step.observation["game_loop"]
        state["player"] = time_step.observation["player"]

        # Binary encoding of available actions
        state["available_actions"] = np.zeros(len(sc_action.FUNCTIONS))
        for i in time_step.observation["available_actions"]:
            state["available_actions"][i] = 1.0

        self.states.append(state)
