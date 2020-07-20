

class find_all:
    @staticmethod
    def find(target_list,condition):
        for item in target_list:
            if condition(item):
                print(item)
    @staticmethod
    def get_count(target_list,condition):
        init_count=0
        for item in target_list:
            if condition(item):
                init_count+=1
        print(init_count)

    @staticmethod
    def judge_info(target_list,condition):
        for item in target_list:
            if condition(item):
                print("存在如:",item)
                break

        else:
            print("不存在")

    @staticmethod
    def get_sum(target_list,condition):
        sum_content=0
        for item in target_list:
            sum_content+=condition(item)
        return sum_content

    @staticmethod
    def get_list(target_list,condition):
        list_value=[]
        for item in target_list:
            list_value.append(condition(item))
        return list_value

    @staticmethod
    def get_max(target_list,condition):
        max_value=0
        max_name=0
        for item in target_list:
            if max_value<condition(item):
                max_value=condition(item)
                max_name=item.name
        return max_name

    @staticmethod
    def uporder_list(target_list,handle):
        for i in range(len(target_list)):
            for s in range(i,len(target_list)):
                if handle(target_list[i])>handle(target_list[s]):
                    target_list[s],target_list[i]=target_list[i],target_list[s]

    @staticmethod
    def get_min(target_list,condition):
        min_value=0
        min_name=target_list[0].name
        for item in target_list:
            if min_value>condition(item):
                min_value=condition(item)
                min_name=item.name
        return min_name


    @staticmethod
    def downorder_list(target_list,handle):
        for i in range(len(target_list)):
            for s in range(i,len(target_list)):
                if handle(target_list[i])<handle(target_list[s]):
                    target_list[s],target_list[i]=target_list[i],target_list[s]


    @staticmethod
    def remove_value(target_list,condition):
        for item in target_list:
            if condition(item):
                target_list.remove(item)
        return target_list






















