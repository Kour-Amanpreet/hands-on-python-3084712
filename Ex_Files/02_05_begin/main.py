import os

DEVELOPMENT = "development"
PRODUCTION = "production"
STAGING = "staging"
CODE_SPACE = "code_space"
LOCAL = "local"

current_env = os.environ.get("ENV_NAME", DEVELOPMENT)

if current_env == DEVELOPMENT:
    print("Development environment")
elif current_env == PRODUCTION:
    print("Production environment")
elif current_env == STAGING:
    print("Staging environment")
elif current_env in [CODE_SPACE, LOCAL]:
    print("Codespace or local environment")
else:
    print("Unknown environment")


""" I can change output by writing following command in the terminal:
export ENV_NAME='code_space'          (say)
then follwing output is recieved on typing command python main.py
Codespace or local environment
If I write some arbitrary environment name as: 
export ENV_NAME='AKMAN'          (say)
then follwing output is recieved on typing command python main.py
Unknown environment
"""