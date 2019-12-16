---
title: boma網頁專題作引用
tags: python, note, django
---
## boma網頁專題作業引用步驟
### 一、
1. 到專案資料夾右鍵開啟 **Git bash** 或命令提示字元cmd
2. 輸入： **pip install pipenv**
3. 建立虛擬環境-產生Python 3虛擬環境： **pipenv --three** 
4. 安裝所有套件： **pipenv install**
5. 看裝了那些：**type Pipfile** 
6. 執行虛擬環境：**pipenv shell**
7. 查看是否在虛擬環境中
```python=
$ which python
/c/Users/ben/.virtualenvs/ntub-abs-check-zYx6CQbe/Scripts/python
```
8. 建立一個遷移（migration）檔案：**`python manage.py makemigrations`**
9. 建立 DB：**`python manage.py migrate`**
10. 建立 super user：**`python manage.py createsuperuser`**
11. 執行 Server：**`python manage.py runserver`**
