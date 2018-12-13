
def spide_write_to_txt(s, file_path):
    try:
        # '../Smart_commons/cs_operators.txt'
        f = open(file_path, 'a')
        f.writelines(s)
    finally:
        if f:
            f.close()

