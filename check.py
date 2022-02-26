import argparse

from matplotlib.style import available
from Available import Available

default_config = {
    'selector': 'div.btn-add-cart',
    'available_text': 'ใส่ตะกร้า',
    'not_available_text': 'หมด',
    'onetime': False
}

# Create the parser
my_parser = argparse.ArgumentParser()

# Add the arguments
my_parser.add_argument('url', type=str, help="url for checking")
my_parser.add_argument('--advice', default=False, action='store_true', help="check product available for www.advice.co.th")
my_parser.add_argument('--onetime', default=False, action='store_true', help="check product available for one time")

# Execute the parse_args() method
args = my_parser.parse_args()

if args.advice:
    config = default_config
else:
    config = default_config
config['onetime'] = args.onetime

line_token = ''

available = Available(url=args.url, config=config, line_token = line_token)
available.start_bot()