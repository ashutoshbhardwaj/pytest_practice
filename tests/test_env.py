def test_env_is_qa(env):
    assert env == 'qa'

def test_env_is_dev(env):
    assert env== 'dev'


def test_config_is_qa(app_config):
    assert app_config.base_url =='http://myqa-env.com'

def test_config_is_dev(app_config):
    assert app_config.base_url == 'http://mydev-env.com'