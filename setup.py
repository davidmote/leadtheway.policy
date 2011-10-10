from setuptools import setup, find_packages

version = '0.1.0'

setup(name='leadtheway.policy',
      version=version,
      description="The collection of products required for the Lead The Way website",
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'':'src'},
      namespace_packages=['leadtheway'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'PIL',
          'Products.PloneFormGen',
          'plone.app.caching',
          'collective.uploadify',
          'collective.indexing',
          'beast.securelogin',
          'avrc.theme.leadtheway',
          'jyu.z3cform.datepicker',
          'collective.geo.bundle',
          'plone.app.dexterity',
          'Solgema.fullcalendar',
          'collective.dexterity.appointments',
          # -*- Extra requirements: -*-
      ],
    extras_require=dict(
        test=['plone.app.testing'],
        ),

      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
