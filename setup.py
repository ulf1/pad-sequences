from setuptools import setup
import pypandoc


setup(name='pad-sequences',
      version='0.5.0',
      description='pad variable length sequences with multiples features',
      long_description=pypandoc.convert('README.md', 'rst'),
      url='http://github.com/ulf1/pad-sequences-multi',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['pad_sequences'],
      install_requires=[
          'setuptools>=40.0.0'],
      python_requires='>=3.5',
      zip_safe=False)
