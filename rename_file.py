import os, sys

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

months_dict = {
  "Jan": "-01-",
  "Feb": "-02-",
  "Mar": "-03-",
  "Apr": "-04-",
  "May": "-05-",
  "Jun": "-06-",
  "Jul": "-07-",
  "Aug": "-08-",
  "Sep": "-09-",
  "Oct": "-10-",
  "Nov": "-11-",
  "Dec": "-12-"
}

# renames a single file
def rename_file(fname):
  for month in months:
    if fname.find(month) != -1:
      new_name = fname.replace(month, months_dict[month])
    os.rename(fname, new_name)
  return new_name

# renames all files given a path
def rename_files(path):
  fnames = os.listdir(path)
  for fname in fnames:
    rename_file(fname)