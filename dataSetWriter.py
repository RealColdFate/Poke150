from ClassLabelMapping import *
import os
import shutil


# creates directories for with class names
def create_class_directories(from_path):
    full_dir_path = os.path.join(from_path, 'data')
    if not os.path.isdir(full_dir_path):
        os.mkdir(full_dir_path)
    else:
        print("Path {} already exists".format(full_dir_path))
    for k, v in mon_dict.items():
        os.mkdir(os.path.join(full_dir_path, k))
    print('done')


# moves images downloaded from pokemon official site to dataset dir
def move_images(from_path, to_path):
    for k, v in mon_dict.items():
        curr_file_name = str(v).zfill(3) + '.jpg'
        print(curr_file_name)
        full_path = os.path.join(from_path, curr_file_name)
        shutil.move(full_path, os.path.join(to_path, k, '1') + '.jpg')


# moves images from Kaggel archive https://www.kaggle.com/lantian773030/pokemonclassification
def move_from_archive(from_path, to_path):
    for label in os.listdir(from_path):
        if label in mon_dict:
            print("Moving {}...".format(label))
            full_class_path_from = os.path.join(from_path, label)
            for file in os.listdir(full_class_path_from):
                shutil.move(os.path.join(full_class_path_from, file), os.path.join(to_path, label))
            print("Moved {}".format(label))


# prints diagnostic information on which entries the Kaggel set was missing
# because of this I was able to find that there was in fact information of Mr. Mime and Farfetchd
def run_diagnostic(from_path):
    count = 1
    check_list = []
    disjoint = []
    for label in os.listdir(from_path):
        if label in mon_dict:
            print('found {}, dex ID {}'.format(label, mon_dict[label]))
            check_list.append(mon_dict[label])
            count += 1
        else:
            disjoint.append(label)
    check_list.sort()
    for i in range(1, 152):
        if i not in check_list:
            for k, v in mon_dict.items():
                if v == i:
                    print(k, " missing, dex ID", v)
    print("the disjoint mon ", disjoint)


def sort_by_dex_id(info):
    return sorted(info, key=lambda x: x[1])


def sort_by_name(info):
    return sorted(info)


def sort_by_most_files(info):
    return sorted(info, key=lambda x: x[2], reverse=True)


def print_info(info):
    for name, did, icount in info:
        print("Class: {}, Dex ID: {}, Image Count: {}".format(name, did, icount))


def get_image_count_info(from_path):
    info = []
    for label in os.listdir(from_path):
        count = 0
        full_class_path = os.path.join(from_path, label)
        for _ in os.listdir(os.path.join(full_class_path)):
            count += 1
        info.append((label, mon_dict[label], count))
    return info


data_path = r'E:\imageSets\Pokemon\dataset\data'
pokemon_official_path = r'poke_images'
kaggel_archive_path = r'E:\imageSets\Pokemon\kaggelset\PokemonData'

information = get_image_count_info(data_path)
print_info(sort_by_most_files(information))
# move_from_archive(kaggel_archive_path, data_path)
# create_class_directories(data_path)
# move_images(pokemon_official_path, data_path)
