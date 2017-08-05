from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    env.autoescape = True

    # env.globals.update(context['globals'])
    # env.filters.update(context['filters'])

    return env
