from JumpScale import j


class Actions(ActionsBaseMgmt):

    def install(self, service):
        _, output = service.executor.cuisine.core.run('ays test doall', die=False)
        telegram_channel = service.hrd.getStr('telegram.channel', None)
        self.ask_telegram(channel=telegram_channel, message="""AYS TESTS:\n```%s```""" % output, keyboard=[], expect_response=False, timeout=900, redis=None)
