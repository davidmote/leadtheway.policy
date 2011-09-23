import unittest2 as unittest
from leadtheway.policy.testing import LEADTHEWAY_POLICY_INTEGRATION_TESTING
from plone.app.testing import applyProfile

from Products.CMFCore.utils import getToolByName

class TestSetup(unittest.TestCase):
    
    layer = LEADTHEWAY_POLICY_INTEGRATION_TESTING

    def test_theme_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('avrc.theme.leadtheway'))        

    def test_indexing_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('collective.indexing'))        

    def test_datepicker_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('jyu.z3cform.datepicker'))     

    def test_geo_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('collective.geo.bundle'))     

    # def test_linguaplone_installed(self):
    #     portal = self.layer['portal']
    #     quickinstaller = getToolByName(portal, 'portal_quickinstaller')
    #     self.assertTrue(quickinstaller.isProductInstalled('Products.LinguaPlone'))   

    def test_fullcalendar_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('Solgema.fullcalendar'))   

    def test_appointments_installed(self):
        portal = self.layer['portal']
        quickinstaller = getToolByName(portal, 'portal_quickinstaller')
        self.assertTrue(quickinstaller.isProductInstalled('collective.dexterity.appointments'))