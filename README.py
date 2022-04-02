# studious-guacamole
print('Welcome to your To-do list.')
input('Title: ')
input('Description: ')

end_task = ''.lower()
while end_task != 'done':
    check = input('When you have completed the task, type done: ').lower()
    if check == 'done':
        print('Well done, you have completed the task!')
        end_task = 'done'
