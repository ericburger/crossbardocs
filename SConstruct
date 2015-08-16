DOCS_SVG_FILES = [
   'crossbar_deployment_00.svg',
   'crossbar_deployment_00b.svg',
   'crossbar_deployment_00c.svg',
   'crossbar_deployment_01.svg',
   'crossbar_deployment_02.svg',
   'crossbar_deployment_03.svg',
   'crossbar_deployment_04.svg',
   'crossbar_deployment_05.svg',
   'crossbar_deployment_06.svg',
   'crossbar_deployment_07.svg',
   'crossbar_deployment_08.svg',
   'crossbar_application_scenario_1.svg',
   'crossbar_application_scenario_2.svg',
   'crossbar_application_scenario_3.svg',
   'crossbar_application_scenario_4.svg',
   'crossbar_application_scenario_5.svg',
   'crossbar_application_scenario_6.svg',
   'crossbar_application_scenario_7.svg',
   'crossbar_transports_1.svg',
   'crossbar_transports_2.svg',
   'crossbar_clients.svg',
   'crossbar_integration.svg'
]

DOCS_SVG_SOURCE_DIR = './work/docs/'
DOCS_SVG_TARGET_DIR = './static/img/docs/gen/'

IOTCOOKBOOK_SVG_FILES = []
IOTCOOKBOOK_SVG_SOURCE_DIR = './work/iotcookbook/'
IOTCOOKBOOK_SVG_TARGET_DIR = './static/img/iotcookbook/gen/'

###
### Do not touch below this unless you know what you are doing;)
###

import os
import pkg_resources

taschenmesser = pkg_resources.resource_filename('taschenmesser', '..')

## use this for Taschenmesser development only
#taschenmesser = "../../infrequent/taschenmesser"
#taschenmesser = "../../../taschenmesser"

env = Environment(tools = ['default', 'taschenmesser'],
                  toolpath = [taschenmesser],
                  ENV  = os.environ)


# Process SVGs
#
docs_imgs = env.process_svg(DOCS_SVG_FILES, DOCS_SVG_SOURCE_DIR, DOCS_SVG_TARGET_DIR)
iotcookbook_imgs = env.process_svg(IOTCOOKBOOK_SVG_FILES, IOTCOOKBOOK_SVG_SOURCE_DIR, IOTCOOKBOOK_SVG_TARGET_DIR)

Alias("img", [docs_imgs, iotcookbook_imgs])
