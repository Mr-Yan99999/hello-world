from CRM_Style.website.test_case.page_object.LoginCRM import *
from CRM_Style.website.test_case.page_object.serach_patient import *
from CRM_Style.website.test_case.page_object.upload_STLAndDDM import *
from CRM_Style.website.test_case.page_object.dsign_Scheme import *
from CRM_Style.website.test_case.page_object.upload_ods import *
from CRM_Style.website.test_case.page_object.accept_Alert import *
from CRM_Style.website.test_case.page_object.offline_new_guijiao import *
from CRM_Style.website.test_case.page_object.offline_new_photo import *
from CRM_Style.website.test_case.page_object.finish_phase import *
from CRM_Style.website.test_case.page_object.offline_middle_guijiao import *
from CRM_Style.website.test_case.page_object.offline_middle_photo import *
from CRM_Style.website.test_case.page_object.quality_reject import *
from CRM_Style.website.test_case.page_object.quality_conformance import *
from CRM_Style.website.test_case.page_object.no_treatment import *
from CRM_Style.website.test_case.page_object.word_scheme import *
from CRM_Style.driver.driver import *
from selenium.webdriver.support import expected_conditions as EC
import traceback
import sys

class Create3D():
    def __init__(self,username,password,url):
        self.driver=browser()
        self.caseid = get_caseid()
        self.username=username
        self.password=password
        self.url=url

    #这是双膜的第1阶段的第1个方案
    def test_douple3D_1_1(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            print(">>>开始创建病例号为 %s 的3D方案" % (self.caseid))
            print(">>>准备文件重命名、更改json")
            rename_file(0,self.caseid,"1_1")   #这个应该返回一个ods列表
            get_new_json(0,self.caseid)
            print(">>>查找病例")
            searchPatient(self.driver, self.caseid)
            print(">>>上传咬合stl以及ddm")
            uploadStlAndDdm(self.driver, 0,self.caseid,"1_1",0)
            print(">>>设计方案中......")
            dsignScheme(self.driver)
            print(">>>上传ods四文件")
            uploadOds(self.driver, 0,self.caseid, "1_1",0,1,1)
            print(">>>加载同步以及处理警告弹窗")
            acceptAlert(self.driver)
            print(">>>病例号为 %s 的3D方案创建成功" % (self.caseid) + "\n")
        except Exception as e:
            print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (self.caseid) + "\n",e)
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)
        self.driver.quit()

    # 这是双膜的第1阶段的第2个方案
    def test_douple3D_1_2(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            print(">>>开始创建病例号为 %s 的3D方案" % (self.caseid))
            print(">>>准备文件重命名、更改json")
            rename_file(0,self.caseid,"1_2")   #这个应该返回一个ods列表
            get_new_json(0,self.caseid)
            print(">>>查找病例")
            searchPatient(self.driver, self.caseid)
            print(">>>设计方案中......")
            dsignScheme(self.driver)
            print(">>>上传ods四文件")
            uploadOds(self.driver,0,self.caseid, "1_2",0,2,2)
            print(">>>加载同步以及处理警告弹窗")
            acceptAlert(self.driver)
            print(">>>病例号为 %s 的3D方案创建成功" % (self.caseid) + "\n")
        except:
            print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (self.caseid) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)
        self.driver.quit()

    # 这是双膜的第1阶段的第3个方案
    def test_douple3D_1_3(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            print(">>>开始创建病例号为 %s 的3D方案" % (self.caseid))
            print(">>>准备文件重命名、更改json")
            rename_file(0,self.caseid,"1_3")   #这个应该返回一个ods列表
            get_new_json(0,self.caseid)
            print(">>>查找病例")
            searchPatient(self.driver, self.caseid)
            print(">>>设计方案中......")
            dsignScheme(self.driver)
            print(">>>上传ods四文件")
            uploadOds(self.driver, 0,self.caseid, "1_3",0,3,3)
            print(">>>加载同步以及处理警告弹窗")
            acceptAlert(self.driver)
            print(">>>病例号为 %s 的3D方案创建成功" % (self.caseid) + "\n")
        except:
            print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (self.caseid) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)
        self.driver.quit()

    # 这是双膜的第1阶段的第4个方案
    def test_douple3D_1_4(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            print(">>>开始创建病例号为 %s 的3D方案" % (self.caseid))
            print(">>>准备文件重命名、更改json")
            rename_file( 0,self.caseid,"1_4")   #这个应该返回一个ods列表
            get_new_json( 0,self.caseid)
            print(">>>查找病例")
            searchPatient(self.driver, self.caseid)
            print(">>>设计方案中......")
            dsignScheme(self.driver)
            print(">>>上传ods四文件")
            uploadOds(self.driver,0, self.caseid, "1_4",0,4,4)
            print(">>>加载同步以及处理警告弹窗")
            acceptAlert(self.driver)
            print(">>>病例号为 %s 的3D方案创建成功" % (self.caseid) + "\n")
        except:
            print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (self.caseid) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)
        self.driver.quit()

    # 这是双膜的第2阶段的第1个方案
    def test_douple3D_2_1(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            print(">>>开始创建病例号为 %s 的3D方案" % (self.caseid))
            print(">>>准备文件重命名、更改json")
            rename_file(0,self.caseid,"2_1")   #这个应该返回一个ods列表
            get_new_json(0,self.caseid)
            print(">>>查找病例")
            searchPatient(self.driver, self.caseid)
            self.driver.switch_to.window(get_handles(self.driver)[1])
            uploadStlAndDdm(self.driver, 0,self.caseid,"1_1",1)
            print(">>>设计方案中......")
            dsignScheme(self.driver)
            print(">>>上传ods四文件")
            uploadOds(self.driver,0, self.caseid, "2_1",1,1,1)
            print(">>>加载同步以及处理警告弹窗")
            acceptAlert(self.driver)
            print(">>>病例号为 %s 的3D方案创建成功" % (self.caseid) + "\n")
        except:
            print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (self.caseid) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)
        self.driver.quit()

    # 这是双膜的第2阶段的第2个方案
    def test_douple3D_2_2(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            print(">>>开始创建病例号为 %s 的3D方案" % (self.caseid))
            print(">>>准备文件重命名、更改json")
            rename_file(0,self.caseid, "2_2")  # 这个应该返回一个ods列表
            get_new_json(0,self.caseid)
            print(">>>查找病例")
            searchPatient(self.driver, self.caseid)
            print(">>>设计方案中......")
            dsignScheme(self.driver)
            print(">>>上传ods四文件")
            uploadOds(self.driver,0, self.caseid, "2_2", 1, 2, 2)
            print(">>>加载同步以及处理警告弹窗")
            acceptAlert(self.driver)
            print(">>>病例号为 %s 的3D方案创建成功" % (self.caseid) + "\n")
        except:
            print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (self.caseid) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)
        self.driver.quit()

    # 这是双膜的第3阶段的第1个方案
    def test_douple3D_3_1(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            print(">>>开始创建病例号为 %s 的3D方案" % (self.caseid))
            print(">>>准备文件重命名、更改json")
            rename_file(0, self.caseid, "3_1")  # 这个应该返回一个ods列表
            get_new_json(0,self.caseid)
            print(">>>查找病例")
            searchPatient(self.driver, self.caseid)
            uploadStlAndDdm(self.driver,0, self.caseid,"1_2",2)
            print(">>>设计方案中......")
            dsignScheme(self.driver)
            print(">>>上传ods四文件")
            uploadOds(self.driver, 0,self.caseid, "3_1", 2, 1, 1)
            print(">>>加载同步以及处理警告弹窗")
            acceptAlert(self.driver)
            print(">>>病例号为 %s 的3D方案创建成功" % (self.caseid) + "\n")
        except:
            print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (self.caseid) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)
        self.driver.quit()

    #这是单膜的第1阶段的第1个方案
    def test_single3D_1_1(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            print(">>>开始创建病例号为 %s 的3D方案" % (self.caseid))
            print(">>>准备文件重命名、更改json")
            rename_file(1,self.caseid,"1_1")   #这个应该返回一个ods列表
            get_new_json(1,self.caseid)
            print(">>>查找病例")
            searchPatient(self.driver, self.caseid)
            print(">>>上传咬合stl以及ddm")
            uploadStlAndDdm(self.driver,1,self.caseid,"1_1",0)
            print(">>>设计方案中......")
            dsignScheme(self.driver)
            print(">>>上传ods四文件")
            uploadOds(self.driver,1, self.caseid, "1_1",0,1,1)
            print(">>>加载同步以及处理警告弹窗")
            acceptAlert(self.driver)
            print(">>>病例号为 %s 的3D方案创建成功" % (self.caseid) + "\n")
        except:
            print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (self.caseid) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)
        self.driver.quit()

    # 这是单膜的第1阶段的第2个方案
    def test_single3D_1_2(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            print(">>>开始创建病例号为 %s 的3D方案" % (self.caseid))
            print(">>>准备文件重命名、更改json")
            rename_file(1,self.caseid,"1_2")   #这个应该返回一个ods列表
            get_new_json(1,self.caseid)
            print(">>>查找病例")
            searchPatient(self.driver, self.caseid)
            print(">>>设计方案中......")
            dsignScheme(self.driver)
            print(">>>上传ods四文件")
            uploadOds(self.driver,1, self.caseid, "1_2",0,2,2)
            print(">>>加载同步以及处理警告弹窗")
            acceptAlert(self.driver)
            print(">>>病例号为 %s 的3D方案创建成功" % (self.caseid) + "\n")
        except:
            print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (self.caseid) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)
        self.driver.quit()

    # 这是单膜的第1阶段的第3个方案
    def test_single3D_1_3(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            print(">>>开始创建病例号为 %s 的3D方案" % (self.caseid))
            print(">>>准备文件重命名、更改json")
            rename_file(1,self.caseid,"1_3")   #这个应该返回一个ods列表
            get_new_json(1,self.caseid)
            print(">>>查找病例")
            searchPatient(self.driver, self.caseid)
            print(">>>设计方案中......")
            dsignScheme(self.driver)
            print(">>>上传ods四文件")
            uploadOds(self.driver,1, self.caseid, "1_3",0,3,3)
            print(">>>加载同步以及处理警告弹窗")
            acceptAlert(self.driver)
            print(">>>病例号为 %s 的3D方案创建成功" % (self.caseid) + "\n")
        except:
            print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (self.caseid) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)
        self.driver.quit()

    # 这是单膜的第1阶段的第4个方案
    def test_single3D_1_4(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            print(">>>开始创建病例号为 %s 的3D方案" % (self.caseid))
            print(">>>准备文件重命名、更改json")
            rename_file(1,self.caseid,"1_4")   #这个应该返回一个ods列表
            get_new_json(1,self.caseid)
            print(">>>查找病例")
            searchPatient(self.driver, self.caseid)
            print(">>>设计方案中......")
            dsignScheme(self.driver)
            print(">>>上传ods四文件")
            uploadOds(self.driver,1, self.caseid, "1_4",0,4,4)
            print(">>>加载同步以及处理警告弹窗")
            acceptAlert(self.driver)
            print(">>>病例号为 %s 的3D方案创建成功" % (self.caseid) + "\n")
        except:
            print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (self.caseid) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)
        self.driver.quit()

    # 这是单膜的第2阶段的第1个方案
    def test_single3D_2_1(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            print(">>>开始创建病例号为 %s 的3D方案" % (self.caseid))
            print(">>>准备文件重命名、更改json")
            rename_file(1,self.caseid,"2_1")   #这个应该返回一个ods列表
            get_new_json(1,self.caseid)
            print(">>>查找病例")
            searchPatient(self.driver, self.caseid)
            uploadStlAndDdm(self.driver, 1, self.caseid, "1_1", 1)
            print(">>>设计方案中......")
            dsignScheme(self.driver)
            print(">>>上传ods四文件")
            uploadOds(self.driver,1,self.caseid, "2_1",1,1,1)
            print(">>>加载同步以及处理警告弹窗")
            acceptAlert(self.driver)
            print(">>>病例号为 %s 的3D方案创建成功" % (self.caseid) + "\n")
        except:
            print("\033[31m 注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (self.caseid) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)
        self.driver.quit()

    # 这是单膜的第2阶段的第2个方案
    def test_single3D_2_2(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            print(">>>开始创建病例号为 %s 的3D方案" % (self.caseid))
            print(">>>准备文件重命名、更改json")
            rename_file(1,self.caseid, "2_2")  # 这个应该返回一个ods列表
            get_new_json(1,self.caseid)
            print(">>>查找病例")
            searchPatient(self.driver, self.caseid)
            print(">>>设计方案中......")
            dsignScheme(self.driver)
            print(">>>上传ods四文件")
            uploadOds(self.driver, 1,self.caseid, "2_2", 1, 2, 2)
            print(">>>加载同步以及处理警告弹窗")
            acceptAlert(self.driver)
            print(">>>病例号为 %s 的3D方案创建成功" % (self.caseid) + "\n")
        except:
            print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (self.caseid) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)
        self.driver.quit()

    # 这是单膜的第3阶段的第1个方案
    def test_single3D_3_1(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            print(">>>开始创建病例号为 %s 的3D方案" % (self.caseid))
            print(">>>准备文件重命名、更改json")
            rename_file(1,self.caseid, "3_1")  # 这个应该返回一个ods列表
            get_new_json(1,self.caseid)
            print(">>>查找病例")
            searchPatient(self.driver, self.caseid)
            uploadStlAndDdm(self.driver, 1, self.caseid, "1_1", 2)
            print(">>>设计方案中......")
            dsignScheme(self.driver)
            print(">>>上传ods四文件")
            uploadOds(self.driver,1, self.caseid, "3_1", 2, 1, 1)
            print(">>>加载同步以及处理警告弹窗")
            acceptAlert(self.driver)
            print(">>>病例号为 %s 的3D方案创建成功" % (self.caseid) + "\n")
        except:
            print("\033[31m注意 ：病例号为 %s的病例创建3D失败，继续执行下一个\033[0m" % (self.caseid) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)
        self.driver.quit()

    def test_offline_new_guijiao(self,patientname,institutions,doctorname,):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            randomValue()
            print(">>>开始创建线下新病例硅胶")
            offline_new_guijiao(self.driver, patientname,institutions,doctorname)
            print(">>>创建完成")
        except:
            print("\033[31m注意 :患者名为 %s的线下病例创建失败，继续执行下一个\033[0m" % (patientname) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)

    def test_offline_new_photo(self,patientname,institutions,doctorname,):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            print(">>>开始创建线下新病例口内照")
            offline_new_photo(self.driver, patientname,institutions,doctorname)
            print(">>>创建完成")
        except:
            print("\033[31m注意 :患者名为 %s的线下病例创建失败，继续执行下一个\033[0m" % (patientname) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)

    def test_offline_middle_guijiao(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            finish_phase(self.driver,self.caseid)
            print(">>>开始创建线下中期硅胶")
            offline_middle_guijiao(self.driver, self.caseid)
            print(">>>创建完成")
        except:
            print("\033[31m注意 :病例序号为 %s的线下中期硅胶病例创建失败，继续执行下一个\033[0m" % (self.caseid) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)

    def test_offline_middle_photo(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            finish_phase(self.driver,self.caseid)
            print(">>>开始创建线下中期口内照")
            offline_middle_photo(self.driver, self.caseid)
            print(">>>创建完成")
        except:
            print("\033[31m注意 :病例序号为 %s的线下中期口内照病例创建失败，继续执行下一个\033[0m" % (self.caseid) + "\n")
            self.driver.switch_to.window(get_handles(self.driver)[0])
            traceback_info = traceback.format_exc()
            print(traceback_info)

    def test_quality_reject(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        searchPatient(self.driver,self.caseid)
        self.driver.switch_to.window(get_handles(self.driver)[1])
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[0])
        Create_Quality_Reject(self.driver)
        print("创建成功")

    def test_quality_conformance(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        searchPatient(self.driver, self.caseid)
        self.driver.switch_to.window(get_handles(self.driver)[1])
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[0])
        Create_Quality_Conformance(self.driver)
        print("创建成功")

    def test_no_treatment(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        searchPatient(self.driver, self.caseid)
        self.driver.switch_to.window(get_handles(self.driver)[1])
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[0])
        Create_No_Treatment(self.driver)
        print("创建成功")

    def test_word_scheme(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        searchPatient(self.driver, self.caseid)
        self.driver.switch_to.window(get_handles(self.driver)[1])
        self.driver.close()
        self.driver.switch_to.window(get_handles(self.driver)[0])
        Create_Word_scheme(self.driver)
        print("创建成功")

    def test_finish_phase(self):
        print(">>>开始登录crm，请耐心等候......" + "\n")
        Login(self.driver, self.url, self.username, self.password)
        try:
            finish_phase(self.driver,self.caseid)
            sleep(2)
            self.driver.quit()
        except:
            print("病例号为%s的病例结束阶段失败，继续执行下一个"%(self.caseid))
            traceback_info = traceback.format_exc()
            print(traceback_info)

def run(username,password,url,institutions,doctorname):
    while True:
        if get_num() == "0_1_1":
            Create3D(username, password, url).test_douple3D_1_1()
            break
        elif get_num() == "0_1_2":
            Create3D(username, password, url).test_douple3D_1_2()
            break
        elif get_num() == "0_1_3":
            Create3D( username, password, url).test_douple3D_1_3()
            break
        elif get_num() == "0_1_4":
            Create3D(username, password, url).test_douple3D_1_4()
            break
        elif get_num() == "0_2_1":
            Create3D(username, password, url).test_douple3D_2_1()
            break
        elif get_num() == "0_2_2":
            Create3D(username, password, url).test_douple3D_2_2()
            break
        elif get_num() == "0_3_1":
            Create3D(username, password, url).test_douple3D_3_1()
            break
        elif get_num() == "1_1_1":
            Create3D(username, password, url).test_single3D_1_1()
            break
        elif get_num() == "1_1_2":
            Create3D(username, password, url).test_single3D_1_2()
            break
        elif get_num() == "1_1_3":
            Create3D(username, password, url).test_single3D_1_3()
            break
        elif get_num() == "1_1_4":
            Create3D(username, password, url).test_single3D_1_4()
            break
        elif get_num() == "1_2_1":
            Create3D(username, password, url).test_single3D_2_1()
            break
        elif get_num() == "1_2_2":
            Create3D(username, password, url).test_single3D_2_2()
            break
        elif get_num() == "1_3_1":
            Create3D(username, password, url).test_single3D_3_1()
            break
        elif get_num() == "新建硅胶":
            Create3D(username, password, url).test_offline_new_guijiao(get_patientname(),institutions,doctorname)
            break
        elif get_num() == "新建口内照":
            Create3D(username, password, url).test_offline_new_photo(get_patientname(),institutions,doctorname)
            break
        elif get_num() == "中期硅胶":
            Create3D(username, password, url).test_offline_middle_guijiao()
            break
        elif get_num() == "中期口内照":
            Create3D( username, password, url).test_offline_middle_photo()
            break
        elif get_num() == "质检合格":
            Create3D(username, password, url).test_quality_reject()
            break
        elif get_num() == "质检不合格":
            Create3D(username, password, url).test_quality_conformance()
            break
        elif get_num() == "不收治":
            Create3D(username, password, url).test_no_treatment()
            break
        elif get_num() == "文字方案":
            Create3D( username, password, url).test_word_scheme()
            break
        elif get_num() == "结束阶段":
            Create3D( username, password, url).test_finish_phase()
            break
        else:
            sleep(3)
            print("指令格式不正确，请重新输入")