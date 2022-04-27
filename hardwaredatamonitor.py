
#!usr/bin/env python
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import psutil 

sg.theme('Default1')

frame_cpu = sg.Frame('CPU使用率%', [
[sg.MLine(key='-cput-'+sg.WRITE_ONLY_KEY,size=(8,3))]
])

frame_rem = sg.Frame('メモリ使用率%', [
    [sg.MLine(key='-memt-'+sg.WRITE_ONLY_KEY,size=(8,3))]
])

layout =[frame_cpu,frame_rem],[sg.MenuBar([['詳細',['ハードウェア情報','バージョン情報','終了']]], key='menu')]

window = sg.Window('パフォーマンス', layout, finalize=True,)

cpu = 0
mem = 0
while True:
    
    event, values = window.read(timeout=700)

    if event == sg.WIN_CLOSED or values['menu']=='終了':
        break
    if event == values['menu']=='ハードウェア情報':
        cpucor=psutil.cpu_count()
        cpucor2=psutil.cpu_count(logical=False)
        desk=psutil.disk_usage(path='/').percent
        desapa=psutil.disk_partitions()
        netwook=psutil.net_if_addrs()
        sg.popup_ok("コア数",cpucor,"論理コア数",cpucor2,"ディスク使用率%",desk,"ディスクパーティション",desapa,"ネットワーク情報(自分も何なのか分からない)",netwook ,title = "ハードウェア情報",font=(12))
    if event == values['menu']=='バージョン情報':
        sg.popup_ok("バージョン: 1.0.0",title ="バージョン情報",font=(12))
    mem = psutil.virtual_memory() 
    cpu = psutil.cpu_percent(interval=1)
    window['-memt-'+sg.WRITE_ONLY_KEY].print(mem.percent)
    window['-cput-'+sg.WRITE_ONLY_KEY].print(cpu)
   
window.close()
