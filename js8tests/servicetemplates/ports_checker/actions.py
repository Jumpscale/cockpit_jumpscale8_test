from JumpScale import j


class Actions(ActionsBaseMgmt):

    def install(self, service):
        e = service.executor
        ports = service.hrd.getList('ports')
        for p in ports:
            rc, out = e.cuisine.core.run("netstat -nltp | grep {0}".format(p), die=False)
            if rc == 0:
                j.logger.log("Service is running on port {0}".format(p))
                self.report(service, "Service is running on port {0}".format(p))
            else:
                j.logger.log("No service is running on port {0}".format(p))
                self.report(service, "No service is running on port {0}".format(p))

    def report(self, service, message=''):
        telegram_channel = service.hrd.getStr('telegram.channel', None)
        self.ask_telegram(channel=telegram_channel, message=message, keyboard=[], expect_response=False, timeout=900, redis=None)
        return
