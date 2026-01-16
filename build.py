# Open the json file containing the data
import json

print("Building FEBio Feature Manual...")
print("Reading febio_features.json...")
with open('febio_features.json', mode='r') as file:
    # Load the JSON data
    data = json.load(file)

# create the mkdocs.yml file
with open('mkdocs.yml', mode='w') as file:
    file.write('site_name: FEBio Feature Manual\n')
    file.write('site_description: This manual provides documentation for the features of FEBio.\n')
    file.write('site_author: FEBio Team\n')
    file.write('theme:\n')
    file.write('  name: material\n')
    file.write('  palette:\n')
    file.write('    primary: indigo\n')
    file.write('    accent: indigo\n')
    file.write('  font:\n')
    file.write('    text: \'Roboto\'\n')
    file.write('    code: \'Roboto Mono\'\n')
    file.write('  features:\n')
    file.write('    - navigation.tabs\n')
    file.write('    - navigation.top\n')
    file.write('    - search.highlight\n')
    file.write('    - search.suggest\n')
    file.write('    - toc.integrate\n')
    file.write('    - content.external.links\n')
    file.write('markdown_extensions:\n')
    file.write('  - admonition\n')
    file.write('  - codehilite\n')
    file.write('  - footnotes\n')
    file.write('  - toc:\n')
    file.write('      permalink: true\n')
    file.write('  - pymdownx.arithmatex:\n')
    file.write('      generic: true\n')
    file.write('  - pymdownx.superfences\n')
    file.write('extra_javascript:\n')
    file.write('  - js/mathjax_config.js\n')
    file.write('  - https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js\n')
    file.write('nav:\n')
    file.write('  - Home: index.md\n')

# create a dictionary to keep track of module and (name, file) list created for that module
module_files = {}

# process the modules first
print("Processing modules...")
for module in data['modules']:
    # get the module name
    module_name = module['name']

    # see if an info field exists

    module_info = '(No description provided)'
    if 'info' in module:
        module_info = module['info']

    clean_mod = module_name.replace(' ', '_').lower()
    filename = f'module_{clean_mod}.md'

    # see if we have a description file for this module
    try:
        with open(f"meta/{filename}", mode='r') as info_file:
            module_info = info_file.read()
    except FileNotFoundError:
        print(f'WARNING: No description file found for \"{module_name}\" ({filename})')

    print(f'Processing module: {module_name}')
    # create a markdown file for each module
    with open(f'docs/modules/{filename}', 'w') as md_file:
        md_file.write(f'# {module_name} module\n\n')
        md_file.write('## Description\n\n')
        md_file.write(f'{module_info}\n')

    # add the filename to the module_files dictionary
    module_files[module_name] = (module_name, filename)

# create a dictionary to keep track of class and (feature, file) list created for that class
class_files = {}

# Process the data
print("Processing data...")
for row in data['features']:
    # get the name
    name = row['type_string']

    # get the class ID
    class_id = row['super_class_id']
    # remove the "_ID" suffix if it exists
    if class_id.endswith('_ID'):
        class_id = class_id[:-3]
    #remove FE prefix if it exists
    if class_id.startswith('FE'):
        class_id = class_id[2:]

    # make all lower case
    class_id = class_id.lower()

    # skip classes that start with 'log' and 'plot'
    if class_id.startswith('log') or class_id.startswith('plot'):
        continue

    # get the module name
    module_name = row['module']
    if module_name == '':
        module_name = 'core'

    # skip thermo-fluid and polar fluid modules
    if module_name.lower() in ['thermo-fluid', 'polar fluid']:
        continue

    print(f'Processing feature: {name}')

    # replace all spaces with underscores and make lower case
    clean_name = name.replace(' ', '_').lower()
    clean_class = class_id.replace(' ', '_').lower()
    clean_mod = module_name.replace(' ', '_').lower()

    # append module name and class ID to filename
    filename = f'{clean_mod}_{clean_class}_{clean_name}.md'

    # see if we have a description file for this feature
    info = ''
    try:
        with open(f"meta/{filename}", mode='r') as info_file:
            info = info_file.read()
    except FileNotFoundError:
        print(f'WARNING: No description file found for \"{name}\" ({filename})')
        info = ''

    # create an markdown file for each feature
    with open(f'docs/features/{filename}', 'w') as md_file:
        md_file.write(f'# {name}\n\n')
        md_file.write(f'**Module:** {module_name}\n\n')
        md_file.write(f'**Category:** {class_id}\n\n')
        md_file.write(f'**Type string:** `"{name}"`\n\n')

        # create a table for parameters listing name, description, default, and units
        md_file.write('## Parameters\n\n')
        params = row['parameters']
        if len(params) == 0:
            md_file.write('This feature has no parameters.\n') 
        else:
            md_file.write('| Name | Description | Default | Units |\n')
            md_file.write('|------|-------------|---------|-------|\n')
            for param in params:
                param_name = param['name']
                param_desc = param['description']
                param_default = param['default']
                param_units = param['units']
                md_file.write(f'| `{param_name}` | {param_desc} | {param_default} | [{param_units}] |\n')

        md_file.write('\n\n## Description\n\n')
        if info == '':
            md_file.write('(No description provided)\n\n')
        else:
            md_file.write(f'{info}\n')

    # add the filename to the class_files dictionary
    if class_id not in class_files:
        class_files[class_id] = []
    class_files[class_id].append((name, filename))

# sort the class_files dictionary by class_id
class_files = dict(sorted(class_files.items()))

# open the mkdocs.yml file in append mode
print("Writing mkdocs.yml...")
with open('mkdocs.yml', mode='a') as mkdocs:

    # append the Modules section
    mkdocs.write('  - Modules:\n')
    for module_name, (name, filename) in module_files.items():
        mkdocs.write(f'    - {name}: modules/{filename}\n')

    # append the Features section
    mkdocs.write('  - Features:\n')
    # append the class sections
    for class_id, features in class_files.items():
        # special cases for class names
        if class_id == 'bc':
            class_id = 'boundary conditions'
                
        if class_id == 'ic':
            class_id = 'initial conditions'

        mkdocs.write(f'    - {class_id.capitalize()}:\n')
        for name, filename in features:
            mkdocs.write(f'        - {name}: features/{filename}\n')


print("Build complete.")
