from setuptools import setup, find_packages

version = '0.2.0'

setup(
    name='leadtheway.policy',
    version=version,
    description="The collection of products required for the Lead The Way website",
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
    keywords='',
    author='BEAST Core Development Team',
    author_email='beast@ucsd.edu',
    url='https://github.com/beastcore/leadtheway.policy',
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
        'plone.app.dexterity',
        'collective.geo.bundle',
        'collective.indexing',
        'collective.uploadify',
        'jyu.z3cform.datepicker',
        'Solgema.fullcalendar',
          'beast.securelogin',
        'collective.dexterity.appointments',
        'avrc.theme.leadtheway',
        ],
    extras_require=dict(
        test=['plone.app.testing'],
        ),
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )
