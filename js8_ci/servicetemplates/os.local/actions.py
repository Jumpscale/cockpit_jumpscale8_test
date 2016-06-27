from JumpScale import j


class Actions(ActionsBaseMgmt):

    def getExecutor(self, service):
        return j.tools.executor.getLocal()
