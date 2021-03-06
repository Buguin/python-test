# -*- codeing:utf-8 -*-
# __author__ = 'Buguin'
from toolkit.xmltools.read_xml_tools import *


class Control(object):
    def __init__(self, configpath):
        # The deque for download sourcecode
        self.configpath = configpath
        self.git_deque = deque(maxlen=20)
        self.svn_deque = deque(maxlen=20)
        # The deque for compare code
        self.compare_deque = deque(maxlen=20)

    def run(self):
        # get deque of repository, include svn and git
        self.git_deque = get_git_deque(self.configpath)
        self.svn_deque = get_svn_deque(self.configpath)

        # get code throgh git and svn tool
        """
        while self.git_deque:
            git_tool = self.git_deque.popleft()
            print(git_tool)
            git_tool.initial()
        """

        while self.svn_deque:
            svn_tool = self.svn_deque.popleft()
            print(svn_tool)
            svn_tool.initial()
        # initial information of config
        compare_deque = get_config_deque(self.configpath)
        while compare_deque:
            compare_tool = compare_deque.popleft()
            print(compare_tool.offering + " " + compare_tool.version)
            source_xmlpath = compare_tool.source_initial()
            target_xmlpath = compare_tool.target_initial()
            # source_xmlpath = r"D:\Users\buguin\PycharmProjects\Mandarin\logs\ConfigItems\RTOS V100R012C00.xml"
            # target_xmlpath = r"D:\Users\buguin\PycharmProjects\Mandarin\logs\TargetItems\RTOS-GIU.xml"
            compare_tool.compare_diff(source_xmlpath, target_xmlpath)
            print(compare_tool.compareresult)
