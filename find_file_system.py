class file:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.children = []
        self.isDirectory = False if '.' in name else True
        self.extension = name.split('.')[-1] if '.' in name else ''

class filter:
    def __init__(self):
        pass
    def apply(self, file):
        return file

class extension_filter(filter):
    def __init__(self, extension):
        self.extension = extension
    def apply(self, file):
        return file.extension == self.extension

class min_size_filter(filter): 
    def __init__(self, size):
        self.size = size
    def apply(self, file):
        return file.size > self.size
    
class file_system:
    def __init__(self):
        self.filters = []
    def add_filter(self, given_filter):
        print(given_filter)
        ### most imp to notice here
        if isinstance(given_filter, filter):self.filters.append(given_filter)
        print(self.filters)
    def applyOrFilter(self, root):
        def dfs(root, result):
            if root.isDirectory:
                for child in root.children:
                    dfs(child, result)
            else:
                for f in self.filters:
                    if f.apply(root):
                        result.append(root.name)
                        print(result)
                        return
        result = []
        dfs(root, result)
        return result

    def applyAndFilter(self, root):
        def dfs(root, result):
            if root.isDirectory:
                for child in root.children:
                    dfs(child, result)
            else:
                for f in self.filters:
                    if not f.apply(root):
                        return
                result.append(root.name)
                print(result)
        result = []
        dfs(root, result)
        return result
# Example usage:
if __name__ == "__main__":
    f1 = file("root", 300)
    f2 = file("folder1", 100)
    f3 = file("folder2", 100)
    f4 = file("folder3", 100)
    f1.children = [f2, f3, f4]

    f5 = file("file1.txt", 4)
    f6 = file("file2.xml", 10)
    f7 = file("file3.txt", 15)
    f8 = file("file4.jpg", 1)
    f2.children = [f5, f6, f7, f8]

    f9 = file("file5.txt", 9)
    f10 = file("file6.rar", 10)
    f11 = file("file7.zip", 3)
    f3.children = [f9, f10, f11]
    
    f12 = file("file8.txt", 4)
    f13 = file("file9.mp3", 6)
    f4.children = [f12, f13]

    greaterThan5 = min_size_filter(5)
    txtFilter = extension_filter("txt")


    fs = file_system()
    fs.add_filter(greaterThan5)
    fs.add_filter(txtFilter)

    print("OR Filter Results:")
    or_results = fs.applyOrFilter(f1)
    
    print("\nAND Filter Results:")
    and_results = fs.applyAndFilter(f1)