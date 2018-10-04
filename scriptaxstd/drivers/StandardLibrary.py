from apitaxcore.flow.responses.ApitaxResponse import ApitaxResponse
from commandtax.models.Command import Command
from scriptax.drivers.builtin.Scriptax import Scriptax
from scriptaxstd.flow.Delegator import Delegator


class StandardLibrary(Scriptax):
    def isDriverCommandable(self) -> bool:
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
        delegator = Delegator(command)
        result = delegator.delegate()
        response = ApitaxResponse()
        if not result:
            response.status = 500
        else:
            response.body.add({'result': result})
            response.status = 200
        return response
