opposites = {’up’: ’down’, ’right’: ’wrong’, ’true’: ’false’}
alias = opposites
copy = opposites.copy()
alias[’right’] = ’left’
opposites[’right’]
’left’
copy[’right’] = ’privilege’
opposites[’right’]
’left