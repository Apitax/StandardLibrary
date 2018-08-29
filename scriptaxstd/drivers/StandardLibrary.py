from apitax.ah.flow.responses.ApitaxResponse import ApitaxResponse
from apitax.ah.models.Command import Command
from apitax.drivers.Driver import Driver


class Api(Driver):
    def isDriverCommandable(self) -> bool:
        return True
        
    def isDriverScriptable(self) -> bool:
        return True

    def getDriverName(self) -> str:
        return 'std'

    def getDriverDescription(self) -> str:
        return 'Provides a standard library for Scriptax'

    def getDriverHelpEndpoint(self) -> str:
        return 'coming soon'

    def getDriverTips(self) -> str:
        return 'coming soon'

    def handleDriverCommand(self, command: Command) -> ApitaxResponse:
        return ApitaxResponse()

    def handleDriverScript(self, command: Command) -> ApitaxResponse:
        return ApitaxResponse()