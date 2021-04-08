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
