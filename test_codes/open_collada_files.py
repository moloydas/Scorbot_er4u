#!/usr/bin/env python

import openravepy

if __name__ == "__main__":
    env = openravepy.Environment()
    env.Load('env.xml')
    env.SetViewer('qtcoin')
    viewer = env.GetViewer()
    viewer.SetBkgndColor([.8, .85, .9])  # RGB tuple
    