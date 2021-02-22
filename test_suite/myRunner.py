# -*- coding: utf-8 -*-
# __author__=luhu

from airtest.cli.runner import AirtestCase, run_script
from argparse import *
import airtest.report.report as report
import jinja2
import shutil
import os
import io
import unittest


class CustomAirtestCase(unittest.TestCase):
    def setUp(self):
        print("custom setup")
        pass

    def tearDown(self):
        print("custom tearDown")
        pass


class MyAirtest(CustomAirtestCase):
    # my_scrpit_dir = 'D:\\Users\\hulu\\PycharmProjects\\my_airtest\\test_suite'

    def run_air(self, my_suite_dir=None, device=None):
        # 聚合结果
        # if device is None:
        #     device = ['android://127.0.0.1:5037?cap_method=JAVACAP^&^&ori_method=ADBORI^&^&touch_method=ADBTOUTH']
        results = []
        # # 获取所有用例集
        # root_log = root_dir
        # if os.path.isdir(root_log):
        #     shutil.rmtree(root_log)
        # else:
        #     os.makedirs(root_log)
        #     print(str(root_log) + 'is created')

        for f in os.listdir(my_suite_dir):
            if f.endswith(".air"):
                airName = f
                script = os.path.join(my_suite_dir, f)    # 拼接脚本路径
                print(script)
                nginx_path = 'D:\\Users\\hulu\\nginx-1.17.9\\html'
                data_log = os.path.join(nginx_path, 'log' + '\\' + airName.replace('.air', ''))+'/log'   # 生成报告的路径
                report_log = os.path.join(nginx_path, 'log/'+ airName.replace('.air', ''))

                print(data_log)
                if os.path.isdir(data_log):
                    shutil.rmtree(data_log)
                else:
                    os.makedirs(data_log)
                    print(str(data_log) + 'is created')
                log_html_path = os.path.join(nginx_path, 'log' + '\\' + airName.replace('.air', ''))\
                                + '/log/log.html'
                args = Namespace(device=device, log=data_log, recording=None, script=script)   # 跑脚本之后的数据log
                try:
                    run_script(args, AirtestCase)
                except:
                    pass
                finally:
                    static_root = 'http://10.32.34.8:8080/static'
                    rpt = report.LogToHtml(script, data_log, static_root=static_root, export_dir=report_log)
                    rpt.report("log_template.html", log_html_path)

                    result = {"name": airName.replace('.air', ''), "result": rpt.test_result}
                    results.append(result)
        # 生成聚合报告
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(my_suite_dir),
            extensions=(),
            autoescape=True
        )
        template = env.get_template("summary_template.html", my_suite_dir)  # summary模板地址
        html = template.render({"results": results})
        summary_path = 'D:\\Users\\hulu\\nginx-1.17.9\\html'
        output_file = os.path.join(summary_path, "summary.html")
        with io.open(output_file, 'w', encoding="utf-8") as f:
            f.write(html)
        print(output_file)


if __name__ == '__main__':
    test = MyAirtest()
    device = ['android://127.0.0.1:5037?cap_method=JAVACAP^&^&ori_method=ADBORI^&^&touch_method=ADBTOUTH']
    test.run_air(my_suite_dir='D:\\Users\\hulu\\PycharmProjects\\my_airtest\\test_suite')   # device=device

