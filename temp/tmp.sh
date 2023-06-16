#! /bin/bash
function get_page_data() {
    # 获取设备页面的xml数据
    # adb shell uiautomator dump：dump页面的xml数据
    # adb shell cat： 查看页面的数据
    # sed 's#/><#/>|<#g'：把数据的 /><# 全部替换为 />|<
    # awk 'BEGIN{RS="|"}{print $0}'： 使用 | 对数据进行分行
    # awk -F \" '{if($4){print $4}}'：使用 " 分割数据，如果第4列数据不为空的时候打印数据
    adb shell uiautomator dump && adb shell cat /sdcard/window_dump.xml |
        sed 's#/><#/>|<#g' |
        awk 'BEGIN{RS="|"}{print $0}' |
        awk -F \" '{if($4){print $4}}'
}

function main() {
    # 获取设备上滑的坐标
    # adb shell wm size：屏幕分辨率
    # -F "x| "：使用x或空格分割结果
    swipe_up=$(
        adb shell wm size |
            awk -F "x| " '{width=$3;height=$4;print width/2, height*0.7, width/2, height*0.4}'
    )
    swipe_down=$(
        adb shell wm size |
            awk -F "x| " '{width=$3;height=$4;print width/2, height*0.3, width/2, height*0.7}'
    )
    i=0
    # 这里循环了3次操作
    while (($i < 3)); do
        # 上滑
        adb shell input swipe $swipe_up
        # 获取页面的应用数据
        get_page_data
        sleep 2
        # 下滑
        adb shell input swipe $swipe_down
        get_page_data
        echo "$swipe_up -- $swipe_down"
        let "i++"
    done
}
main
