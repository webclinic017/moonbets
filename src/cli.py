from PyInquirer import Separator

main_menu = [
    {
        'type': 'list',
        'name': 'theme',
        'message': 'What do you want to do?',
        'choices': [
            'QUICK Single stonk report',
            'Single stonk report',
            'Future earnings report',
            'Exit'
        ]
    }
]

report_dates = [
    {
        'type': 'input',
        'name': 'business_days',
        'message': 'Enter business days',
    },
    {
        'type': 'input',
        'name': 'days_from_today',
        'message': 'Enter days from current date',
    }
]

stonk_report = [
    {
        'type': 'input',
        'name': 'ticker',
        'message': 'Enter ticker',
    }
]


screener_options = [
    {
        'type': 'checkbox',
        'message': 'Select options for filter',
        'name': 'toppings',
        'choices': [ 
            Separator('Cap Size'),
            {
                'name': 'Ham'
            },
            {
                'name': 'Ground Meat'
            },
            {
                'name': 'Bacon'
            },
            Separator('= The Cheeses ='),
            {
                'name': 'Mozzarella',
                'checked': True
            },
            {
                'name': 'Cheddar'
            },
            {
                'name': 'Parmesan'
            },
            Separator('= The usual ='),
            {
                'name': 'Mushroom'
            },
            {
                'name': 'Tomato'
            },
            {
                'name': 'Pepperoni'
            },
            Separator('= The extras ='),
            {
                'name': 'Pineapple'
            },
            {
                'name': 'Olives',
                'disabled': 'out of stock'
            },
            {
                'name': 'Extra cheese'
            }
        ]
    }
]

