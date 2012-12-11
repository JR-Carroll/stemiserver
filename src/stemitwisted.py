'''
Created on Dec 6, 2012

@author: nammer
'''

from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

try:
    reactor.listenTCP(1234, EchoFactory())
    print "running..."
    reactor.run()
except:
    print "failed"