import os

def disc_usage(path): #expects a path to a directory (or file)
    '''returns total disc usage in bytes for a directory and all
      its nested children (files + subdirectories) i.e. cumulative disc usage '''

    current = os.path.getsize(path) #immediate disc usage in bytes
    if os.path.isdir(path): #if path is to a (sub)directory
        for item in os.listdir(path):
            child = os.path.join(path, item) #returns a path to item
            current = current + disc_usage(child)
    return current #returns cumulative total


'''the above algorithm expects a finite traversal of file system, where
the lowermost directories must contain only files (no further subdirectories)
'''