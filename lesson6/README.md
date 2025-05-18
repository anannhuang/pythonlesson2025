## 3. 0517

直播網址：[上午](https://www.youtube.com/watch?v=TD-aKNc1on0)/[下午](https://www.youtube.com/watch?v=CRB_ymO10ac)

### *今日重點*：
- 基本資料結構 >> 儲存於記憶體(從excel檔、資料庫...儲存至記憶體)
  1. list
  2. dictionary
  3. set >> 支援數學上的集合運算，包括交集（&）、聯集（|）、差集（-）、對稱差集（^）等，非常適合用來處理需要比較、篩選、合併資料的情境
- 結構化程式碼、結構化專案，需使用本地端編輯軟體，例：anaconda(但佔大量記憶體，功能齊全適合初學者使用)、PyCharm(開發python用)、Visual Studio Code(Free and Open Source)
- 建立虛擬環境：每個不同的專案都要建立不同的虛擬環境
- 安裝VS Code >> windows版本要自行安裝git >> 將終端機設定預設為cmd
- VS code中的各項設定：安裝python、jupyter、miniconda(虛擬環境)
- 製作專案：建立.py檔，並在虛擬環境中執行
---

### [**VS code設定教學**](https://github.com/roberthsu2003/python/tree/master/vscode%E8%A8%AD%E5%AE%9A)

步驟：
1. [安裝VS code](https://code.visualstudio.com/download)
2. 安裝VS code中的模組：**chinese(中文介面)、`python`、`jupyter`**  
   *安裝完chinese若未自動更改為中文介面>>crtl+shift+P>>輸入"display">>Configure Display Language>>設定改為繁中
3. [安裝git](https://git-scm.com/downloads/win)：
   安裝後，先在"開始"搜尋git bash，確認開啟有介面，並重啟VS code.
4. 在VS code中更改終端機預設選項為cmd
5. 先在終端機輸入下方指令確認是否安裝成功：
    ```
    git --version
    ```
  
  #### **設定git**
    git config --global user.name "Ann Huang"
    git config --global user.email "ann82925902@gmail.com"
    git config --global pull.rebase false

輸入下方指令確認是否設定完成：

    git config --list

在VS code：原始檔控制 >> github-複製存放庫(從github上複製) >> 存放位置：文件 >> 新增資料夾：github >> 選取為存放資料的目的地>>複製的資料庫便會出現在檔案總管   

**[安裝miniconda](https://www.anaconda.com/download/success)**   
<u>*需額外勾選同意將miniconda加入my PATH environment variable* \->(不加入會無法輸入指令)</u> 

[**miniconda設定教學**](https://github.com/roberthsu2003/python/tree/master/mini_conda)   
步驟：   
在終端機輸入下方指令確認是否安裝成功：   
  ~~~
  conda --version
  ~~~

  #### 取消termail一開始就進入base虛擬環境
    conda config --set auto_activate_base false

  #### conda init
    conda init --all bash

  #### 檢查目前已建立的虛擬環境
    conda env list

  #### 建立虛擬環境 (myenv改為自訂的環境名稱)
    conda create --name myenv python=3.10

  #### 啟動虛擬環境 (myenv改為自訂的環境名稱)
    conda activate myenv

  #### 離開虛擬環境
    conda deactivate


新增資料夾、新增任何修改，先儲存，變更>>暫存變更>>輸入說明>>提交>>同步變更>>VS code及GitHub就會同步剛才做的修改。

---
### - 製作專案：新增.py檔    
  在終端機執行，注意是否在選定的虛擬環境中執行專案，若要執行的程式在根目錄的資料夾中，需要先進入該資料夾。   
  e.g. 要執行在PYTHONLESSON2025的lesson6資料夾中的lesson6_3.py，可以在lesson6資料夾處按右鍵>>在整合式終端機中開啟>>會看到終端機中執行的虛擬環境為何以及專案所處的資料夾>>輸入指令：python lesson6_3.py>>即可執行專案。   
  在終端機右下角更改虛擬環境。   
  **一個專案對應一個虛擬環境！**

### - 結構式程式碼
  自訂function：用"def"，設定一個功能，不算在主程式中的程式碼
  要呼叫自訂的function才會執行程式
  將複雜的程式碼包裝起來，變成簡單的程式碼，更有邏輯！！   
  [參考lesson6_3.py](https://github.com/anannhuang/pythonlesson2025/blob/main/lesson6/lesson6_3.py)   
  ```
  def function1():
  ```

**記憶體區塊**
執行程式時呼叫程式，會新增記憶體，待流程跑完，即釋放記憶體。