from ctypes import pointer


class Solution():

    def isValid(self, s: str) -> bool:
        input = s

        self.deal_list = []
        self.pointer = 0
        self.left_pair_dict = {'[': ']',
                          '(': ')',
                          '{': '}'}
        self.right_pair_dict = {']': '[',
                           ')': '(',
                           '}': '{'}

        def get_pair(text: str) -> list:
            '''Return:[input_type,pair] eg. ['left','}']'''

            try:
                return ['left', self.left_pair_dict[text]]
            except:
                return ['right', self.right_pair_dict[text]]

        def check(input):
            for single in input:
                [single_type, pair] = get_pair(single)
                if self.pointer == 0 and single_type == 'right':
                    raise Exception('A right without left')
                if single_type == 'left':
                    self.pointer += 1
                    self.deal_list.append(single)
                elif single_type == 'right':
                    if self.deal_list[-1] == pair:
                        self.deal_list.pop()
                        self.pointer -= 1
                    else:
                        raise Exception('Unpair Symbol: '+self.deal_list[-1]+single)
            if self.pointer != 0:
                raise Exception('Unclose Symbol')
            return True

        try:
            check(input)
            return True
        except Exception as e:
            return False
