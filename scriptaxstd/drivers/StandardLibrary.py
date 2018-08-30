from apitax.ah.flow.responses.ApitaxResponse import ApitaxResponse
from apitax.ah.models.Command import Command
from apitax.drivers.Driver import Driver
from scriptax.drivers.Scriptax import Scriptax
from scriptaxstd.flow.Delegator import Delegator


class Api(Scriptax):
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
        response.body.add({'result': result})
        if (not result):
            response.status = 500
        else:
            response.status = 200
        return response
        