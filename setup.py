from setuptools import setup, find_packages
setup(
    name = "aminatorplugins_chef-zero",
    version = "0.1",
    packages = find_packages(),
    namespace_packages = ( 'aminatorplugins', 'aminatorplugins.provisioner'),

    data_files = [
        ('/etc/aminator/plugins', ['default_conf/aminatorplugins.provisioner.chef-zero.yml']),
    ],

    entry_points = {
       'aminator.plugins.provisioner': [
           'chef = aminatorplugins.provisioner.chef-zero:ChefProvisionerPlugin',
       ],
    },

    # metadata for upload to PyPI
    author = "David Owens",
    author_email = "dave@davetested.com",
    description = "Chef zero provisioner for Netflix's aminator",
    license = "Apache 2.0",
    keywords = "aminator plugin chef-zero chef zero",
)
