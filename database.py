
import csv, os, copy


class Database:
    """
    Table in Table
    """
    def __init__(self):
        self.database = []

    def insert(self, table):
        self.database.append(table)

    def search(self, table_name):
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None


class Table:
    def __init__(self, table_name, table):
        self.table = table
        self.table_name = table_name

    def update(self, ID, key, value):
        for row in self.table:
            row_list = [x for x in row.keys()]
            if row[row_list[0]] == ID:  # row.keys()[0] get first key of dict, assuming ID
                row[key] = value
                return

    def find(self, ID, key):
        for row in self.table:
            row_list = [x for x in row.keys()]
            if row[row_list[0]] == ID:  # row.keys()[0] get first key of dict, assuming ID
                return row[key]

    def join(self, other_table, common_key):
        joined_table = Table(
            self.table_name + '_joins_' + other_table.table_name, [])
        for item1 in self.table:
            for item2 in other_table.table:
                if item1[common_key] == item2[common_key]:
                    dict1 = copy.deepcopy(item1)
                    dict2 = copy.deepcopy(item2)
                    dict1.update(dict2)
                    joined_table.table.append(dict1)
        return joined_table

    def filter(self, condition):
        filtered_table = Table(self.table_name + '_filtered', [])
        for item1 in self.table:
            if condition(item1):
                filtered_table.table.append(item1)
        return filtered_table

    def aggregate(self, function, aggregation_key):
        temps = []
        for item1 in self.table:
            if self.__is_float(item1[aggregation_key]):
                temps.append(float(item1[aggregation_key]))
            else:
                temps.append(item1[aggregation_key])
        return function(temps)

    def __is_float(self, element):
        if element is None:
            return False
        try:
            float(element)
            return True
        except ValueError:
            return False

    def select(self, attributes_list):
        temps = []
        for item1 in self.table:
            dict_temp = {}
            for key in item1:
                if key in attributes_list:
                    dict_temp[key] = item1[key]
            temps.append(dict_temp)
        return temps

    def insert(self, dictionary):
        self.table.append(dictionary)

    def clear(self):  # use with caution
        self.table = []

    def remove_dict(self, dictionary):
        for row in self.table:
            if row == dictionary:
                self.table.remove(row)

    def remove_this(self, ID):
        for row in self.table:
            row_list = [x for x in row.keys()]
            if row[row_list[0]] == ID:
                self.table.remove(row)

    def __str__(self):
        return self.table_name + ':' + str(self.table)
