import os
# Paths ----------------------------------------------------------------------------------------------------------------
path = "/Users/krunal/Desktop/code/pyt/database"
start = "/Users/krunal"
relative_path = os.path.relpath(path, start)
print(relative_path)
# Absolute path to the file you’re looking for
dirname = os.path.dirname("/images")
filename = os.path.join(dirname, 'your relative path to the file')
print(filename)
abspath = os.path.abspath("app.py")
print(abspath)

absolute_path = os.path.dirname(__file__)
relative_path = "src/lib"
full_path = os.path.join(absolute_path, relative_path)

print("\n" + absolute_path + "\n" + relative_path + "\n" + full_path)
# ----------------------------------------------------------------------------------------------------------------------

l3 = tk.Label(root,  text='Welcome')
object_methods=[l3 for l3 in dir(tk.Label)
               if callable(getattr(tk.Label,l3))]
print(object_methods)
