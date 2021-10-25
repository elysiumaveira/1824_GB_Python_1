"""
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
которая решена, например, во фреймворке django.
"""


import os
import shutil


destination = os.path.join('my_project', 'templates')

for root_dir, list_dir, files in os.walk('my_project'):
    if 'templates' in list_dir:
        source = os.path.join(root_dir, 'templates')
        print(source)
        shutil.copytree(source, destination, dirs_exist_ok=True)
