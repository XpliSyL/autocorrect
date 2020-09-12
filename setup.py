from distutils.core import setup

setup(name='autocorrect',
      version='2.0.0',
      python_requires='>=3.6',
      packages=['autocorrect'],
      package_data={'autocorrect': ['data/en.tar.gz']},
      description='Spelling Corrector',
      author='Jonas McCallum, Filip Sondej',
      author_email='filipsondej@protonmail.com',
      url='https://github.com/fsondej/autocorrect',
      license='https://opensource.org/licenses/LGPL-3.0',
      classifiers=(
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
            'Natural Language :: English',
            'Natural Language :: Polish',
            'Natural Language :: Russian',
            'Natural Language :: Ukrainian',
            'Natural Language :: Turkish',
            'Natural Language :: Spanish',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3'),
      keywords='autocorrect spelling corrector nlp multilanguage spellcheck')
