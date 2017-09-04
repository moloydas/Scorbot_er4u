#!/usr/bin/env python

import openravepy

if __name__ == "__main__":
    env = openravepy.Environment()
    env.Load('er4u_env.xml')
    env.SetViewer('qtcoin')
    robot = env.GetRobots()[0]
