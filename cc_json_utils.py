import cc_data


def make_cc_data_from_json(json_file):
    cc_data_file = cc_data.CCDataFile()

    for json_level in json_file["levels"]:
        # print(json_level)
        cc_level = cc_data.CCLevel()
        cc_level.level_number = json_level["level_num"]
        cc_level.time = json_level["time_limit"]
        cc_level.num_chips = json_level["chip_count"]
        cc_level.upper_layer = json_level["up_layer"]
        cc_level.lower_layer = json_level["low_layer"]

        json_fields = json_level["fields"]
        for json_field in json_fields:
            field_type = json_field["type"]

            if field_type == "title":
                title = json_field["title"]
                cc_title_field = cc_data.CCMapTitleField(title)
                cc_level.add_field(cc_title_field)

            elif field_type == "hint":
                hint = json_field["hint"]
                cc_map_hint_field = cc_data.CCMapHintField(hint)
                cc_level.add_field(cc_map_hint_field)

            elif field_type == "password":
                password = json_field["password"]
                cc_encoded_password_field = cc_data.CCEncodedPasswordField(password)
                cc_level.add_field(cc_encoded_password_field)

            elif field_type == "monsters":
                json_monster_list = json_field["monsters"]
                monsters = []
                for monster in json_monster_list:
                    x = monster[0]
                    y = monster[1]
                    monsters.append(cc_data.CCCoordinate(x, y))
                    cc_monster_move_field = cc_data.CCMonsterMovementField(monsters)
                    cc_level.add_field(cc_monster_move_field)
                    # print (monster)

        cc_data_file.levels.append(cc_level)

    return cc_data_file