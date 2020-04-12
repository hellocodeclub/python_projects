import hashlib

def get_hash(file):
    BUF_SIZE = 65536
    sha1 = hashlib.sha1()
    with open(file, 'rb') as file_to_process:
        data = file_to_process.read(BUF_SIZE)
        sha1.update(data)
    return sha1.hexdigest()


def merge_two_dicts(dict1, dict2):
    merge_dict = dict1.copy()
    for key in dict2:
        if( key in dict1):
            for item in dict2[key]:
                merge_dict[key].append(item)
        else:
            merge_dict[key] = dict2[key]
    return merge_dict