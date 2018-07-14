#!/usr/local/bin/python

import os
import csv
import json

post_id_count = 4356 
table_id_count = 144
category_id = '48'
insert_sql = ''

def file_name(file_dir):
    list = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if file.split('.')[-1] == 'json':
                list.append(file)
    return list

def read_json(list):
    global post_id_count
    global category_id
    global table_id_count
    global insert_sql
    for file in list:
        path = '/Volumes/Software/timing-fitness/products_pics/YM/temp/' + file
        with open(path) as file_object:
            contents = file_object.read()
            dict_obj = json.loads(contents)
            # dict_obj["data"] = dict_obj["data"].insert(-1, ["Product Parameters", "#colspan#"])
            data_obj = dict_obj["data"]
            for temp_arr in data_obj:
                if len(temp_arr) == 3:
                    del temp_arr[2]
            data_obj.insert(0, ["Product Parameters", "#colspan#"])
            dict_obj["data"] = data_obj
            option = {
                "last_editor": 1,
                "table_head": True,
                "table_foot": False,
                "alternating_row_colors": True,
                "row_hover": True,
                "print_name": False,
                "print_name_position": "above",
                "print_description": False,
                "print_description_position": "below",
                "extra_css_classes": "",
                "use_datatables": False,
                "datatables_sort": True,
                "datatables_filter": True,
                "datatables_paginate": True,
                "datatables_lengthchange": True,
                "datatables_paginate_entries": 10,
                "datatables_info": True,
                "datatables_scrollx": False,
                "datatables_custom_commands": ""
            }

            # generate the data as table press import format type.
            # dict_obj["options"] = option
            # json_str = json.dumps(dict_obj)
            # with open(path, 'w') as f:
                # f.write(json_str)
            create_init_sql(dict_obj['name'], post_id_count, table_id_count, dict_obj['decription'])
            post_id_count = post_id_count + 1
            table_id_count = table_id_count + 1

    with open('/Volumes/Software/timing-fitness/products_pics/YM/temp/all.sql', 'w') as f:
        f.write(insert_sql.encode('utf-8'))

def create_init_sql(name, post_id, table_id, title):
    global insert_sql

    insert_sql = insert_sql + "INSERT INTO abc_posts (post_author, post_date, post_date_gmt, post_content, post_title, post_status, comment_status, ping_status, post_name, post_modified, post_modified_gmt, post_parent, guid, menu_order, post_type, comment_count) VALUES('1', '2018-07-14 13:36:36', '2018-07-14 05:36:36', '<h3>Product Description</h3>\n[table id=%d /]\n <h3>Learn More</h3>\n <a href=\"/our-service/\">Our Service</a>\n <h3>Download</h3>\n <a href=\"/wp-content/uploads/2018/03/timing-fitness-products-cata.pdf\">Download Our Full Products Catalog</a>\n', '%s', 'draft', 'open', 'closed', '%s', '2018-07-14 13:36:36', '2018-07-14 05:36:36', 0, 'https://www.timingfit.com/?post_type=products&#038;p=%d', 0, 'products', 0)" % (table_id, title, title.lower().replace(' ', '-'), post_id) + ";\n"
    insert_sql = insert_sql + "INSERT INTO abc_term_relationships(object_id, term_taxonomy_id, term_order) values (%d, %s, 0)" % (post_id, category_id) + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, '_yoast_wpseo_primary_product_categories', category_id) + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, '_yoast_wpseo_content_score', 95) + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'rtthemert_gallery_images', '') + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'rtthemecustom_sidebar_position', '')  + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'rtthemefree_tab_4_content', '')  + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'rtthemefree_tab_4_icon', '')  + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'rtthemefree_tab_4_title', '')  + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'rtthemefree_tab_3_content', '')  + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'rtthemefree_tab_3_icon', '')  + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'rtthemefree_tab_3_title', '')  + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'rtthemefree_tab_2_content', '')  + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'rtthemefree_tab_2_icon', '')  + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'rtthemefree_tab_2_title', '')  + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'rtthemefree_tab_1_content', '[gallery ids="3845,3844,3846,3153"]')  + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'rtthemefree_tab_1_icon', 'icon-rocket-1')  + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'rtthemefree_tab_1_title', 'Packaging&Shipping')  + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'rtthemeattached_documents', '')  + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'rtthemerelated_products[]', '')  + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'rtthemeshort_description', 'Yoga Mat')  + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'rtthemesale_price', '')  + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'rtthemeprice_regular', '')  + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'rtthemesku', name.replace('-', '')) + ';\n'
    insert_sql = insert_sql + "INSERT INTO abc_postmeta(post_id, meta_key, meta_value) VALUES(%d, '%s', '%s')" % (post_id, 'slide_template', 'default') + ';\n'

   

if __name__ == "__main__":
    list = file_name('/Volumes/Software/timing-fitness/products_pics/YM/temp')
    read_json(list)