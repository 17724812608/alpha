

from common.method import read_case,api_fun,write_result


def excute_fun(filename,sheetname):
    cases = read_case(filename,sheetname) # 定义变量，接收获取测试用例数据
    # print(cases)
    for case in cases:               #循环，挨个取值
        case_id = case['case_id']    #获取case_id
        url = case['url']             #获取url
        data = eval(case['data'])           #获取data
        expect = eval(case['expected'])     #获取期望

        #获取期望
        expect_code = expect['code']
        expect_msg = expect['msg']
        print('预期结果:code:{},msg为{}'.format(expect_code,expect_msg))

        #调用接口
        real_result = api_fun(url=url,data=data)   #前面的url是函数定义的形参，后者是实际参数，定义变量
        #获取实际的code，msg
        real_code = real_result['code']
        real_msg = real_result['msg']
        print('实际结果:code:{},msg为{}'.format(real_code,real_msg))

        #断言
        if expect_code==real_code and expect_msg==real_msg:
            print('第{}条测试用例执行通过'.format(case_id))
            final_re = 'passed'
        else:
            print('第{}条测试用例执行不通过'.format(case_id))
            final_re = 'failed'
        print('*'*50)
        #写入最终测试结果到Excel
        write_result(filename,sheetname,case_id+1,8,final_re)


#调用excete_fun对login接口自动化测试
excute_fun('C:\Users\曹贺杰.LAPTOP-Q6E1SRM0\.jenkins\workspace\scb22α\\test_data\\testcase_api_wuye.xlsx', 'login')
#代码分层结构，不在同级了，写绝对路径
#'\'不识别，需要做转译