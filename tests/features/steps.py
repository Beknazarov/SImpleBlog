from lettuce import step, world


@step(r'Open "(.*)" page')
def should_open_main_page(step, page):
    world.current_page = world.mapping[page]
    world.browser.get(world.current_page['url'])


@step(u'Name "([^"]*)" value "([^"]*)"')
def set_input_value(step, name, value):
    elem = world.browser.find_element_by_name(world.current_page[name])
    elem.send_keys(value)


@step(u'Click "([^"]*)"')
def click_group1(step, element):
    el = world.browser.find_element_by_css_selector(world.current_page[element])
    el.click()


@step(u'Click2 "([^"]*)"')
def click_group1(step, element):
    el = world.browser.find_element_by_xpath(world.current_page[element])
    el.click()
