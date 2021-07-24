from pytest import mark
#
# @mark.parametrize('tv_model', [
#     'Sony',
#     'Samsung',
#     'Visio'
#
#
# ])
def test_television_turns_on(tv_model):
    print(f"{tv_model} turns on as exected")

def test_browser_can_navigate_to_training_ground(browser):
    browser.get('http://techstepacademy.com/training-ground')


