new_file = open('fails.txt', 'a', encoding='utf-8')

new_file.write('Datorium')

new_file.close()

new_file = open('fails.txt', 'r', encoding='utf-8')
file_content = new_file.read()
print(file_content)

new_file.close()

# rakstīt – write
# lasīt – read
# pievienot – append