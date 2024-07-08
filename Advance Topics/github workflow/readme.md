### for the code to work properly , you have to configure AWS SSO on your PC

### Steps to configure AWS SSO:
    1. If the SSO is not configured first configure SSO.
    2. Open terminal & Run command 'aws configure sso'
    3. Input all necessary information
    4. Run command export AWS_PROFILE = sequenx-aws-profile
    5. If SSO is configured, Open gitbash
    6. Go to project directory
    7. Run command: ./setup_local_env aws-sequenx-profile
    8. Wait
    9. Now you are good to use the libraries listed in pipenv to use in your project
    10. If the pip env is configured it is better to remove the env first before doing above steps.    Pipenv --rm