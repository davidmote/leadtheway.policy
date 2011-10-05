from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class LeadTheWayPolicy(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import leadtheway.policy as package
        xmlconfig.file('configure.zcml', package, context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'leadtheway.policy:default')


LEADTHEWAY_POLICY_FIXTURE = LeadTheWayPolicy()

LEADTHEWAY_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(LEADTHEWAY_POLICY_FIXTURE,),
    name='leadtheway:Integration'
    )
