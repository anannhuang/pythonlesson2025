# python_2025
致理python大數據分析  
[google meet上課網址](https://meet.google.com/qkf-btyj-jnz)
___
## 1. 0503

直播網址：[上午](https://youtube.com/live/ds8RirjEo4M)/[下午](https://www.youtube.com/watch?v=EXC_aE3XmtI)

*今日重點*：
- 設立變數 >> 暫存的值，非資料結構
- 數學運算子/複合指定運算子/運算子的優先順序
- 運算式(會傳出值)/敘述式(不會傳出值)
- 只有數值型別可做數學運算
- 字串型別可相加/做乘法
- 暫時轉換型別
- function(函式)：print()、input()、type()、int()、float()、str()
  
    |int() |float() |str()|
    |:----:|:----:|:----:|
    |整數|浮點數|字串|
    |5|5.0|'5'|

- import function：import math -> .sqrt()  
   *因內建函式庫無開根號函式，故需先從標準函式庫 (Standard Library)匯入math function，再使用math.sqrt()運算
- **perplexity** -> ai搜尋引擎

python是 __`動態型別`__，依據變數判斷型別

__HW: 學習markdown語法__ [github中文版說明](https://gist.github.com/billy3321/1001749662c370887c63bb30f26c9e6e)   
0504練習：   
1. markdown語法：無序子列表、標題大標小標、跳脫字元(反斜線)、畫重點(__粗體__、_斜體_、`短區塊`)、
   連結(\[連結名稱\](網址))、表格(破折號、冒號表示置左置中置右)、縮排(用Tab)、分隔線
3. 數學運算練習




___
## 2. 0510

直播網址：[上午](https://www.youtube.com/watch?v=j6IfJ4IW8ws)/[下午](https://www.youtube.com/watch?v=ubAmIJHRqfk)

*今日重點*：
- 學習程式碼
  1. 數學運算
  2. **流程控制**：主程式區塊(一定執行)、程式流控制\>>判斷(條件式: if)、迴圈(loop)
- 條件式：比較運算子
- 條件判斷：單項選擇(if)、雙項選擇(else)、多項選擇(elif)、巢狀判斷
- 邏輯運算子
- 布林值(bool): True、False
- for 迴圈：遍歷(迭代)\->重複執行
  - for 變數 in 串列資料(list)：for ... in ... **明確知道執行的次數**
  - **資料結構**：資料類型：list、tuple、dictionary、set
- while迴圈：無限迴圈，需要建立變數來控制while的執行與否，放在while迴圈的條件式內
  - while 條件式(傳回布林值)
  - 若wlile迴圈執行條件為True，則一直重複執行，直到條件為False才停止
  - 步驟：建立變數->比較變數->改變變數的值
  - 使迴圈中止：**break / continue**   
    -> **break**會使用在if判斷式中，若成立則`提前跳出迴圈`；**continue**若成立則跳過本次迴圈剩餘程式碼，`直接跳至下一輪迴圈`。





___
## 3. 0517

直播網址：[上午](https://www.youtube.com/watch?v=TD-aKNc1on0)

*今日重點*：
- 基本資料結構 >> 儲存於記憶體(從excel檔、資料庫...儲存至記憶體)
  1. list
  2. dictionary
  3. set >> 支援數學上的集合運算，包括交集（&）、聯集（|）、差集（-）、對稱差集（^）等，非常適合用來處理需要比較、篩選、合併資料的情境
- 結構化程式碼、結構化專案，需使用本地端編輯軟體，例：anaconda(但佔大量記憶體，功能齊全適合初學者使用)、PyCharm(開發python用)、Visual Studio Code(Free and Open Source)
- VS Code >> windows版本要自行安裝git >> 將終端機設定預設為cmd
- [設定教學](https://github.com/roberthsu2003/python/tree/master/vscode%E8%A8%AD%E5%AE%9A)

  ### **git設定**
    ```
    git config --global user.name "Ann Huang"
    git config --global user.email "ann82925902@gmail.com"
    git config --global pull.rebase false
在VS code：原始檔控制 >> github-複製存放庫 >> 存放位置：文件 >> 新增資料夾：github >> 選取為存放資料的目的地







