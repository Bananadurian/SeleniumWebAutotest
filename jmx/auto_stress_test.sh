#! /usr/bin/env bash


# 压测的时间模板设置为60s，每次20秒
export jmx_template="interface"
export suffix=".jmx"
export jmx_template_filename="${jmx_template}${suffix}"
export os_type="uname"  # 区分max和Linux

# jmeter位置
export jmeter_path="/usr/lib/apache-jmeter-5.5/bin/jmeter"

echo "自动化压测开始"

# 压测并发数列表
thread_number_array=(10 20 30)

for num in "${thread_number_array[@]}"
do
    # 生成对应压测线程的jmx文件
    export jmx_filename="${jmx_template}_${num}${suffix}"
    export jtl_filename="test_${num}.jtl"
    export web_report_path_name="web_report_${num}"

    # 清空之前上一次压测的jmx、jtl、报告文件
    rm -f ${jmx_filename} ${jtl_filename}
    rm -rf ${web_report_path_name}
    # 使用模板创建此次执行的jmx文件
    cp ${jmx_template_filename} ${jmx_filename}
    
    # 根据系统替换jmx文件的参数thread_num
    if [["${os_type}"=="Linux"]]; then
        sed -i "s/thread_num/${num}/g" ${jmx_filename}
    else
        sed -i "" "s/thread_num/${num}/g" ${jmx_filename}
    fi
    echo "生成jmx文件: ${jmx_filename}"

    # 执行脚本生成结果jtl文件，并生成测试报告
    ${jmeter_path} -n -t ${jmx_filename} -l ${jtl_filename} -e -o ${web_report_path_name}
    
    rm -f ${jmx_filename} ${jtl_filename}
done
echo "自动化压测结束"