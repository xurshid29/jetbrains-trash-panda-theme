from jinja2 import Environment, PackageLoader, select_autoescape
import yaml

themes = {
    'default': 'default.yaml',
    'light': 'light.yaml',
    'moonlight': 'moonlight.yaml'
}

for name in themes:
    with open(f'src/data/{themes[name]}') as theme_data_file:
        theme_data = yaml.safe_load(theme_data_file)

    env = Environment(
        loader=PackageLoader('theme', 'src/templates'),
        autoescape=select_autoescape()
    )

    env.filters['bool'] = bool

    theme_template = env.get_template('theme.json.template')
    theme_scheme_template = env.get_template('scheme.xml.template')

    with open(f'src/main/resources/{theme_data["theme_out_file"]}', 'w+') as theme_out_file:
        theme_out_file.write(theme_template.render(theme_data))
        theme_out_file.close()

    with open(f'src/main/resources/{theme_data["scheme_out_file"]}', 'w+') as scheme_out_file:
        scheme_out_file.write(theme_scheme_template.render(theme_data))
        scheme_out_file.close()
