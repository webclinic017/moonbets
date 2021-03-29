main_menu = [
    {
        'type': 'list',
        'name': 'theme',
        'message': 'What do you want to do?',
        'choices': [
            'Future earnings report',
            'Single stonk report',
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
