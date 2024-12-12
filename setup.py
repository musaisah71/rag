from setuptools import find_packages, setup

setup(
    name='Generative_AI_Project',  # Changed spaces to underscores as package names shouldn't contain spaces
    version='0.0.0',
    author='Musa',                 # Added missing comma
    author_email='isahmusa71@yahoo.com',  # Added missing comma
    packages=find_packages(),      # Added missing comma
    install_requires=[             # Added your required packages
        'streamlit',
        'PyPDF2',
        'langchain',
        'python-dotenv',
        'google-generativeai',
        'faiss-cpu'
    ]
)