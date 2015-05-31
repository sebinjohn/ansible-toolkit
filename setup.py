from setuptools import setup


setup(name='Ansible Toolkit',
      version='1.0',
      description='The missing Ansible tools',
      url='http://github.com/dellis23/ansible-toolkit',
      author='Daniel Ellis',
      author_email='ellisd23@gmail.com',
      license='GPLv3',
      install_requires=['ansible'],
      packages=['ansible_toolkit'],
      scripts=[
          'bin/atk-show-vars',
      ])