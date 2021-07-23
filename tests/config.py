class Config:
    def __init__(self, env):
        self.base_url = {
            'dev': 'http://mydev-env.com' ,
            'qa': 'http://myqa-env.com'
        }[env]

        self.app_port  = {
            'dev': 8080,
            'qa': 80
        }[env]

